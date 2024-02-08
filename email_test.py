import re
import time
import datetime

import requests
import imaplib
import email
from email.header import decode_header

import sys

start_date = (datetime.date.today() - datetime.timedelta(days=2))
start_time = datetime.datetime.combine(start_date, datetime.datetime.min.time())
end_date = datetime.date.today()

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
def login_with_email_token(email_token, allow_contract):
    print("Login with email token")
    login_url = "https://selfserve.synergy.net.au/apps/rest/emailLogin/loginWithEmailToken"
    login_payload = {'emailToken': email_token}
    login_response = requests.post(login_url, json=login_payload, headers={'Content-Type': 'application/json', 'Allow-Contract': allow_contract})
    return login_response


# Function to get contract account number
def get_contract_account_number(cookies):
    print("Getting contract account number")
    index_json_url = "https://selfserve.synergy.net.au/apps/rest/account/index.json"
    index_json_response = requests.get(index_json_url, cookies=cookies)
    if index_json_response.status_code == 200:
        json_data = index_json_response.json()
        contract_account_number = json_data[0]['contractAccountNumber']
        if contract_account_number:
            print(f"Contract Account Number: {contract_account_number}")
            return contract_account_number
        else:
            raise Exception("Contract Account Number not found in response JSON.")
    else:
        raise Exception(f"Failed to retrieve contract account number. Status code: {index_json_response.status_code}")


# Function to get device ID
def get_device_id(contract_account_number, cookies):
    print("Getting device ID")
    account_json_url = f"https://selfserve.synergy.net.au/apps/rest/account/{contract_account_number}/show.json"
    account_json_response = requests.get(account_json_url, cookies=cookies)
    if account_json_response.status_code == 200:
        json_data = account_json_response.json()
        device_id = json_data['installationDetails']['intervalDevices'][0]['deviceId']
        if device_id:
            print(f"Device ID: {device_id}")
            return device_id
        else:
            raise Exception("Device ID not found in response JSON.")
    else:
        raise Exception(f"Failed to retrieve device ID. Status code: {account_json_response.status_code}")


# Function to get usage data
def get_usage_data(contract_account_number, device_id, start_date, end_date, cookies):
    print("Getting usage data")
    usage_json_url = f"https://selfserve.synergy.net.au/apps/rest/intervalData/{contract_account_number}/getHalfHourlyElecIntervalData?intervalDeviceIds={device_id}&startDate={
        start_date.strftime("%Y-%m-%d")}&endDate={end_date.strftime("%Y-%m-%d")}"
    usage_json_response = requests.get(usage_json_url, cookies=cookies)
    if usage_json_response.status_code == 200:
        json_data = usage_json_response.json()
        if json_data:
            print(f"Usage Data: {json_data}")
            return json_data
        else:
            raise Exception("Device ID not found in response JSON.")
    else:
        raise Exception(f"Failed to retrieve usage data. Status code: {usage_json_response.status_code}")


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
            login_response = login_with_email_token(email_token, login_email_response.headers.get("Allow-Contract"))
            if login_response.status_code == 200:
                # print("Login successful!")
                cookies = login_response.cookies
                contract_account_number = get_contract_account_number(cookies)
                if contract_account_number:
                    device_id = get_device_id(contract_account_number, cookies)
                    if device_id:
                        usage_data = get_usage_data(contract_account_number, device_id, start_date, end_date, cookies)
                        print(usage_data)
                        print(usage_data)
            else:
                raise Exception("Failed to login with email token.")
    elif login_email_response.status_code == 400 and "you have had too many attempts" in login_email_response.text:
        print("Too many attempts, try again tomorrow.")
    else:
        raise Exception("Web server response did not meet expected conditions.")
