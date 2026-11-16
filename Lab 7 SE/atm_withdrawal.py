
import re

def notes_needed(amount):
    if not isinstance(amount, str):
        return None
    amount = amount.strip()
    if not re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)", amount):
        return None
    return int(amount.replace(',', '')) // 100


def mask_card(card_number):
    if not isinstance(card_number, str):
        return "Invalid card number"
    digits = card_number.replace(" ", "")
    if not re.fullmatch(r"[0-9]{16}", digits):
        return "Invalid card number"
    return "XXXX XXXX XXXX " + digits[-4:]


def average_withdrawal(amounts_csv):
    if not isinstance(amounts_csv, str):
        return None
    parts = amounts_csv.split(',')
    if not parts or any(not p.strip().isdecimal() for p in parts):
        return None
    amounts = [int(p.strip()) for p in parts]
    return sum(amounts) // len(amounts)


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result)


if __name__ == "__main__":
    main()
