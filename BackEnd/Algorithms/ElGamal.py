from sympy import mod_inverse
import random

def encrypt(plaintext, key, additional_key):
    p, g = map(int, additional_key.split(","))
    x = int(key)
    y = pow(g, x, p)
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    steps = [f"p = {p}, g = {g}, x = {x}, y = {y}, k = {k}, c1 = {c1}"]
    c2 = []
    result = ""
    for char in plaintext:
        m = ord(char.lower()) - ord('a')
        cipher = (m * pow(y, k, p)) % p
        c2.append(cipher)
        result += chr((cipher % 26) + 65)
        steps.append(f"{char} -> {chr((cipher % 26) + 65)} (m = {m}, c2 = {cipher})")
    return result, steps

def decrypt(ciphertext, key, additional_key):
    p, g = map(int, additional_key.split(","))
    x = int(key)
    c1 = int(ciphertext[:4])
    c2 = [ord(c) - 65 for c in ciphertext[4:]]
    result = ""
    steps = [f"p = {p}, g = {g}, x = {x}, c1 = {c1}"]
    for c in c2:
        m = (c * mod_inverse(pow(c1, x, p), p)) % p
        result += chr(m + 65)
        steps.append(f"c2 = {c} -> {chr(m + 65)}")
    return result, steps