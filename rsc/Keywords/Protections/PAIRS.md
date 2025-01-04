# PAIRS

PaX Pairs protection is a security technique included in the PaX project (a security patch for Linux). It is designed to mitigate the exploitation of buffer overflow vulnerabilities by protecting pairs of related critical data in memory, such as pointers and associated data. This makes it difficult for attackers to manipulate linked memory structures.

## How does it work?

* Pointer and Data Pairing:

The technique ensures that pointers (references to memory) are tightly linked with the data they handle.

If one of the elements of the pair is manipulated, the system detects the discrepancy and responds appropriately.

* Metadata Protection:

Protects heap metadata structures to prevent malicious corruption, such as in heap overflow attacks.

* Consistency Validation:

Implements checks to ensure that peers remain synchronized and consistent.