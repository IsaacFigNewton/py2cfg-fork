#!/usr/bin/python3

print("\nEnter your Caesar key in numeric form (1-25): ")
key: int = int(input())

print("\nEnter 1 for encryption, and 0 for decryption: ")
mode: int = int(input())

print("\nEnter your single character, Caesar encoded: ")
encoded_char: int = int(input())

print("\nYour message translation is:\n")

if mode == 1:
    # 26 is the symbol set size (# letters in alphabet)
    if (encoded_char + key) < 26:
        print(encoded_char + key)
    else:
        print((encoded_char + key) - 26)
else:
    # 26 is the symbol set size (# letters in alphabet)
    if 0 < (encoded_char - key):
        print(encoded_char - key)
    else:
        print((encoded_char - key) + 26)
