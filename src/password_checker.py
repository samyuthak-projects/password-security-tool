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

def estimate_crack_time(password):

    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*" for c in password):
        charset_size += 8

    length = len(password)

    combinations = charset_size ** length

    guesses_per_second = 1_000_000_000  # 1 billion guesses/sec

    seconds = combinations / guesses_per_second

    return seconds


def format_time(seconds):

    if seconds < 60:
        return "seconds"
    elif seconds < 3600:
        return "minutes"
    elif seconds < 86400:
        return "hours"
    elif seconds < 31536000:
        return "days"
    else:
        return "months/years"
    
    
while True:
    pw = input("Enter a password (or 'quit'): ")

    if pw == "quit":
        break

    result = check_password(pw)
    crack_time = estimate_crack_time(pw)
    readable_time = format_time(crack_time)

    print("Strength:", result)
    print("Estimated crack time:", readable_time)