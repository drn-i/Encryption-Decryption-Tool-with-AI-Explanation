from sympy import mod_inverse

def encrypt(plaintext, key, additional_key, e=17):
    p, q = map(int, additional_key.split(","))
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    result = ""
    steps = [f"p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}"]