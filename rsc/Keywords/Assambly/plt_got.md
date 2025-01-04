# The PLT and GOT

When you call `puts()` in C and compile it as an ELF executable, it is not _actually_ `puts()` - instead, it gets compiled as `puts@plt`. Check it out in GDB:

![](https://ir0nstone.gitbook.io/~gitbook/image?url=https%3A%2F%2F349224153-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MEwBGnjPgf263kl5vWP%252Fsync%252F485781dd12eb3125bb8d6a6e4393d90fe8e212ae.png%3Fgeneration%3D1597664138404840%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=bca65646&sv=2)

Why does it do that?

Well, as we said, it doesn't know where `puts` actually is - so it jumps to the PLT entry of `puts` instead. From here, `puts@plt` does some very specific things:

- If there is a GOT entry for `puts`, it jumps to the address stored there.
    
- If there isn't a GOT entry, it will resolve it and jump there.
    

The GOT is a _massive_ table of addresses; these addresses are the actual locations in memory of the `libc` functions. `puts@got`, for example, will contain the address of `puts` in memory. When the PLT gets called, it reads the GOT address and redirects execution there. If the address is empty, it coordinates with the `ld.so` (also called the **dynamic linker/loader**) to get the function address and stores it in the GOT.

How is this useful for binary exploitation?

Well, there are two key takeaways from the above explanation:

- Calling the PLT address of a function is equivalent to calling the function itself
    
- The GOT address contains addresses of functions in `libc`, and the GOT is within the binary.
    

The use of the first point is clear - if we have a PLT entry for a desirable `libc` function, for example `system`, we can just redirect execution to its PLT entry and it will be the equivalent of calling `system` directly; no need to jump into `libc`.

The second point is less obvious, but debatably even more important. As the GOT is part of the binary, it will always be a constant offset away from the base. Therefore, if PIE is disabled or you somehow leak the binary base, you know the exact address that contains a `libc` function's address. If you perhaps have an arbitrary read, it's trivial to leak the real address of the `libc` function and therefore bypass ASLR.