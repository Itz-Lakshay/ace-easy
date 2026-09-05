"""
Password Strength Checker
--------------------------
Checks a user-entered password against common strength requirements
and gives it an overall rating: WEAK, MEDIUM, or STRONG.

Requirements checked:
    1. Minimum length (8+ characters)
    2. Contains an uppercase letter
    3. Contains a lowercase letter
    4. Contains a number
    5. Contains a special character

Note: The password is never printed, logged, or written to a file.
It is only held in memory long enough to run the checks.
"""

MIN_LENGTH = 8
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"


def check_length(password):
    """Return True if password meets the minimum length requirement."""
    return len(password) >= MIN_LENGTH


def check_uppercase(password):
    """Return True if password contains at least one uppercase letter."""
    for char in password:
        if char.isupper():
            return True
    return False


def check_lowercase(password):
    """Return True if password contains at least one lowercase letter."""
    for char in password:
        if char.islower():
            return True
    return False


def check_number(password):
    """Return True if password contains at least one digit."""
    for char in password:
        if char.isdigit():
            return True
    return False


def check_special_character(password):
    """Return True if password contains at least one special character."""
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False


def analyze_password(password):
    """
    Run all checks on the password and return a dictionary mapping
    each requirement's description to True/False.
    """
    results = {
        "At least 8 characters": check_length(password),
        "Contains uppercase letter": check_uppercase(password),
        "Contains lowercase letter": check_lowercase(password),
        "Contains a number": check_number(password),
        "Contains special character": check_special_character(password),
    }
    return results


def get_strength_rating(results):
    """
    Count how many requirements were satisfied and map that count
    to a strength label: WEAK, MEDIUM, or STRONG.
    Returns a tuple of (label, score).
    """
    score = 0
    for passed in results.values():
        if passed:
            score += 1

    if score <= 2:
        label = "WEAK"
    elif score <= 4:
        label = "MEDIUM"
    else:
        label = "STRONG"

    return label, score


def display_results(results, label, score):
    """Print the checklist and overall rating to the console."""
    print("\nPassword Analysis")
    print("-" * 40)

    for requirement, passed in results.items():
        mark = "PASS" if passed else "FAIL"
        print(f"  [{mark}] {requirement}")

    print("-" * 40)
    print(f"Requirements satisfied: {score}/5")
    print(f"Strength: {label}")
    print("-" * 40)


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    results = analyze_password(password)
    label, score = get_strength_rating(results)

    # Drop the reference to the raw password now that we're done with
    # it — nothing from here on needs or touches the actual password.
    del password

    display_results(results, label, score)


if __name__ == "__main__":
    main()