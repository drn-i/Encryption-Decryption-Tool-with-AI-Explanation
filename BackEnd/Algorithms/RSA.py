from sympy import mod_inverse

def encrypt(plaintext, key, additional_key, e=17):
    p, q = map(int, additional_key.split(","))
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    result = ""
    steps = [f"p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}"]
    for char in plaintext:
        m = ord(char.lower()) - ord('a')
        c = pow(m, e, n)
        result += chr((c % 26) + 65)
        steps.append(f"{char} -> {chr((c % 26) + 65)} (m = {m}, c = {c})")
    return result, steps

def decrypt(ciphertext, key, additional_key, e=17):
    p, q = map(int, additional_key.split(","))
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    result = ""
    steps = [f"p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}"]
    for char in ciphertext:
        c = ord(char.lower()) - ord('a')
        m = pow(c, d, n)
        result += chr(m + 65)
        steps.append(f"{char} -> {chr(m + 65)} (c = {c}, m = {m})")
    return result, steps