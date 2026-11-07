import sys
import requests

# Check for argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Validate numeric input
try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Your CoinCap API Key
API_KEY = "YOUR_API_KEY_HERE"   # <<<<<< REPLACE THIS

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

# Request Bitcoin price safely
try:
    response = requests.get(url)
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()

# Calculate total value
total = amount * price

# Print with commas + 4 decimal places
print(f"${total:,.4f}")



