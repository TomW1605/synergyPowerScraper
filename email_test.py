import re
import time

import requests
import imaplib
import email
from email.header import decode_header

import sys


# Function to send a login email token
def send_email_token(premise_id, email_address):
    print("Sending email token")
    login_url = "https://selfserve.synergy.net.au/apps/rest/emailLogin/getEmailToken"
    login_payload = {'emailAddress': email_address, 'premiseId': premise_id}
    login_response = requests.post(login_url, data=login_payload)
    return login_response


# Function to get the email token
def get_email_token(email_address, password, email_server, email_port, timeout=180):
    print("Get email token")
    start_time = time.time()  # Record the start time
    while time.time() - start_time < timeout:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(email_server, email_port)
        mail.login(email_address, password)
        mail.select("inbox")
        # Check if the timeout has occurred
        if time.time() - start_time > timeout:
            print("Timeout occurred. No email token received.")
            break

        # Search for emails with a specific subject
        status, messages = mail.search(None, '(UNSEEN SUBJECT "Your Synergy One-time Passcode")') #UNSEEN

        if messages[0]:
            # Get the latest email ID
            latest_email_id = messages[0].split()[-1]

            # Fetch the email content
            _, msg_data = mail.fetch(latest_email_id, '(RFC822)')
            raw_email = msg_data[0][1]

            # Decode the email content
            msg = email.message_from_bytes(raw_email)

            email_token = None

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8")
                        # print(body)

                        # Extract a 6-digit email token using regular expression
                        match = re.search(r'>(\d{6})<', body)
                        if match:
                            email_token = match.group(1)
                            # print(f"Email Token: {email_token}")
            else:
                body = msg.get_payload(decode=True).decode("utf-8")
                # print(body)

                # Extract a 6-digit email token using regular expression
                match = re.search(r'>(\d{6})<', body)
                if match:
                    email_token = match.group()
                    # print(f"Email Token: {email_token}")

            # Print the extracted email token
            if email_token:
                print(f"Email Token: {email_token}")
                mail.logout()
                return email_token
            else:
                print("No email token found.")
        else:
            print("No unread emails with email token. Waiting for new emails...")
            time.sleep(10)  # Adjust the interval as needed

    print("Timeout reached. No email token received within the specified duration.")
    mail.logout()
    return None


# Function to login with email token
def login_with_email_token(email_token):
    print("Login with email token")
    login_url = "https://selfserve.synergy.net.au/apps/rest/emailLogin/loginWithEmailToken"
    login_payload = {'emailToken': email_token}
    login_response = requests.post(login_url, json=login_payload)
    return login_response


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python script.py <premise_id> <email_address> <password> <email_server> <email_port>")
        sys.exit(1)

    premise_id = sys.argv[1]
    email_address = sys.argv[2]
    password = sys.argv[3]
    email_server = sys.argv[4]
    email_port = int(sys.argv[5])

    # Perform type and existence checks
    if not premise_id or not isinstance(premise_id, str):
        print("Error: premise_id must be a non-empty string.")
        sys.exit(1)

    if not email_address or not isinstance(email_address, str):
        print("Error: email_address must be a non-empty string.")
        sys.exit(1)

    if not password or not isinstance(password, str):
        print("Error: password must be a non-empty string.")
        sys.exit(1)

    if not email_server or not isinstance(email_server, str):
        print("Error: email_server must be a non-empty string.")
        sys.exit(1)

    if len(sys.argv) >= 7:
        if not email_port:
            print("Error: email_port must be a non-empty integer.")
            sys.exit(1)

    login_email_response = send_email_token(premise_id, email_address)
    if login_email_response.status_code == 200:
        email_token = get_email_token(email_address, password, email_server, email_port)
        if email_token:
            login_response = login_with_email_token(email_token)
            if login_response.status_code == 200:
                print("Login successful!")
            else:
                print("Failed to login with email token.")
    else:
        print("Web server response did not meet expected conditions.")
