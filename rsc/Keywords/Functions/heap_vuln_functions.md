## Heap (Heap-related vulnerabilities)

These vulnerabilities occur due to mismanagement of dynamic memory in the heap.
### Vulnerable functions:

`malloc`, `calloc`, `realloc`: Misuse of these functions, such as not checking the return of a null pointer or not properly handling the allocated size, can generate vulnerabilities.

`free`: Use double free or use-after-free.

`strdup`: Do not check the size before duplicating strings.

`memcpy`: May overwrite heap memory if size is not validated correctly.