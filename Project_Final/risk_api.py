from pathlib import Path
from typing import Any, Dict, List, Tuple

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field


APP_DIR = Path(__file__).resolve().parent
ARTIFACT_PATH = APP_DIR / "loan_model_artifacts.joblib"
artifacts = joblib.load(ARTIFACT_PATH)
MODELS = artifacts["models"]
FEATURE_COLUMNS = artifacts["feature_columns"]
ENCODING_MAPS = artifacts["encoding_maps"]
NOMINAL_FEATURES = artifacts["nominal_features"]
DEFAULT_MODEL_NAME = artifacts["default_model_name"]


class LoanApplication(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    age: int = Field(alias="Age", ge=18)
    income: float = Field(alias="Income", gt=0)
    loan_amount: float = Field(alias="LoanAmount", gt=0)
    credit_score: int = Field(alias="CreditScore", ge=300, le=850)
    months_employed: int = Field(alias="MonthsEmployed", ge=0)
    num_credit_lines: int = Field(alias="NumCreditLines", ge=1)
    interest_rate: float = Field(alias="InterestRate", gt=0, le=100)
    loan_term: int = Field(alias="LoanTerm", gt=0)
    dti_ratio: float = Field(alias="DTIRatio", ge=0, le=1)
    education: str = Field(alias="Education")
    employment_type: str = Field(alias="EmploymentType")
    marital_status: str = Field(alias="MaritalStatus")
    has_mortgage: str = Field(alias="HasMortgage")
    has_dependents: str = Field(alias="HasDependents")
    loan_purpose: str = Field(alias="LoanPurpose")
    has_cosigner: str = Field(alias="HasCoSigner")

class RiskAssessment(BaseModel):
    model: str
    default_probability: float = Field(
        description="Estimated default probability from 0.0 to 1.0."
    )
    prediction: int = Field(
        description="Model class: 1 indicates default; 0 indicates non-default."
    )
    risk_level: str
    recommendation: str
    risk_factors: List[str] = Field(
        description="Rule-based applicant risk flags; empty when none are identified."
    )


app = FastAPI(
    title="Loan Risk Assessment API",
    description=(
        "Estimate loan default risk using the trained loan model. "
        "This is screening support, not a final lending decision."
    ),
    version="1.0.0",
)


def prepare_record(values: Dict[str, Any]) -> pd.DataFrame:
    record = pd.DataFrame([values])

    for column, mapping in ENCODING_MAPS.items():
        value = record.at[0, column]
        if value not in mapping:
            choices = list(mapping.keys())
            raise HTTPException(
                status_code=422,
                detail=f"Unsupported value for {column}: {value!r}. Choose from: {choices}",
            )
        record[column] = record[column].map(mapping)

    record = pd.get_dummies(record, columns=NOMINAL_FEATURES, drop_first=True)
    return record.reindex(columns=FEATURE_COLUMNS, fill_value=0)


def risk_band(probability: float) -> Tuple[str, str]:
    if probability >= 0.70:
        return "HIGH RISK", "Immediate manual review required"
    if probability >= 0.40:
        return "MODERATE RISK", "Additional documentation needed"
    return "LOW RISK", "Continue with standard review; this score is not an approval"


def identify_risk_factors(application: LoanApplication) -> List[str]:
    risk_factors = []
    if application.credit_score < 600:
        risk_factors.append("Low credit score")
    if application.dti_ratio > 0.5:
        risk_factors.append("High debt-to-income ratio")
    if application.months_employed < 12:
        risk_factors.append("Limited employment history")
    if application.loan_amount / application.income > 3:
        risk_factors.append("High loan-to-income ratio")
    if application.has_cosigner == "No" and application.loan_amount > 100000:
        risk_factors.append("Large loan without co-signer")
    return risk_factors


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "model": DEFAULT_MODEL_NAME}


@app.post("/assess", response_model=RiskAssessment)
def assess(application: LoanApplication) -> RiskAssessment:
    record = prepare_record(application.model_dump(by_alias=True))
    model = MODELS[DEFAULT_MODEL_NAME]
    probability = float(model.predict_proba(record)[0, 1])
    prediction = int(model.predict(record)[0])
    risk_level, recommendation = risk_band(probability)

    return RiskAssessment(
        model=DEFAULT_MODEL_NAME,
        default_probability=probability,
        prediction=prediction,
        risk_level=risk_level,
        recommendation=recommendation,
        risk_factors=identify_risk_factors(application),
    )