## Integer Overflow

These vulnerabilities occur due to incorrect calculations leading to integer overflows.
### Vulnerable functions:
They are not directly associated with specific functions, but errors occur in calculations involving:

Memory sizes (`malloc`, `calloc`, etc.).

* Indexes in arrays.

Arithmetic operations without validations (+, -, *, *, /).

* Use of standard functions that depend on variable sizes (such as `memcpy` and `strncpy`).
