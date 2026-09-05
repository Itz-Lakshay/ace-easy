# Manual Test Cases

The following edge cases were run manually against
`password-strength-checker.py` to confirm correct behavior beyond the
typical examples in the README.

| # | Input                  | Notes                              | Result                |
|---|-------------------------|-------------------------------------|------------------------|
| 1 | `` (empty string)       | No characters at all                | 0/5 — WEAK             |
| 2 | `aaaaaaaa`               | Long, but only lowercase            | 2/5 — WEAK             |
| 3 | `12345678`               | Long, but only digits               | 2/5 — WEAK             |
| 4 | `!!!!!!!!`               | Long, but only special characters   | 2/5 — WEAK             |
| 5 | `Ab1!Ab1!`               | Short (8 chars) but hits every type | 5/5 — STRONG           |
| 6 | `AAAAAAAA1!`             | No lowercase letter                 | 4/5 — MEDIUM           |

These confirm:
- An empty password is handled without errors (all checks correctly
  return `False`, nothing crashes on an empty string).
- Length alone does not guarantee a high score — a long password
  missing several character types still rates WEAK or MEDIUM.
- The minimum 8-character password can still reach STRONG if it hits
  every other requirement.