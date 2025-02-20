import argparse
import datetime

from SynergyDataFetcher import SynergyDataFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch and parse Synergy usage data.")
    parser.add_argument("--premise_id", type=str, help="Premise ID", required=True)
    parser.add_argument('-e', "--email_address", type=str, help="Email address", required=True)
    parser.add_argument('-p', "--password", type=str, help="Password", required=True)
    parser.add_argument('-s', "--email_server", type=str, help="Email server", required=True)
    parser.add_argument("--email_port", type=int, help="Email port", default=993)

    args = parser.parse_args()

    synergy_fetcher = SynergyDataFetcher(args.premise_id, args.email_address, args.password, args.email_server, args.email_port)
    raw_usage_data = synergy_fetcher.fetch(datetime.date.today() - datetime.timedelta(days=4), datetime.date.today())
    parsed_usage_data = synergy_fetcher.parse()
    print(parsed_usage_data)

if __name__ == "__main__":
    main()
