from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
ARTIFACT_PATH = APP_DIR / "loan_model_artifacts.joblib"

# Reuse the fitted models and preprocessing metadata exported by the notebook.
artifacts = joblib.load(ARTIFACT_PATH)
MODELS = artifacts["models"]
RESULTS = artifacts["results"]
FEATURE_COLUMNS = artifacts["feature_columns"]
ENCODING_MAPS = artifacts["encoding_maps"]
NOMINAL_FEATURES = artifacts["nominal_features"]
DEFAULT_MODEL_NAME = artifacts["default_model_name"]

st.set_page_config(
    page_title="Loan Risk Assessment System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #767676;
        background-color: #F3F4F6;
    }

    .stApp {
        background: linear-gradient(135deg, #F3F4F6 0%, #E5E7EB 100%);
    }

    .block-container {
        background: #F3F4F6;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: #767676;
    }

    p, span, div, label, li, td, th {
        color: #767676;
    }

    [data-testid="stForm"] {
        background: #FFFFFF;
    }

    [data-testid="stMetric"] {
        background: #FFFFFF;
    }

    [data-testid="stSidebar"] {
        background: #FFFFFF;
    }

    .streamlit-expanderHeader,
    .streamlit-expanderContent {
        background: #FFFFFF;
        color: #767676;
    }

    .stAlert {
        background: #FFFFFF;
    }

    .stDataFrame {
        background: #FFFFFF;
    }

    .stJson {
        background: #FFFFFF;
        color: #767676;
    }

    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF;
        color: #767676;
    }

    .stCaption, .stHelpText {
        color: #767676;
    }

    [data-testid="stMetric"] label {
        color: #767676;
    }

    [data-testid="stMetricValue"] {
        color: #767676;
    }

    /* Standard blue action style for the two loan-form submit buttons. */
    [data-testid="stFormSubmitButton"] button,
    [data-testid="stFormSubmitButton"] button[data-testid="stBaseButton-primary"],
    [data-testid="stForm"] [data-testid="stFormSubmitButton"] button,
    [data-testid="stForm"] button[kind="primary"],
    [data-testid="stForm"] button[data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-primary"],
    button[kind="primary"],
    [data-testid="stDownloadButton"] button {
        background: #0D6EFD !important;
        background-color: #0D6EFD !important;
        color: #FFFFFF !important;
        border: 1px solid #0D6EFD !important;
        border-color: #0D6EFD !important;
        box-shadow: none !important;
    }
    [data-testid="stFormSubmitButton"] button *,
    [data-testid="stFormSubmitButton"] button svg,
    [data-testid="stForm"] [data-testid="stFormSubmitButton"] button *,
    [data-testid="stForm"] button[kind="primary"] *,
    [data-testid="stForm"] button[data-testid="stBaseButton-primary"] *,
    [data-testid="stBaseButton-primary"] *,
    button[kind="primary"] *,
    [data-testid="stDownloadButton"] button * {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
        stroke: #FFFFFF !important;
    }
    [data-testid="stFormSubmitButton"] button:hover,
    [data-testid="stForm"] [data-testid="stFormSubmitButton"] button:hover,
    [data-testid="stForm"] button[kind="primary"]:hover,
    [data-testid="stForm"] button[data-testid="stBaseButton-primary"]:hover,
    [data-testid="stBaseButton-primary"]:hover,
    button[kind="primary"]:hover,
    [data-testid="stDownloadButton"] button:hover {
        background: #0B5ED7 !important;
        background-color: #0B5ED7 !important;
        border-color: #0A58CA !important;
        color: #FFFFFF !important;
    }

    /* CSV upload Browse button follows the same primary blue style. */
    [data-testid="stFileUploaderDropzone"] button {
        background-color: #0D6EFD !important;
        color: #FFFFFF !important;
        border-color: #0D6EFD !important;
    }
    [data-testid="stFileUploaderDropzone"] button:hover {
        background-color: #0B5ED7 !important;
        border-color: #0A58CA !important;
        color: #FFFFFF !important;
    }
    [data-testid="stFileUploaderDropzone"] button *,
    [data-testid="stFileUploaderDropzone"] button svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
        stroke: #FFFFFF !important;
    }


    /* Batch results use a real horizontal scroll area when many columns are selected. */
    div[data-testid="stHorizontalBlock"]:has(.batch-header),
    div[data-testid="stHorizontalBlock"]:has(.batch-card) {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        scrollbar-width: auto;
    }
    div[data-testid="stHorizontalBlock"]:has(.batch-header) > div[data-testid="column"],
    div[data-testid="stHorizontalBlock"]:has(.batch-card) > div[data-testid="column"] {
        flex: 0 0 150px !important;
        min-width: 150px !important;
    }
    div[data-testid="stHorizontalBlock"]:has(.batch-header) > div[data-testid="column"]:first-child,
    div[data-testid="stHorizontalBlock"]:has(.batch-card) > div[data-testid="column"]:first-child {
        flex-basis: 70px !important;
        min-width: 70px !important;
    }
    div[data-testid="stHorizontalBlock"]:has(.batch-header) > div[data-testid="column"]:last-child,
    div[data-testid="stHorizontalBlock"]:has(.batch-card) > div[data-testid="column"]:last-child {
        flex-basis: 105px !important;
        min-width: 105px !important;
    }

    .batch-card {
        box-sizing: border-box;
        width: 100%;
        min-height: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 0 0.75rem;
        margin: 0;
        box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
        font-size: 0.88rem;
        line-height: 1.15;
        overflow: hidden;
        white-space: nowrap;
    }
    .batch-header {
        box-sizing: border-box;
        width: 100%;
        min-height: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        background: #111827;
        color: #FFFFFF !important;
        border-radius: 10px;
        padding: 0 0.75rem;
        margin: 0 0 0.35rem 0;
        font-size: 0.78rem;
        font-weight: 700;
        line-height: 1;
        white-space: nowrap;
    }
    /* Keep the action cell exactly the same height as every data cell. */
    .stButton button[aria-label="👁 View"] {
        height: 48px;
        min-height: 48px;
        margin: 0;
        border-radius: 10px;
        font-size: 0.84rem;
        padding: 0 0.55rem;
    }
    .batch-risk-high {
        color: #B91C1C !important;
        background: #FEF2F2;
        padding: 0.28rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        display: inline-block;
    }
    .batch-risk-medium {
        color: #B45309 !important;
        background: #FFFBEB;
        padding: 0.28rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        display: inline-block;
    }
    .batch-risk-low {
        color: #047857 !important;
        background: #ECFDF5;
        padding: 0.28rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        display: inline-block;
    }
    .batch-cell {
        box-sizing: border-box;
        min-height: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        padding: 0 0.55rem;
        border-bottom: 1px solid #E5E7EB;
        color: #374151;
        font-size: 0.82rem;
        line-height: 1.15;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }
    .batch-index {
        justify-content: center;
        font-weight: 600;
    }
    .popup-title {
        font-size: 1.45rem;
        font-weight: 700;
        margin-bottom: 0.15rem;
    }
    .popup-subtitle {
        color: #6B7280 !important;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
    .popup-section {
        background: #F8FAFC;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 0.9rem 1rem;
        margin: 0.75rem 0;
    }
    .popup-section-title {
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.65rem;
    }
    .popup-metric {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 0.7rem;
        text-align: center;
    }
    .popup-metric-label {
        font-size: 0.72rem;
        color: #6B7280 !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .popup-metric-value {
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 0.15rem;
    }

    .hover-table-wrap {
        width: 100%;
        margin-top: 0.5rem;
        overflow: visible;
    }
    .hover-hint {
        padding: 0.7rem 0.9rem; margin-bottom: 0.6rem; border-radius: 8px;
        background: #FFFFFF; border: 1px solid #D1D5DB; font-size: 0.9rem;
    }
    .hover-table { width: 100%; background: #FFFFFF; border: 1px solid #D1D5DB; border-radius: 8px; overflow: visible; }
    .hover-header, .record-hover {
        display: grid; grid-template-columns: 0.7fr 0.6fr 1fr 1fr 0.9fr 0.7fr 1fr 1fr;
        align-items: center;
    }
    .hover-header { background: #F3F4F6; font-weight: 700; border-bottom: 1px solid #D1D5DB; }
    .hover-header > div, .record-hover > div { padding: 0.7rem; white-space: nowrap; }
    .record-hover { position: relative; cursor: pointer; border-bottom: 1px solid #E5E7EB; background: #FFFFFF; }
    .record-hover:last-child { border-bottom: none; }
    .record-hover:hover { background: #F9FAFB; z-index: 100; }
    .hover-card {
        display: none; position: absolute; z-index: 999999; left: 1rem; top: calc(100% + 6px);
        width: min(720px, 80vw); max-height: 70vh; overflow-y: auto; padding: 1rem;
        background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 12px;
        box-shadow: 0 14px 35px rgba(0,0,0,0.18); text-align: left; white-space: normal; color: #374151;
    }
    .record-hover:hover .hover-card { display: block; }
    .hover-row-spacer { display: none; }
    @media (max-width: 900px) {
        .hover-table { overflow-x: auto; }
        .hover-header, .record-hover { min-width: 900px; }
        .hover-card { width: min(600px, 88vw); }
    }
    .hover-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.7rem;
        color: #374151;
    }
    .hover-risk {
        display: flex;
        flex-direction: column;
        gap: 0.2rem;
        padding: 0.65rem 0.8rem;
        background: #F9FAFB;
        border-radius: 7px;
        margin-bottom: 0.8rem;
    }
    .hover-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.55rem;
        margin-bottom: 0.8rem;
    }
    .hover-grid > div {
        padding: 0.5rem;
        background: #F8FAFC;
        border-radius: 6px;
        font-size: 0.8rem;
    }
    .hover-section {
        padding-top: 0.65rem;
        margin-top: 0.65rem;
        border-top: 1px solid #E5E7EB;
        font-size: 0.82rem;
        line-height: 1.45;
    }
    .hover-section ul {
        margin: 0.35rem 0 0 1rem;
        padding: 0;
    }
    .risk-pill {
        display: inline-block;
        padding: 0.2rem 0.45rem;
        border-radius: 999px;
        background: #F3F4F6;
        font-weight: 600;
        font-size: 0.75rem;
    }
    @media (max-width: 900px) {
        .hover-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .hover-card {
            width: min(600px, 88vw);
        }
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

def prepare_record(values):
    record = pd.DataFrame([values])

    for column, mapping in ENCODING_MAPS.items():
        record[column] = record[column].map(mapping)

    record = pd.get_dummies(
        record,
        columns=NOMINAL_FEATURES,
        drop_first=True,
    )
    return record.reindex(columns=FEATURE_COLUMNS, fill_value=0)

def risk_band(probability):
    if probability >= 0.70:
        return "HIGH RISK", "#c53030", "🔴", "Immediate manual review required"
    if probability >= 0.40:
        return "MODERATE RISK", "#c05621", "🟡", "Additional documentation needed"
    return "LOW RISK", "#2f855a", "🟢", "Standard processing approved"

# Sidebar with system information
with st.sidebar:
    st.markdown("## 🏦 Loan Risk System")
    st.markdown("---")

    st.markdown("### System Status")
    st.success("✅ All systems operational")

    st.markdown("### Model Information")
    st.info(f"**Active Model:** {DEFAULT_MODEL_NAME}")

    selected_metrics = RESULTS[DEFAULT_MODEL_NAME]
    st.metric("Model Recall", f'{selected_metrics["recall"] * 100:.1f}%')
    st.metric("Model F1-Score", f'{selected_metrics["f1"]:.3f}')
    st.metric("Model AUC-ROC", f'{selected_metrics["auc"]:.3f}')

    st.markdown("---")
    st.caption("© 2024 Bank Risk Assessment System")
    st.caption("Internal Use Only")

# Main content with tabs
tab1, tab2, tab3 = st.tabs([
    "📋 Loan Assessment",
    "📂 CSV Batch Assessment",
    "📊 Model Performance"
])

with tab1:
        st.markdown("# Loan Risk Assessment")
        st.markdown("### Evaluate loan applicant default risk")
        st.markdown("Enter applicant information below to receive an automated risk assessment.")

        with st.form("loan_form"):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### 👤 Applicant Information")
                age = st.number_input("Age", min_value=18, max_value=69, value=35, help="Applicant's age in years", format="%d")
                income = st.number_input("Annual Income ($)", min_value=15000, max_value=150000, value=82500, step=500, help="Gross annual income", format="%d")
                credit_score = st.number_input("Credit Score", min_value=300, max_value=849, value=574, help="FICO credit score", format="%d")
                months_employed = st.number_input("Months Employed", min_value=0, max_value=119, value=60, help="Total months at current job", format="%d")
                num_credit_lines = st.number_input("Number of Credit Lines", min_value=1, max_value=4, value=2, help="Total active credit accounts", format="%d")

            with col2:
                st.markdown("### 💰 Loan Details")
                loan_amount = st.number_input("Loan Amount ($)", min_value=5000, max_value=250000, value=127500, step=1000, help="Requested loan amount", format="%d")
                interest_rate = st.number_input("Interest Rate (%)", min_value=2.0, max_value=25.0, value=13.5, step=0.1, help="Annual interest rate", format="%.2f")
                loan_term = st.number_input("Loan Term (Months)", min_value=12, max_value=60, value=36, step=12, help="Loan duration in months", format="%d")
                dti_ratio = st.number_input("Debt-to-Income Ratio", min_value=0.1, max_value=0.9, value=0.5, step=0.01, help="Monthly debt payments / monthly income", format="%.2f")

            with col3:
                st.markdown("### 📋 Additional Information")
                education = st.selectbox("Education Level", list(ENCODING_MAPS["Education"].keys()))
                employment_type = st.selectbox("Employment Type", list(ENCODING_MAPS["EmploymentType"].keys()))
                marital_status = st.selectbox("Marital Status", ["Married", "Divorced", "Single"])
                loan_purpose = st.selectbox("Loan Purpose", ["Auto", "Business", "Education", "Home", "Other"])
                has_mortgage = st.selectbox("Has Existing Mortgage", ["No", "Yes"])
                has_dependents = st.selectbox("Has Dependents", ["No", "Yes"])
                has_cosigner = st.selectbox("Has Co-Signer", ["No", "Yes"])

            col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
            with col_btn2:
                submitted = st.form_submit_button("Generate Risk Assessment", type="primary", icon=":material/search:", width="stretch")
                reset_button = st.form_submit_button("Reset Form", type="primary", icon=":material/refresh:")

        # Quick test scenarios (outside form)
        st.markdown("### 🎯 Quick Test Scenarios")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🟢 Low Risk Profile", key="low_risk"):
                st.info("Low Risk Profile: High income, excellent credit, stable employment, low DTI")
                st.json({
                    "Age": 45,
                    "Income": 120000,
                    "Credit Score": 750,
                    "Months Employed": 120,
                    "Loan Amount": 50000,
                    "Interest Rate": 5.0,
                    "DTI Ratio": 0.25,
                    "Education": "Master's",
                    "Employment": "Full-time"
                })

        with col2:
            if st.button("🟡 Moderate Risk Profile", key="moderate_risk"):
                st.info("Moderate Risk Profile: Average income, fair credit, moderate DTI")
                st.json({
                    "Age": 35,
                    "Income": 82500,
                    "Credit Score": 574,
                    "Months Employed": 60,
                    "Loan Amount": 127500,
                    "Interest Rate": 13.5,
                    "DTI Ratio": 0.5,
                    "Education": "Bachelor's",
                    "Employment": "Full-time"
                })

        with col3:
            if st.button("🔴 High Risk Profile", key="high_risk"):
                st.info("High Risk Profile: Low income, poor credit, high DTI, unstable employment")
                st.json({
                    "Age": 22,
                    "Income": 25000,
                    "Credit Score": 350,
                    "Months Employed": 3,
                    "Loan Amount": 200000,
                    "Interest Rate": 22.0,
                    "DTI Ratio": 0.85,
                    "Education": "High School",
                    "Employment": "Unemployed"
                })

        if submitted:
            values = {
                "Age": age,
                "Income": income,
                "LoanAmount": loan_amount,
                "CreditScore": credit_score,
                "MonthsEmployed": months_employed,
                "NumCreditLines": num_credit_lines,
                "InterestRate": interest_rate,
                "LoanTerm": loan_term,
                "DTIRatio": dti_ratio,
                "Education": education,
                "EmploymentType": employment_type,
                "MaritalStatus": marital_status,
                "HasMortgage": has_mortgage,
                "HasDependents": has_dependents,
                "LoanPurpose": loan_purpose,
                "HasCoSigner": has_cosigner,
            }

            record = prepare_record(values)

            # Debug: Show the prepared record
            with st.expander("🔍 Debug: Model Input Data"):
                st.write("Input values:", values)
                st.write("Prepared record shape:", record.shape)
                st.write("Prepared record columns:", record.columns.tolist())
                st.write("Expected feature columns:", FEATURE_COLUMNS[:5], "... (total", len(FEATURE_COLUMNS), "features)")

            probabilities = {
                name: model.predict_proba(record)[0, 1]
                for name, model in MODELS.items()
            }

            # Debug: Show model predictions
            with st.expander("🔍 Debug: Model Predictions"):
                st.write("All model predictions:")
                for name, prob in probabilities.items():
                    st.write(f"{name}: {prob:.4f} ({prob*100:.2f}%)")

            probability = probabilities[DEFAULT_MODEL_NAME]
            label, color, emoji, recommendation = risk_band(probability)

            # Main result display
            st.markdown("---")
            st.markdown("## Risk Assessment Result")

            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(
                    f'<div class="result" style="border-color: {color};">'
                    f'<h2 style="color: #767676;">{emoji} {label}</h2>'
                    f'<p>Default Probability: <strong>{probability * 100:.1f}%</strong></p>'
                    f'<p style="margin-top: 0.5rem; font-size: 0.95rem;">{recommendation}</p></div>',
                    unsafe_allow_html=True,
                )

            with col2:
                st.metric("Confidence Level", f"{(1 - abs(probability - 0.5) * 2) * 100:.1f}%")
                st.metric("Loan-to-Income", f"{loan_amount / income:.2f}x")

            # Additional metrics
            st.markdown("### 📊 Detailed Analysis")
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Credit Score", f"{credit_score}")
            col2.metric("DTI Ratio", f"{dti_ratio:.2%}")
            col3.metric("Employment Stability", f"{months_employed / 12:.1f} years")
            col4.metric("Loan Term", f"{loan_term} months")

            # Risk factors analysis
            st.markdown("### ⚠️ Risk Factors")
            risk_factors = []

            if credit_score < 600:
                risk_factors.append("Low credit score")
            if dti_ratio > 0.5:
                risk_factors.append("High debt-to-income ratio")
            if months_employed < 12:
                risk_factors.append("Limited employment history")
            if loan_amount / income > 3:
                risk_factors.append("High loan-to-income ratio")
            if has_cosigner == "No" and loan_amount > 100000:
                risk_factors.append("Large loan without co-signer")

            if risk_factors:
                for factor in risk_factors:
                    st.warning(f"⚠️ {factor}")
            else:
                st.success("✅ No significant risk factors identified")

            # Recommendation section
            st.markdown("### 📋 Recommended Action")
            if probability >= 0.70:
                st.error("### 🚨 MANUAL REVIEW REQUIRED")
                st.markdown("**Immediate Actions:**")
                st.markdown("- Assign to senior loan officer for manual review")
                st.markdown("- Request additional financial documentation")
                st.markdown("- Verify all income and employment information")
                st.markdown("- Consider requiring collateral or co-signer")
                st.markdown("- If approved, implement enhanced monitoring")
            elif probability >= 0.40:
                st.warning("### ⚠️ ADDITIONAL VERIFICATION NEEDED")
                st.markdown("**Required Actions:**")
                st.markdown("- Verify supporting documents")
                st.markdown("- Confirm repayment capacity")
                st.markdown("- Consider partial approval with conditions")
                st.markdown("- Standard underwriting review")
            else:
                st.success("### ✅ STANDARD PROCESSING APPROVED")
                st.markdown("**Actions:**")
                st.markdown("- Proceed with standard loan processing")
                st.markdown("- Automated underwriting approved")
                st.markdown("- Standard monitoring and policy controls")
                st.markdown("- No additional documentation required")

# Clear any previously opened batch-record dialog whenever the full app reruns.
# This does NOT run during fragment-only reruns, so the dialog remains open/usable
# while interacting inside Tab 2, but cannot reappear when Tab 1 triggers a full rerun.
st.session_state["show_batch_details"] = False
st.session_state.pop("selected_batch_record", None)

# The CSV workflow is isolated in a fragment. Interactions such as
# file upload rerun only this section instead of the whole application.
@st.fragment
def render_batch_tab():
        st.markdown("# CSV Batch Loan Assessment")
        st.markdown("### Upload multiple loan applications and receive a risk assessment for each row.")
        st.info(f"**Active Model:** {DEFAULT_MODEL_NAME}. The same fitted model and preprocessing used in the first tab are applied to every CSV row.")
        required_columns = ["Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", "NumCreditLines", "InterestRate", "LoanTerm", "DTIRatio", "Education", "EmploymentType", "MaritalStatus", "HasMortgage", "HasDependents", "LoanPurpose", "HasCoSigner"]
        st.markdown("#### Required CSV columns")
        st.code(", ".join(required_columns), language="text")
        st.caption("Optional: **LoanID** is retained for record identification, table display, details, and full CSV export; it is not used by the risk model.")
        uploaded_csv = st.file_uploader(
            "Upload CSV files",
            type=["csv"],
            accept_multiple_files=True,
            key="batch_csv",
            help="Select one or more CSV files. All files must contain the required model columns."
        )
        if not uploaded_csv:
            st.session_state.pop("batch_last_upload_signature", None)
            st.session_state.pop("batch_column_visibility", None)
            st.session_state.pop("batch_column_settings_signature", None)
            st.session_state.pop("batch_select_all_columns", None)
            st.session_state.pop("batch_previous_select_all", None)
        if uploaded_csv:
            try:
                # Read and combine all selected CSV files into one batch. LoanID is retained
                # exactly as supplied and is never sent to the model.
                uploaded_files = uploaded_csv if isinstance(uploaded_csv, list) else [uploaded_csv]
                frames = []
                for uploaded_file in uploaded_files:
                    frame = pd.read_csv(uploaded_file)
                    frame["__source_csv__"] = getattr(uploaded_file, "name", "uploaded.csv")
                    frames.append(frame)
                batch_df = pd.concat(frames, ignore_index=True)
                st.success(
                    f"{len(uploaded_files)} CSV file(s) loaded successfully: {len(batch_df):,} total rows."
                )
                missing = [c for c in required_columns if c not in batch_df.columns]
                if missing:
                    st.error("The uploaded CSV is missing required columns:")
                    st.write(missing)
                else:
                    input_df = batch_df.drop(columns=["__source_csv__"], errors="ignore").copy()
                    model_df = input_df[required_columns].copy()
                    unknown = {}
                    for column, mapping in ENCODING_MAPS.items():
                        if column in model_df.columns:
                            model_df[column] = model_df[column].map(mapping)
                            bad = input_df.loc[model_df[column].isna(), column].dropna().unique().tolist()
                            if bad:
                                unknown[column] = bad
                    if unknown:
                        st.error("The CSV contains categorical values not present in the trained model:")
                        st.json(unknown)
                    else:
                        # Convert numeric inputs before reindexing. Some numeric features may
                        # have been removed by training-time feature selection, so checking
                        # them after reindexing can raise a KeyError.
                        numeric = ["Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", "NumCreditLines", "InterestRate", "LoanTerm", "DTIRatio"]
                        for c in numeric:
                            model_df[c] = pd.to_numeric(model_df[c], errors="coerce")
                        if model_df[numeric].isna().any().any():
                            st.error("Some numeric fields contain missing or non-numeric values.")
                        else:
                            model_df = pd.get_dummies(model_df, columns=NOMINAL_FEATURES, drop_first=True)
                            model_df = model_df.reindex(columns=FEATURE_COLUMNS, fill_value=0)
                            model = MODELS[DEFAULT_MODEL_NAME]
                            probabilities = model.predict_proba(model_df)[:, 1]
                            predictions = model.predict(model_df)
                            results_df = input_df.copy()
                            results_df["Default Probability"] = probabilities
                            results_df["Default Prediction"] = predictions
                            results_df["Risk Level"] = ["HIGH RISK" if p >= 0.70 else "MODERATE RISK" if p >= 0.40 else "LOW RISK" for p in probabilities]
                            st.markdown("## Risk Assessment Results")
                            c1, c2, c3 = st.columns(3)
                            c1.metric("Applications", f"{len(results_df):,}")
                            c2.metric("High Risk", f"{(results_df['Risk Level'] == 'HIGH RISK').sum():,}")
                            c3.metric("Moderate Risk", f"{(results_df['Risk Level'] == 'MODERATE RISK').sum():,}")
                            # Polished per-row assessment table with modal-style details.
                            st.markdown("### 📋 Batch Assessment Results")
                            st.caption("Review the portfolio below and open any application for its complete assessment.")

                            # Column display/order settings are kept inside a compact settings control.
                            display_options = list(results_df.columns)
                            # LoanID is an identifier only: it is never sent to the model,
                            # but it is retained from the uploaded CSV for display and full export.
                            default_display_columns = [
                                c for c in [
                                    "LoanID", "Age", "Income", "LoanAmount", "CreditScore",
                                    "DTIRatio", "Default Probability", "Risk Level"
                                ] if c in display_options
                            ]

                            # Re-apply the default column selection for every newly uploaded CSV.
                            # The upload signature includes file metadata, so removing one CSV and
                            # adding another starts cleanly with the same default columns.
                            upload_signature = tuple(
                                (
                                    getattr(uploaded_file, "name", ""),
                                    getattr(uploaded_file, "size", None),
                                    getattr(uploaded_file, "file_id", None),
                                )
                                for uploaded_file in uploaded_files
                            )
                            if st.session_state.get("batch_last_upload_signature") != upload_signature:
                                st.session_state["batch_last_upload_signature"] = upload_signature
                                st.session_state["batch_column_settings_signature"] = tuple(display_options)
                                st.session_state["batch_column_visibility"] = {
                                    column: column in default_display_columns for column in display_options
                                }
                                # Initialize the actual checkbox widget state too, so the defaults
                                # are checked on every new CSV, even if the previous CSV was customized.
                                for column in display_options:
                                    st.session_state[f"batch_column_visible_{column}"] = column in default_display_columns
                                st.session_state["batch_select_all_columns"] = False
                                st.session_state["batch_previous_select_all"] = False
                                # A new CSV gets a fresh table selection as well.
                                st.session_state.pop("batch_selected_table_row", None)
                                st.session_state.pop("selected_batch_record", None)
                                st.session_state.pop("show_batch_details", None)

                            with st.expander("⚙️ Columns", expanded=False):
                                # Compact multi-column selector with Select All.
                                all_selected = all(
                                    st.session_state["batch_column_visibility"].get(column, False)
                                    for column in display_options
                                )
                                select_all = st.checkbox(
                                    "Select all",
                                    value=all_selected,
                                    key="batch_select_all_columns",
                                )

                                # If Select All changed, apply it to every column.
                                previous_select_all = st.session_state.get("batch_previous_select_all")
                                if previous_select_all is None:
                                    st.session_state["batch_previous_select_all"] = select_all
                                elif select_all != previous_select_all:
                                    for column in display_options:
                                        st.session_state["batch_column_visibility"][column] = select_all
                                        st.session_state[f"batch_column_visible_{column}"] = select_all
                                    st.session_state["batch_previous_select_all"] = select_all

                                # Compact multi-column checkbox layout.
                                selection_cols = st.columns(4)
                                for position, column in enumerate(display_options):
                                    col = selection_cols[position % 4]
                                    visible = col.checkbox(
                                        column,
                                        key=f"batch_column_visible_{column}",
                                    )
                                    st.session_state["batch_column_visibility"][column] = visible

                            display_columns = [
                                column for column in display_options
                                if st.session_state["batch_column_visibility"].get(column, False)
                            ]

                            # Changing column visibility is a table-setting interaction, not a
                            # request to reopen the previously selected record. Clear the one-time
                            # details trigger whenever the visible-column set changes.
                            current_column_signature = tuple(display_columns)
                            previous_column_signature = st.session_state.get("batch_last_display_columns")
                            if previous_column_signature is not None and current_column_signature != previous_column_signature:
                                st.session_state.pop("selected_batch_record", None)
                                st.session_state["show_batch_details"] = False
                            st.session_state["batch_last_display_columns"] = current_column_signature

                            if not display_columns:
                                st.info("Select at least one column in ⚙️ Columns to display the batch results.")
                            else:
                                def format_batch_value(row, column):
                                    value = row[column]
                                    if pd.isna(value):
                                        return "—"
                                    if column in {"Income", "LoanAmount"}:
                                        try:
                                            return f"₹{float(value):,.0f}"
                                        except (TypeError, ValueError):
                                            return str(value)
                                    if column == "DTIRatio":
                                        try:
                                            return f"{float(value):.2%}"
                                        except (TypeError, ValueError):
                                            return str(value)
                                    if column == "Default Probability":
                                        try:
                                            return f"{float(value):.2%}"
                                        except (TypeError, ValueError):
                                            return str(value)
                                    if column == "Default Prediction":
                                        return "Default" if int(value) == 1 else "No Default"
                                    return str(value)

                                # Scrollable table-style grid with a real View button in the Action column.
                                # Native st.dataframe cannot host clickable buttons inside cells, so this
                                # keeps the table compact while giving every record its own working action.
                                # Values are formatted while each grid cell is rendered below.  Do
                                # not write formatted strings back into a typed DataFrame first:
                                # modern pandas rejects assigning values such as "45" to an int64
                                # column, which previously prevented valid CSV uploads from loading.
                                grid_height = min(620, max(260, 52 + min(len(results_df), 12) * 50))
                                # Keep every column readable instead of squeezing all columns into the
                                # viewport.  The bordered grid itself scrolls horizontally when more
                                # columns are selected.
                                grid_min_width = 170 + (len(display_columns) * 170) + 105
                                st.markdown(
                                    f"""<style>
                                    div[data-testid=\"stVerticalBlockBorderWrapper\"]:has(.batch-grid-scroll-marker) {{
                                        overflow-x: auto !important;
                                    }}
                                    .batch-grid-scroll-marker {{
                                        min-width: {grid_min_width}px;
                                        height: 1px;
                                        margin: 0;
                                        padding: 0;
                                    }}
                                    </style>""",
                                    unsafe_allow_html=True,
                                )
                                with st.container(height=grid_height, border=True):
                                    st.markdown('<div class="batch-grid-scroll-marker"></div>', unsafe_allow_html=True)
                                    # Header row. Each data column has a stable minimum width so the
                                    # grid grows horizontally instead of becoming unreadably narrow.
                                    header_widths = [0.55] + [1.70] * len(display_columns) + [0.85]
                                    header_cols = st.columns(header_widths, gap="small")
                                    with header_cols[0]:
                                        st.markdown('<div class="batch-header">#</div>', unsafe_allow_html=True)
                                    for col_idx, column in enumerate(display_columns, start=1):
                                        with header_cols[col_idx]:
                                            st.markdown(
                                                f'<div class="batch-header">{column}</div>',
                                                unsafe_allow_html=True,
                                            )
                                    with header_cols[-1]:
                                        st.markdown('<div class="batch-header">Action</div>', unsafe_allow_html=True)

                                    for row_position, (_, row) in enumerate(results_df.iterrows()):
                                        row_cols = st.columns(header_widths, gap="small")
                                        with row_cols[0]:
                                            st.markdown(
                                                f'<div class="batch-cell batch-index">{row_position + 1}</div>',
                                                unsafe_allow_html=True,
                                            )

                                        for col_idx, column in enumerate(display_columns, start=1):
                                            value = format_batch_value(row, column)
                                            if column == "Risk Level":
                                                risk_value = str(value).upper()
                                                if "HIGH RISK" in risk_value:
                                                    value_html = f'<span class="batch-risk-high">{value}</span>'
                                                elif "MODERATE RISK" in risk_value:
                                                    value_html = f'<span class="batch-risk-medium">{value}</span>'
                                                elif "LOW RISK" in risk_value:
                                                    value_html = f'<span class="batch-risk-low">{value}</span>'
                                                else:
                                                    value_html = str(value)
                                            else:
                                                value_html = str(value)
                                            with row_cols[col_idx]:
                                                st.markdown(
                                                    f'<div class="batch-cell">{value_html}</div>',
                                                    unsafe_allow_html=True,
                                                )

                                        with row_cols[-1]:
                                            if st.button(
                                                "👁 View",
                                                key=f"batch_view_row_{row_position}",
                                                width="stretch",
                                                help=f"View full assessment for record {row_position + 1}",
                                            ):
                                                st.session_state["selected_batch_record"] = row_position
                                                st.session_state["show_batch_details"] = True
                                                st.rerun(scope="fragment")

                            selected_idx = st.session_state.get("selected_batch_record")
                            if st.session_state.get("show_batch_details", False) and selected_idx is not None:
                                selected_row = results_df.iloc[selected_idx]

                                @st.dialog(f"Loan Assessment · Record {selected_idx + 1}", width="large")
                                def show_batch_record_details(row, record_number):
                                    probability = float(row["Default Probability"])
                                    label, risk_color, risk_icon, action_title = risk_band(probability)

                                    st.markdown(
                                        f'<div class="popup-title">{risk_icon} Record {record_number} — Loan Assessment</div>'
                                        f'<div class="popup-subtitle">Detailed assessment using the same model and preprocessing as the individual assessment.</div>',
                                        unsafe_allow_html=True
                                    )

                                    metric_cols = st.columns(3)
                                    metric_data = [
                                        ("Default Probability", f"{probability:.2%}"),
                                        ("Prediction", "Default" if int(row["Default Prediction"]) == 1 else "No Default"),
                                        ("Risk Level", f"{risk_icon} {label}"),
                                    ]
                                    for col, (metric_label, metric_value) in zip(metric_cols, metric_data):
                                        with col:
                                            st.markdown(
                                                f'<div class="popup-metric">'
                                                f'<div class="popup-metric-label">{metric_label}</div>'
                                                f'<div class="popup-metric-value">{metric_value}</div>'
                                                f'</div>',
                                                unsafe_allow_html=True
                                            )

                                    st.markdown(
                                        '<div class="popup-section"><div class="popup-section-title">👤 Applicant & Loan Details</div>',
                                        unsafe_allow_html=True
                                    )

                                    detail_data = [
                                        ("Age", row["Age"]),
                                        ("Income", f"₹{float(row['Income']):,.0f}"),
                                        ("Loan Amount", f"₹{float(row['LoanAmount']):,.0f}"),
                                        ("Credit Score", row["CreditScore"]),
                                        ("Months Employed", row["MonthsEmployed"]),
                                        ("Credit Lines", row["NumCreditLines"]),
                                        ("Interest Rate", row["InterestRate"]),
                                        ("Loan Term", row["LoanTerm"]),
                                        ("DTI Ratio", f"{float(row['DTIRatio']):.2%}"),
                                        ("Education", row["Education"]),
                                        ("Employment", row["EmploymentType"]),
                                        ("Marital Status", row["MaritalStatus"]),
                                        ("Mortgage", row["HasMortgage"]),
                                        ("Dependents", row["HasDependents"]),
                                        ("Loan Purpose", row["LoanPurpose"]),
                                        ("Co-signer", row["HasCoSigner"]),
                                    ]

                                    detail_cols = st.columns(4)
                                    for i, (name, value) in enumerate(detail_data):
                                        with detail_cols[i % 4]:
                                            st.markdown(f"**{name}**")
                                            st.caption(str(value))

                                    st.markdown("</div>", unsafe_allow_html=True)

                                    factors = []
                                    if float(row["CreditScore"]) < 600:
                                        factors.append("Low credit score")
                                    if float(row["DTIRatio"]) > 0.5:
                                        factors.append("High debt-to-income ratio")
                                    if float(row["MonthsEmployed"]) < 12:
                                        factors.append("Limited employment history")
                                    if float(row["LoanAmount"]) / max(float(row["Income"]), 1) > 3:
                                        factors.append("High loan-to-income ratio")
                                    if str(row["HasCoSigner"]) == "No" and float(row["LoanAmount"]) > 100000:
                                        factors.append("Large loan without co-signer")

                                    st.markdown(
                                        '<div class="popup-section"><div class="popup-section-title">⚠️ Risk Factors</div>',
                                        unsafe_allow_html=True
                                    )
                                    if factors:
                                        for factor in factors:
                                            st.markdown(f"• {factor}")
                                    else:
                                        st.success("No major rule-based risk factors identified.")
                                    st.markdown("</div>", unsafe_allow_html=True)

                                    st.markdown(
                                        '<div class="popup-section"><div class="popup-section-title">📋 Recommended Action</div>',
                                        unsafe_allow_html=True
                                    )
                                    if probability >= 0.70:
                                        st.error("**MANUAL REVIEW REQUIRED**")
                                        st.markdown(
                                            "- Assign to senior loan officer for manual review\n"
                                            "- Request additional financial documentation\n"
                                            "- Verify income and employment information\n"
                                            "- Consider collateral or a co-signer\n"
                                            "- Apply enhanced monitoring if approved"
                                        )
                                    elif probability >= 0.40:
                                        st.warning("**ADDITIONAL VERIFICATION NEEDED**")
                                        st.markdown(
                                            "- Verify supporting documents\n"
                                            "- Confirm repayment capacity\n"
                                            "- Consider approval with conditions\n"
                                            "- Complete standard underwriting review"
                                        )
                                    else:
                                        st.success("**STANDARD PROCESSING APPROVED**")
                                        st.markdown(
                                            "- Proceed with standard loan processing\n"
                                            "- Automated underwriting approved\n"
                                            "- Apply standard monitoring and policy controls\n"
                                            "- No additional documentation required"
                                        )
                                    st.markdown("</div>", unsafe_allow_html=True)

                                show_batch_record_details(selected_row, selected_idx + 1)

                            # Export options
                            st.markdown("### 📤 Export Results")
                            export_col1, export_col2 = st.columns(2)
                            csv_output = results_df.to_csv(index=False).encode("utf-8")
                            compact_results = results_df[[
                                "Default Probability",
                                "Default Prediction",
                                "Risk Level"
                            ]].copy()
                            compact_output = compact_results.to_csv(index=False).encode("utf-8")
                            with export_col1:
                                st.download_button(
                                    "⇩  Export Full Results",
                                    data=csv_output,
                                    file_name="loan_risk_assessment_full_results.csv",
                                    mime="text/csv",
                                    key="download_full_results",
                                    type="primary"
                                )
            except Exception as exc:
                st.error(f"Unable to process the CSV: {exc}")
        st.markdown("---")

with tab2:
    render_batch_tab()

with tab3:
        st.markdown("# Model Performance Dashboard")
        st.markdown("### Technical metrics and model comparison")
        st.markdown("## 📈 Model Performance Metrics")
        comparison_df = pd.DataFrame(RESULTS).T.rename_axis("Model")
        comparison_df.columns = [col.capitalize() for col in comparison_df.columns]
        for col in comparison_df.columns:
            if comparison_df[col].dtype == 'float64':
                comparison_df[col] = comparison_df[col].apply(lambda x: f"{x:.4f}")
        st.dataframe(comparison_df, width='stretch')
        st.markdown("## 🎯 Model Selection Criteria")
        st.markdown("""
        - **Recall**: Ability to correctly identify default cases (minimize false negatives)
        - **F1-Score**: Balanced measure of precision and recall
        - **AUC-ROC**: Model's ability to distinguish between classes
        - **Accuracy**: Overall correctness of predictions
        """)
        st.markdown("## 📊 Current Model Details")
        st.info(f"**Selected Model:** {DEFAULT_MODEL_NAME}")
        selected_metrics = RESULTS[DEFAULT_MODEL_NAME]
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{selected_metrics['accuracy']:.4f}")
        col2.metric("Precision", f"{selected_metrics['precision']:.4f}")
        col3.metric("Recall", f"{selected_metrics['recall']:.4f}")
        col4.metric("F1-Score", f"{selected_metrics['f1']:.4f}")
        st.markdown("## 🔧 Feature Information")
        st.markdown(f"**Total Features Used:** {len(FEATURE_COLUMNS)}")
        st.markdown(f"**Encoding Maps:** {len(ENCODING_MAPS)} categorical variables")
        st.markdown(f"**Nominal Features:** {len(NOMINAL_FEATURES)} one-hot encoded")
        with st.expander("View Feature Columns"):
            st.write(FEATURE_COLUMNS)
        with st.expander("View Encoding Maps"):
            st.write(ENCODING_MAPS)
