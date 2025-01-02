## Stack and Buffer Overflow

These vulnerabilities occur when data is written beyond the limit of a buffer in memory.
### Vulnerable functions:

***String manipulation***:

`strcpy`, `strcat`: Do not check the boundaries of the target buffer.

`gets`: Reads until a line break is found, but does not limit the size.

`sprintf`: Does not check the output buffer size.

`scanf (with %s)`: If no size limit is specified.

`strncpy`, `strncat`: Although safer, they can still be misused if the limits are not calculated correctly.


***Memory manipulation***:

`memcpy`, `memmove`, `strncpy`: If the specified size is incorrect, they can overwrite memory.

`alloca`: Allocates memory on the stack, which may overflow it if the size is large.


### Old and obsolete functions:

`bcopy`, `gets`, `scanf (no size specified)`.