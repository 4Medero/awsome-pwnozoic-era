# Heap Mitigations

Heap Mitigations are techniques and security mechanisms designed to protect the heap against attacks such as heap overflows, use-after-free, and double free. These mitigations make it more difficult to exploit vulnerabilities in the heap by adding additional protections and improving the randomness or integrity of dynamic memory.

## Main Heap Mitigation Techniques

* Heap Metadata Protection:

Heap management data (such as free block pointers or internal structures) is protected to prevent corruption.

Example: Canary on metadata to detect corruption before it is used.

* Heap Layout Randomization:

Changes the layout of memory blocks on the heap randomly to avoid predictions by the attacker.

Related to Address Space Layout Randomization (ASLR).

* Safe Unlinking:

Validates pointers when memory blocks are unallocated (freed), to avoid vulnerabilities such as unlinking attacks.

Example: Comparison of forward and backward pointers before deleting nodes in linked lists.

* Delayed Freeing:

Delays the reuse of freed blocks to mitigate attacks such as use-after-free.

Released blocks are placed in a temporary list before being reused.

* Heap Integrity Checks:

Implements periodic heap consistency checks to identify run-time corruption.

* Guard Pages:

Inserts unreachable pages around large blocks in the heap to detect overflows attempting to write outside the allocated boundaries.

* Heap Spraying Mitigation:

Blocks or hinders heap spraying techniques, where the attacker fills the heap with malicious data to increase the chances of an exploit succeeding.

* Isolation of Allocations:

Isolates different types of allocations (objects, strings, etc.) in different memory regions to prevent collisions between sensitive and controllable data by the attacker.

* Pointer Obfuscation:

Obfuscates pointers or memory addresses in internal heap structures to make them difficult to manipulate.