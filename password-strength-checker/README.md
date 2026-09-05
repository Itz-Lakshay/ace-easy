# Password Strength Checker

## Scenario

A small command-line program that checks whether a password is weak or
strong, based on five common security requirements.

## Requirements Checked

The program asks the user to enter a password and checks whether it:

1. Has a minimum length (8+ characters)
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a number
5. Contains a special character

It then displays which requirements were satisfied and gives an overall
strength rating: **WEAK**, **MEDIUM**, or **STRONG**, based on how many
of the five requirements were met:

| Requirements satisfied | Rating |
|-------------------------|--------|
| 0–2                      | WEAK   |
| 3–4                      | MEDIUM |
| 5                        | STRONG |

## How to Run

```
python password-strength-checker.py
```

You'll be prompted to enter a password, then the program prints a
breakdown of each requirement and the overall rating.

## Example Output

```
=== Password Strength Checker ===
Enter a password to check: Str0ng!Password

Password Analysis
----------------------------------------
  [PASS] At least 8 characters
  [PASS] Contains uppercase letter
  [PASS] Contains lowercase letter
  [PASS] Contains a number
  [PASS] Contains special character
----------------------------------------
Requirements satisfied: 5/5
Strength: STRONG
----------------------------------------
```

## Explanation of Logic

The program is broken into small, single-purpose functions rather than
one large block of code:

- **`check_length`, `check_uppercase`, `check_lowercase`, `check_number`,
  `check_special_character`** — each one loops through the password
  character by character and returns `True` as soon as it finds a
  character matching what it's looking for (e.g. a digit, or a
  character from the special-characters list), or `False` if it never
  finds one. Keeping these as five separate functions, instead of one
  big function, means each requirement can be understood, tested, and
  changed independently.

- **`analyze_password`** — calls all five check functions on the given
  password and collects the results into a dictionary, mapping each
  requirement's description to whether it passed. This function only
  answers "what did the password satisfy" — it doesn't decide on a
  rating.

- **`get_strength_rating`** — takes that dictionary, counts how many
  requirements passed, and maps the count to a WEAK/MEDIUM/STRONG
  label using simple threshold checks. Separating this from
  `analyze_password` means the rating logic (and its thresholds) can
  be changed without touching how individual requirements are
  checked.

- **`display_results`** — takes the results dictionary and the rating,
  and prints everything in a readable format: a pass/fail line per
  requirement, followed by the score and overall strength.

- **`main`** — ties everything together: gets the password from the
  user, calls `analyze_password`, then `get_strength_rating`, deletes
  the password from memory once it's no longer needed, and finally
  calls `display_results`.

### Privacy Note

The password is read into memory only long enough to run the checks.
It is never printed, logged, or written to any file, and the variable
holding it is explicitly deleted (`del password`) once analysis is
complete.

## Skills Demonstrated

- **Strings**: character-by-character iteration, `.isupper()`,
  `.islower()`, `.isdigit()`, membership checks (`in`)
- **Conditions**: `if` / `elif` / `else` for both individual checks
  and the strength-rating thresholds
- **Loops**: `for` loops for scanning password characters and for
  counting satisfied requirements
- **Functions**: single-responsibility functions composed together
  in `main`