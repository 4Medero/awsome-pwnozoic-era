# X64 CALL CONVENTION

In x64 linux arguments to a function are passed via registers. The first few args are passed by these registers:
```
rdi:    First Argument
rsi:    Second Argument
rdx:    Third Argument
rcx:    Fourth Argument
r8:     Fifth Argument
r9:     Sixth Argument
```