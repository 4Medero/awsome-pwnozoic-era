# NX Protection

NX (No-eXecute) protection, also known as DEP (Data Execution Prevention), is a security measure used to prevent code execution in memory areas that are not intended to be executable. This helps mitigate various types of attacks, such as buffer overflows and shellcode injection.

## How does NX work?

* Memory tagging:
  - The operating system and hardware mark certain memory regions as "non-executable". For example:
    - [Stack](https://ctf101.org/binary-exploitation/what-is-the-stack/): Used for data (not code).
    - [Heap](https://ir0nstone.gitbook.io/notes/binexp/heap/introduction-to-the-heap): Used for dynamic storage (not code).
* Execution prevention:
  - If the program tries to execute instructions from a region marked as "not executable", the system generates an exception or error, stopping the execution.
* Affected regions:
  - Normally, regions such as stack and heap are protected, while legitimate code sections (.text) are executable.

## Benefits of NX

* Protection against shellcode:
Attackers cannot execute code injected into the stack or heap.

* Hinders exploits:
Mitigates attacks that rely on executing malicious code in areas not designed for it.

* [ASLR](./ASLR.md) compatibility:
Together with ASLR, forms a solid barrier against many types of exploits.

## Limitations of NX

* Does not protect against ROP:
Attackers can use techniques such as Return-Oriented Programming (ROP) to reuse legitimate instructions within the program or shared libraries.
* Insecure programs:
If a program has vulnerabilities such as infoleaks or does not implement NX properly, an attacker can find ways to evade this protection.
* Compatibility:
On older systems or systems with obsolete hardware, NX may not be supported.
