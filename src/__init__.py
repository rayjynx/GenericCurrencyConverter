import requests

def get_exchange_rate (from_currency, to_currency):
    # formatting, replacing USD with user input of 'from_currency'
    url = f'https://v6.exchangerate-api.com/v6/ff9ccceb156448eaf84a4717/latest/{from_currency}'

    # error handling
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['conversion_rates'][to_currency]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    input_amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter currency to convert from: ").upper()
    to_currency = input("Enter currency to convert to: ").upper()

    exchange_rate = get_exchange_rate(from_currency, to_currency)

    if exchange_rate:
        converted_amount = input_amount * exchange_rate
        print(f"{input_amount} {from_currency} is equal to: {converted_amount:.2f} {to_currency}")
    else:
        print("Failed to fetch exchange rate. Please try again later.")

if __name__ == '__main__':
    main()

