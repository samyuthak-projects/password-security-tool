import re

def check_password(password):

    length = len(password) >= 8
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"\d", password))
    special = bool(re.search(r"[!@#$%^&*]", password))

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


while True:
    pw = input("Enter a password (or 'quit'): ")

    if pw == "quit":
        break

    result = check_password(pw)
    print("Strength:", result)