"""Gmail API client wrapper."""

import json
import os
import sys
from typing import Any, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .config import CREDENTIALS_FILE, GMAIL_SCOPES, TOKEN_FILE


class GmailClient:
    """Wrapper for Gmail API interactions."""

    def __init__(self):
        """Initialize the Gmail client."""
        self.service = None
        self.creds = None

    def authenticate(self) -> bool:
        """
        Authenticate with Gmail API.

        Returns:
            bool: True if authentication successful, False otherwise.
        """
        try:
            # Load existing token if available
            if TOKEN_FILE.exists():
                self.creds = Credentials.from_authorized_user_file(TOKEN_FILE, GMAIL_SCOPES)

            # Refresh token if expired
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            elif not self.creds or not self.creds.valid:
                # Need to get new credentials
                if not CREDENTIALS_FILE.exists():
                    return False

                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, GMAIL_SCOPES)
                self.creds = flow.run_local_server(port=0)

                # Save token for future use
                with open(TOKEN_FILE, "w") as token:
                    token.write(self.creds.to_json())

            # Build the service
            self.service = build("gmail", "v1", credentials=self.creds)
            return True
        except Exception as e:
            print(f"Authentication error: {e}", file=sys.stderr)
            return False

    def list_messages(self, query: str = "", max_results: int = 10) -> list[dict[str, Any]]:
        """
        List messages matching the query.

        Args:
            query: Gmail search query
            max_results: Maximum number of messages to return

        Returns:
            List of message objects with id and snippet
        """
        try:
            results = self.service.users().messages().list(userId="me", q=query, maxResults=max_results).execute()
            messages = results.get("messages", [])
            return messages
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return []

    def get_message(self, message_id: str) -> Optional[dict[str, Any]]:
        """
        Get full message details.

        Args:
            message_id: ID of the message to retrieve

        Returns:
            Message object with all details or None if error
        """
        try:
            message = self.service.users().messages().get(userId="me", id=message_id, format="full").execute()
            return message
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return None

    def send_message(self, to: str, subject: str, body: str) -> Optional[str]:
        """
        Send an email message.

        Args:
            to: Recipient email address
            subject: Email subject
            body: Email body (plain text or HTML)

        Returns:
            Message ID if successful, None otherwise
        """
        try:
            import base64

            from email.mime.text import MIMEText

            message = MIMEText(body, "html")
            message["to"] = to
            message["subject"] = subject

            raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = {"raw": raw}

            result = self.service.users().messages().send(userId="me", body=send_message).execute()
            return result.get("id")
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return None

    def get_label_list(self) -> list[dict[str, Any]]:
        """
        Get all labels.

        Returns:
            List of label objects
        """
        try:
            results = self.service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])
            return labels
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return []

    def mark_as_read(self, message_id: str) -> bool:
        """
        Mark message as read.

        Args:
            message_id: ID of the message to mark as read

        Returns:
            True if successful, False otherwise
        """
        try:
            self.service.users().messages().modify(
                userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]}
            ).execute()
            return True
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return False

    def delete_message(self, message_id: str) -> bool:
        """
        Delete a message.

        Args:
            message_id: ID of the message to delete

        Returns:
            True if successful, False otherwise
        """
        try:
            self.service.users().messages().delete(userId="me", id=message_id).execute()
            return True
        except HttpError as error:
            print(f"An error occurred: {error}", file=sys.stderr)
            return False
