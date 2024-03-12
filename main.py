import datetime
import sys

from SynergyDataFetcher import SynergyDataFetcher

if len(sys.argv) < 6:
    print("Usage: python script.py <premise_id> <email_address> <password> <email_server> <email_port>")
    sys.exit(1)

premise_id = sys.argv[1]
email_address = sys.argv[2]
password = sys.argv[3]
email_server = sys.argv[4]

try:
    email_port = int(sys.argv[5])
except ValueError:
    print("Error: email_port must be a non-empty integer.")
    sys.exit(1)

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

if not email_port or not isinstance(email_port, int):
    print("Error: email_port must be a non-empty integer.")
    sys.exit(1)

# from test_data import usage_data
synergy_fetcher = SynergyDataFetcher(premise_id, email_address, password, email_server, email_port) #, usage_data)
raw_usage_data = synergy_fetcher.fetch(datetime.date.today() - datetime.timedelta(days=4), datetime.date.today())
parsed_usage_data = synergy_fetcher.parse()
print(parsed_usage_data)
