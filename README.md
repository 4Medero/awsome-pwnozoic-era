![Pwnozoic-Era](https://github.com/user-attachments/assets/a1796ca7-0171-4d26-96bd-185e33d2debd)

<p> 
<img src="https://github.com/user-attachments/assets/d9f33e61-bf4d-452f-aa11-2370a9b3f045" align="left">
</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

**A curated list of resources about learning binary exploitation(Pwnology Roadmap)**

## Books
### Exploiting
- ["Hacking: The Art of Exploitation" (2nd Edition)](https://www.amazon.com/Hacking-Art-Exploitation-Jon-Erickson/dp/1593271441) - Jon Erickson
- ["The Shellcoder's Handbook"](https://www.amazon.com/Shellcoders-Handbook-Discovering-Exploiting-Security/dp/047008023X?tag=hydsma-20&source=dsa&hvcampaign=booksm&gclid=Cj0KCQiA7NO7BhDsARIsADg_hIYCIo5qmBmkGYY-0UbmPKh-Fh8mrsQnRtYh4Y58XGvpgZFyd89-mCUaAobNEALw_wcB) - Chris Anley, John Heasman, Felix Lindner y Gerardo Richarte
- ["Exploiting Software: How to Break Code"](https://www.amazon.com/Exploiting-Software-How-Break-Code/dp/0201786958) - Greg Hoglund y Gary McGraw
- ["Practical Binary Analysis: Build Your Own Linux Tools for Binary Instrumentation, Analysis, and Disassembly](https://practicalbinaryanalysis.com/) - Dennis Andriesse
- ["Modern Binary Exploitation"](https://github.com/RPISEC/MBE) - RPISEC

### Reversing
- ["Reversing: Secrets of Reverse Engineering"](https://www.amazon.com/Reversing-Secrets-Engineering-Eldad-Eilam/dp/0764574817?tag=hydsma-20&source=dsa&hvcampaign=booksm&gclid=Cj0KCQiA7NO7BhDsARIsADg_hIa9tDeiK_tyhYTX-GDp78DR6pB95qbo7N1EHUV9DBklYNO1jSPBV50aAqH5EALw_wcB) - Eldad Eilam
- ["Practical Reverse Engineering"](https://www.amazon.com/Practical-Reverse-Engineering-Reversing-Obfuscation/dp/1118787315) - Bruce Dang
- ["Gray Hat Python"](https://www.amazon.com/Gray-Hat-Python-Programming-Engineers/dp/1593271921) - Justin Seitz

## Tools

* **Debuggers**:
  - [gdb](https://es.m.wikipedia.org/wiki/GNU_Debugger) - GNU Debugger
  - [radare2](https://www.radare.org/) - UNIX-like reverse engineering framework and command-line toolset
  - [GEF](https://hugsy.github.io/gef) - GEF (GDB Enhanced Features) - a modern experience for GDB with advanced debugging capabilities for exploit devs & reverse engineers on Linux
  - [pwndbg](https://pwndbg.re/) - Exploit Development and Reverse Engineering with GDB Made Easy
  - [gdb-peda](https://github.com/longld/peda) - PEDA - Python Exploit Development Assistance for GDB
  - [x64dbg](https://x64dbg.com/) - An open-source x64/x32 debugger for windows.
  - [OllyDbg](https://www.ollydbg.de/) - OllyDbg is a 32-bit assembler level analysing debugger for Microsoft®.
    
* **Decompilers**:
  - [angr](https://angr.io/) - angr is an open-source binary analysis platform for Python. It combines both static and dynamic symbolic ("concolic") analysis, providing tools to solve a variety of tasks.
  - [Binary Ninja](https://binary.ninja/) - Binary Ninja is an interactive decompiler, disassembler, debugger, and binary analysis platform built by reverse engineers, for reverse engineers.
  - [DogBolt](https://dogbolt.org/) - It is an interactive online decompiler which shows equivalent C-like output of decompiled programs from many popular decompilers.
  - [Ghidra](https://ghidra-sre.org/) - Ghidra is a software reverse engineering (SRE) framework
  - [IDA](https://hex-rays.com/ida-free) - IDA is commonly used in software reverse engineering, assisting with malware analysis and vulnerability detection.
    
* **Libraries**:
  - [pwntools](https://docs.pwntools.com/en/stable/) - pwntools is a CTF framework and exploit development library. Written in Python, it is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible.
  - [r2pipe](https://github.com/radareorg/radare2-r2pipe) - Access radare2 via pipe from any programming language!
  - [capstone](https://www.capstone-engine.org) - Capstone disassembly/disassembler framework for ARM, ARM64 (ARMv8), Alpha, BPF, Ethereum VM, HPPA, LoongArch, M68K, M680X, Mips, MOS65XX, PPC, RISC-V(rv32G/rv64G), SH, Sparc, SystemZ, TMS320C64X, TriCore, Webassembly, XCore and X86.
  - [struct](https://docs.python.org/3/library/struct.html) - This module converts between Python values and C structs represented as Python bytes objects.
  - [sockets](https://docs.python.org/es/3/library/socket.html) - This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
    
## Training platforms
- [Deusx64](https://deusx64.ai/)
- [pwnable.tw](https://pwnable.tw/)
- [pwn.college](https://pwn.college/dojos)
- [PicoGym](https://play.picoctf.org/)
- [Pwn101 TryHackMe](https://tryhackme.com/r/room/pwn101)
- [ROPEmporium](https://ropemporium.com/)
- [crackmes.one](https://crackmes.one/)
- [Microcorruption](https://microcorruption.com/)

## Attack Techniques 

### [Stack && Buffer Overflow(BOF)](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
BOF occurs when the amount of data in the buffer exceeds its storage capacity. That extra data overflows into adjacent memory locations and corrupts or overwrites the data in those locations.
[Example](rsc/BOF/)

* [Ret2Shellcode](https://www.youtube.com/watch?v=6Yiupj3XHrM)
  - Consists of injecting shellcode into the program's memory, usually on the stack or heap, and then redirecting the execution flow to that location to execute it.
  - **When**:
    - `NX Disabled`
    - No `ASLR` or limited
    - No `stack canary` found
    - Availability of executable memory
* [Ret2Win](https://ir0nstone.gitbook.io/notes/binexp/stack/ret2win)
  - ret2win is a binary exploitation technique that consists of redirecting the execution flow to an existing function within the binary that already performs a useful task for the attacker, such as opening a shell or reading a specific file.
  - **When**:
    - `NX`
    - No `ASLR` or limited
    - A `win()` function
  - [Example](rsc/Ret2Win/)
* [Ret2Libc](https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc)
  - Redirects the execution flow to existing functions in the standard C library (libc), such as *system()*, *execve()* or *exit()*. Instead of injecting code, functions available in program memory are reused. It is especially useful for executing arbitrary commands (such as opening a shell) on protected systems.
  - **When**:
    - `NX`
    - No `ASLR` or limited(Partial)
    - No `stack canary` found(Partial)
    - `RELRO`(Partial)
    - Note: Although ASLR randomizes addresses in memory, in binaries without `PIE` (Position Independent Executable), the libc base address can be predictable or filtered through information leaks. See [leaked libc](https://github.com/D4nex/Notes/blob/master/Binary%20Exploitation/leaked_libc.md)

## Resources

### Assambly
* Registers
  - [x32 Registers](rsc/Keywords/Assambly/x32registers.md)
  - [x64 Registers](rsc/Keywords/Assambly/x64registers.md)
  - [Registers Table](rsc/Keywords/Assambly/registers_table.md)
  - [Call Convention](rsc/Keywords/Assambly/call_convention.md)
  - [Endianess](https://youtu.be/T8E_JRqN0fY?si=GoPxTucPUx3sfnZ6)
* Stack:
  - [The Stack](https://ctf101.org/binary-exploitation/what-is-the-stack/)
* Heap:
  - [The Heap](https://ir0nstone.gitbook.io/notes/binexp/heap/introduction-to-the-heap)
### C vulnerable functions
* [Stack && Buffer Overflow](rsc/Keywords/Functions/bof_vuln_functions.md)
* [Heap Overflow](rsc/Keywords/Functions/heap_vuln_functions.md)
* [Format String ](rsc/Keywords/Functions/fstring_vuln_functions.md)
* [Integer Overflow ](rsc/Keywords/Functions/iof_vuln_functions.md)

### Protections
* [NX](rsc/Keywords/Protections/NX.md)
* [Stack Canary](rsc/Keywords/Protections/CANARY)
* [ASLR](rsc/Keywords/Protections/ASLR.md)

### Linux binaries(ELF)
* [PLT && GOT](rsc/Keywords/Assambly/plt_got.md)
## Pwnology

![Pwnology](https://github.com/user-attachments/assets/549f39f3-1aaf-408d-96e9-4bad0e0eb37e)
[Pwnology by AbuCTF](https://abuctf.github.io/posts/Pwnology/)
