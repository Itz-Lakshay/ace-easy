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


def main():
    print("=== Password Strength Checker ===")
    # Password input and analysis logic will be added in later commits.


if __name__ == "__main__":
    main()