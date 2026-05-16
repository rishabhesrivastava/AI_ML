"""Gmail MCP Server implementation."""

import sys
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from .config import CREDENTIALS_FILE
from .gmail_client import GmailClient

# Initialize FastMCP server (stdout is reserved for MCP JSON-RPC; never print there)
mcp = FastMCP("Gmail MCP Server")

# Global Gmail client instance
gmail_client: Optional[GmailClient] = None


def get_gmail_client() -> GmailClient:
    """Get or create Gmail client instance."""
    global gmail_client
    if gmail_client is None:
        gmail_client = GmailClient()
        if not gmail_client.authenticate():
            raise RuntimeError(
                "Failed to authenticate with Gmail API. "
                f"Please ensure credentials.json exists at {CREDENTIALS_FILE}"
            )
    return gmail_client


@mcp.tool()
def list_emails(query: str = "", max_results: int = 10) -> dict[str, Any]:
    """
    List emails from your Gmail inbox.

    Args:
        query: Gmail search query (e.g., "from:user@example.com", "has:attachment")
        max_results: Maximum number of emails to return (default: 10)

    Returns:
        Dictionary containing list of emails with preview information
    """
    try:
        client = get_gmail_client()
        messages = client.list_messages(query=query, max_results=max_results)

        emails = []
        for msg in messages:
            message_detail = client.get_message(msg["id"])
            if message_detail:
                headers = message_detail["payload"]["headers"]
                email_info = {
                    "id": msg["id"],
                    "snippet": message_detail.get("snippet", ""),
                    "from": next((h["value"] for h in headers if h["name"] == "From"), "Unknown"),
                    "subject": next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)"),
                }
                emails.append(email_info)

        return {"success": True, "emails": emails, "count": len(emails)}
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_email_details(message_id: str) -> dict[str, Any]:
    """
    Get detailed information about a specific email.

    Args:
        message_id: The Gmail message ID

    Returns:
        Dictionary containing full email details including subject, sender, and body
    """
    try:
        client = get_gmail_client()
        message = client.get_message(message_id)

        if not message:
            return {"success": False, "error": "Message not found"}

        headers = message["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
        to = next((h["value"] for h in headers if h["name"] == "To"), "Unknown")
        date = next((h["value"] for h in headers if h["name"] == "Date"), "Unknown")

        # Extract body (simplified - doesn't handle all MIME types)
        body = ""
        if "parts" in message["payload"]:
            for part in message["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    data = part.get("body", {}).get("data", "")
                    if data:
                        import base64

                        body = base64.urlsafe_b64decode(data).decode("utf-8")
                        break
        else:
            data = message["payload"].get("body", {}).get("data", "")
            if data:
                import base64

                body = base64.urlsafe_b64decode(data).decode("utf-8")

        return {
            "success": True,
            "email": {
                "id": message_id,
                "subject": subject,
                "from": sender,
                "to": to,
                "date": date,
                "body": body,
                "snippet": message.get("snippet", ""),
            },
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def send_email(to: str, subject: str, body: str) -> dict[str, Any]:
    """
    Send an email message.

    Args:
        to: Recipient email address
        subject: Email subject line
        body: Email body (can be HTML)

    Returns:
        Dictionary indicating success or failure with message ID if successful
    """
    try:
        client = get_gmail_client()
        message_id = client.send_message(to, subject, body)

        if message_id:
            return {"success": True, "message_id": message_id, "message": "Email sent successfully"}
        else:
            return {"success": False, "error": "Failed to send email"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def mark_email_as_read(message_id: str) -> dict[str, Any]:
    """
    Mark an email as read.

    Args:
        message_id: The Gmail message ID

    Returns:
        Dictionary indicating success or failure
    """
    try:
        client = get_gmail_client()
        success = client.mark_as_read(message_id)

        if success:
            return {"success": True, "message": "Email marked as read"}
        else:
            return {"success": False, "error": "Failed to mark email as read"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def delete_email(message_id: str) -> dict[str, Any]:
    """
    Delete an email message.

    Args:
        message_id: The Gmail message ID to delete

    Returns:
        Dictionary indicating success or failure
    """
    try:
        client = get_gmail_client()
        success = client.delete_message(message_id)

        if success:
            return {"success": True, "message": "Email deleted successfully"}
        else:
            return {"success": False, "error": "Failed to delete email"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def search_emails(query: str, max_results: int = 20) -> dict[str, Any]:
    """
    Search for emails using Gmail search syntax.

    Args:
        query: Gmail search query (e.g., "filename:pdf", "is:starred", "after:2024/01/01")
        max_results: Maximum number of results to return

    Returns:
        Dictionary containing list of emails matching the search query
    """
    try:
        client = get_gmail_client()
        messages = client.list_messages(query=query, max_results=max_results)

        emails = []
        for msg in messages:
            message_detail = client.get_message(msg["id"])
            if message_detail:
                headers = message_detail["payload"]["headers"]
                email_info = {
                    "id": msg["id"],
                    "snippet": message_detail.get("snippet", ""),
                    "from": next((h["value"] for h in headers if h["name"] == "From"), "Unknown"),
                    "subject": next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)"),
                }
                emails.append(email_info)

        return {"success": True, "query": query, "emails": emails, "count": len(emails)}
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_labels() -> dict[str, Any]:
    """
    Get all Gmail labels.

    Returns:
        Dictionary containing list of all labels in your Gmail account
    """
    try:
        client = get_gmail_client()
        labels = client.get_label_list()

        label_list = [{"id": label["id"], "name": label["name"]} for label in labels]

        return {"success": True, "labels": label_list, "count": len(label_list)}
    except Exception as e:
        return {"success": False, "error": str(e)}


def main():
    """Main entry point for the Gmail MCP Server."""
    try:
        # Verify credentials file exists
        if not CREDENTIALS_FILE.exists():
            print(
                f"Error: credentials.json not found at {CREDENTIALS_FILE}",
                file=sys.stderr,
            )
            print(
                "Please download it from Google Cloud Console and place it in the project root.",
                file=sys.stderr,
            )
            sys.exit(1)

        # Run the server
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
