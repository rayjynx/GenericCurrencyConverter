import requests

# Function to get currency codes from json and store them into a tuple for user input validation
# Also error handling for any exceptions while fetching from API
def get_currency_codes():
    # Using USD as a base currency to fetch the list of all available currencies
    url = 'https://v6.exchangerate-api.com/v6/ff9ccceb156448eaf84a4717/latest/USD'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Get all currency codes (keys) from the conversion_rates dictionary
        currency_codes = tuple(data['conversion_rates'].keys())
        return currency_codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function for getting exchange rate, code almost same as get_currency_codes()
def get_exchange_rate(from_currency, to_currency):
    url = f'https://v6.exchangerate-api.com/v6/ff9ccceb156448eaf84a4717/latest/{from_currency}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['conversion_rates'].get(to_currency)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Error handling for value of currency to convert
def get_amount():
    while True:
        try:
            input_amount_prompt = float(input("Enter amount to convert: "))
            return input_amount_prompt
        except ValueError:
            print("ERROR: Invalid input. Please enter a numeric value.")

# Main function
def main():

    # Calling get_currency_codes() and storing the tuple to currency_codes
    currency_codes = get_currency_codes()

    # If currency codes cant be fetched
    if currency_codes is None:
        print("Failed to fetch the list of currency codes. Exiting...")
        return

    # Calling get_amount() and storing the received value to input_amount
    input_amount = get_amount()

    from_currency = input("Enter currency to convert from: ").upper()
    # Error handling
    while from_currency not in currency_codes:
        print(f"ERROR: Invalid currency code: {from_currency}")
        from_currency = input("Please enter a valid currency code to convert from: ").upper()

    to_currency = input("Enter currency to convert to: ").upper()
    # Error handling
    while to_currency not in currency_codes:
        print(f"ERROR: Invalid currency code: {to_currency}")
        to_currency = input("Please enter a valid currency code to convert to: ").upper()

    # Calculating exchange rate based on inputs from from_currency and to_currency and storing them to var
    exchange_rate = get_exchange_rate(from_currency, to_currency)

    # Error handling
    if exchange_rate:
        converted_amount = input_amount * exchange_rate
        print(f"{input_amount} {from_currency} is equal to: {converted_amount:.2f} {to_currency}")
    else:
        print("ERROR: Failed to fetch exchange rate. Please try again later.")


if __name__ == '__main__':
    main()
