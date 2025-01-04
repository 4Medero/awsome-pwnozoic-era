# CFI

Control Flow Integrity Protection (CFI) is a security technique designed to prevent attacks that manipulate the control flow of a program, such as Return-Oriented Programming (ROP) or Jump-Oriented Programming (JOP). It ensures that the execution of a program follows only legitimate paths defined in its code.

# How does it work?

CFI protects the control flow through two main steps:

* Compile-Time Analysis:

The compiler generates a valid map of all control destinations allowed in the program (e.g., addresses to which jumps, calls, or returns can be made).

* Runtime Validation:

During execution, the destinations of each jump, call or return are checked against the previously defined map.

If the destination is not valid, the program blocks or stops execution.

# Types of CFI

* Indirect Branch Target Validation:

Protects indirect jumps (jmp or call) by ensuring that they point only to legitimate locations.

 * Forward-Edge CFI:

Protects function calls (forward control).

Example: Verify that an indirect call to a virtual function points only to valid methods of an object.

* Backward-Edge CFI:

Protects function returns (backward control).

Example: Guarantee that a return returns to an address previously stored in the stack, avoiding malicious redirections.