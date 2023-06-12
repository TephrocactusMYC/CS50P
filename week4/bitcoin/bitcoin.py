import sys
import requests

COINDESK_API = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    """Let the user ask the price of Bitcoin using sys.argv"""
    bitcoin_amount = parse_input()
    cost = get_cost(bitcoin_amount)
    print(f"${cost:,.4f}")

def parse_input():
    """Check that the user provides the correct command-line argument to the program"""
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    return bitcoin_amount

def get_cost(bitcoin_amount):
    """Queries the CoinDesk API for the current exchange rate of Bitcoin and calculates the cost of the specified amount"""
    try:
        response = requests.get(COINDESK_API)
        data = response.json()
        rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        cost = bitcoin_amount * rate
    except requests.RequestException:
        print("Error connecting to the API. Please try again later.")
        sys.exit(1)
    except KeyError:
        print("Unexpected response from API. Please try again later.")
        sys.exit(1)
    return cost

if __name__ == "__main__":
    main()
