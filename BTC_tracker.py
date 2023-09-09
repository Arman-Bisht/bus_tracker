# Import required libraries
import requests
import time

# Declare API endpoint
endpoint = "https://api.coinbase.com/v2/prices/spot"

# List of currencies to extract bitcoin value for
currencies = ["INR", "USD", "JPY"]

while True:
    for currency in currencies:
        # Make API request to get bitcoin value for currency
        response = requests.get(f"{endpoint}?currency={currency}")
        data = response.json()
        bitcoin_value = data["data"]["amount"]

        # Display the value
        print(f"Bitcoin value in {currency}: {bitcoin_value}")

    # Wait for 30 minutes before making the next API request
    time.sleep(1800)
# """This code is a script that retrieves the current value of Bitcoin in various currencies (INR, USD, and JPY) from the Coinbase API. Here's a step by step explanation:

#1.The script starts by importing the required libraries "requests" and "time". "requests" is used to make HTTP requests to an API endpoint, and "time" is used to pause the execution of the code for a specified amount of time.

#2.The endpoint of the Coinbase API is declared with the endpoint variable. This endpoint is used to retrieve the current spot price of Bitcoin in a specified currency.

#3.A list of currencies, currencies, is declared with the values "INR", "USD", and "JPY". This list represents the currencies for which the value of Bitcoin needs to be retrieved.

#4.A while loop is then executed which will run indefinitely. Within the loop, another for loop is used to iterate over the currencies list.

#5.For each currency in the currencies list, the script makes a GET request to the Coinbase API endpoint with the currency parameter set to the current currency. The response from the API is stored in the response variable, which is then parsed as JSON and stored in the data variable.

#6.The current value of Bitcoin in the specified currency is then extracted from the data variable and stored in the bitcoin_value variable.

#7.The value of Bitcoin is then displayed in the console with a message that includes the currency symbol and its value.

#8.After the value of Bitcoin has been displayed for each currency in the currencies list, the script pauses for 30 minutes using the time.sleep() function before starting the loop again and making another API request. This process repeats indefinitely.
#  """