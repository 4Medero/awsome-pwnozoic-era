# ASLR Protection

ASLR (Address Space Layout Randomization) protection is a security technique implemented in operating systems to make it more difficult to exploit vulnerabilities in programs, especially those related to buffer overflows and memory manipulations.

## What is ASLR?

ASLR consists of randomizing the memory addresses where the different parts of a program are loaded (such as the stack, heap, shared libraries, and program segments). This makes the memory addresses change every time the program is executed, making it difficult for an attacker to predict or use specific addresses to exploit vulnerabilities.

## How it works

* Randomized segments:

The memory addresses of the stack, heap, and .text (code) and .data (global variables) sections of the program are loaded at different locations at each execution.

Shared libraries (such as libc) are also loaded at random addresses.
* Effect on exploitation:

Attacks that rely on known addresses (such as returning to the stack or calling specific functions in libc) fail because the addresses change on each execution.

## Benefits of ASLR

* Makes memory-based attacks more difficult: An attacker cannot easily predict where the data or code he needs to manipulate is located.

* Mitigates reusable exploits: Exploits designed for fixed addresses will not work on ASLR-enabled systems.

* Combined protection: Works well in conjunction with other security techniques, such as non-executable execution ([NX](rsc/Keywords/Protections/NX.md))and [stack canarie](rsc/Keywords/Protections/CANARY.md)