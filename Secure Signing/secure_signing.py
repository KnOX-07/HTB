from hashlib import sha256
from pwn import *
import string

charset = string.ascii_letters + string.digits + "{}_@#!"

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

def H(m):
    return sha256(m).digest()

io = remote("94.237.54.201", 35828)
p = log.progress("flag")

last_flag = "HTB{"  
last_hash = ""
new_hash = ""
zero_xor_hash = ""

while True:
    flag_length = len(last_flag) + 1  
    zero_xor_flag = "." * flag_length
    zero_xor_hash = H(xor(zero_xor_flag.encode(), zero_xor_flag.encode())).hex()
    
    for c in charset:
        new_flag = last_flag + c  
        
        io.recvuntil(b"> ")
        io.send(b"1\n")  
        
        io.recvuntil(b": ")
        io.send(new_flag.encode() + b"\n")  
        
        io.recvuntil(b": ")
        new_hash = io.recvline().decode().strip()  
        
        if last_hash and last_hash == new_hash:
            p.success(f"Success! The flag is {last_flag}}}")  
            io.close()
            exit()
        
        if zero_xor_hash == new_hash:
            p.status(f"Found: {new_flag} -> Hash: {new_hash}")
            last_flag = new_flag 
            last_hash = new_hash  
            break
    else:
        p.failure("Failed to find a matching character!")
        io.close()
        break
