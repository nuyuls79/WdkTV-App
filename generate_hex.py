#!/usr/bin/env python3
import base64
import binascii

KEY = "Rahasia123"   # harus sama dengan kunci di C++ nanti

def xor_encrypt(plain_text: str) -> str:
    b64 = base64.b64encode(plain_text.encode()).decode()
    key_bytes = KEY.encode()
    b64_bytes = b64.encode()
    out = bytearray()
    for i, b in enumerate(b64_bytes):
        out.append(b ^ key_bytes[i % len(key_bytes)])
    return binascii.hexlify(out).decode()

if __name__ == "__main__":
    premium = "https://raw.githubusercontent.com/nuyuls79/StreamPlay-Free/refs/heads/builds/repo.json"
    free    = "https://raw.githubusercontent.com/michat88/Repo_Gratis/refs/heads/builds/repo.json"
    firebase = ""   # kosong, biarkan
    print("PREMIUM_HEX =", xor_encrypt(premium))
    print("FREE_HEX    =", xor_encrypt(free))
    if firebase:
        print("FIREBASE_HEX =", xor_encrypt(firebase))