# XnR

XN (Execute Never) protection, also known as XnR (eXecute no Read), is a security mechanism that prevents code execution from certain memory regions, such as the stack or heap. This helps prevent attacks that rely on executing injected code, such as buffer overflows or shellcode.

How does it work?

XN uses control bits in the operating system page table to mark memory regions as:

Executable: legitimate code, such as the program binary and its libraries.

Non-executable: Regions intended for data, such as stack, heap or dynamic mapping areas.

This ensures that any attempt to execute code from areas marked as "Non-executable" results in a segmentation fault or hardware exception.

## Common Implementations

* DEP (Data Execution Prevention):

Available on Windows systems.

It marks memory allocated to data as non-executable by default.

* W^X (Write XOR Execute):

Common on UNIX and BSD systems.

Prohibits a memory region from being simultaneously writable and executable.

* ARM Execute Never (XN):

ARM architecture uses an XN bit in its page table to implement this protection.