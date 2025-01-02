# Stack Canary Protection
## What is a Stack Canary?

A canary is a random value (or a specific pattern) that is inserted just before the return address in the stack.

If an attack attempts to overwrite the return address, it will also overwrite the canary.

Before the function returns, the program checks if the canary has the same initial value. If a change is detected, the program assumes that the stack has been corrupted and aborts execution.

## How the protection works

* Canary placement:

When a function is called, a random value (the canary) is stored between the local variables and the return address in the stack.

* Canary check:

Before returning from the function, the program verifies that the value of the canary has not been altered.

 * Abort if there is alteration:

If the canary value does not match the original, the program throws an exception or quits to prevent the attacker from taking control.

## Types of Canaries

* Terminator Canary:

Uses special values such as NULL, CR, LF, or -1, which often break standard string handling functions and make overwriting difficult.

* Random Canary:

Uses a random value generated at the start of program execution. This makes it difficult for an attacker to predict the value.

* Random XOR Canary:

Similar to Random Canary, but mixes the value with sensitive data (such as the process ID) for added protection.

## Benefits of Stack Canary

* Prevention of basic buffer overflow attacks:
Stops simple return address overwrites.

* Ease of implementation:
It is a technique widely supported by compilers such as GCC and Clang via the -fstack-protector option.

## Limitations of Stack Canary

* It does not protect the entire stack:
Canaries only protect the return address, not other structures such as function pointers or sensitive variables in the stack.


* Dependency on infoleaks:
If an attacker can leak the value of the canary (via an infoleak-type vulnerability), the protection can be evaded.


* Performance overhead:
Introduces a slight overhead in the program due to additional insert and verify operations.


* Does not protect against ROP:
Return-Oriented Programming (ROP) attacks can evade Stack Canary without overwriting it.