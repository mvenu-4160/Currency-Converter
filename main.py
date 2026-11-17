exchange_rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

def convert_to_inr(amount, currency):
    return amount * exchange_rates[currency]

def convert_currency(amount, from_currency, to_currency):
    inr_amount = convert_to_inr(amount, from_currency)
    result = inr_amount / exchange_rates[to_currency]
    return result

print("===== CURRENCY CONVERTER =====")
print("Available: INR, USD, EUR, GBP")

try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency: ").strip().upper()
    to_currency = input("To currency: ").strip().upper()

    if amount < 0:
        print("Amount cannot be negative.")

    elif from_currency not in exchange_rates:
        print("Unsupported currency:", from_currency)

    elif to_currency not in exchange_rates:
        print("Unsupported currency:", to_currency)

    else:
        result = convert_currency(
            amount, from_currency, to_currency
        )
        print(f"{amount:g} {from_currency} = {result:.2f} {to_currency}")

except ValueError:
    print("Invalid amount. Enter a number.")