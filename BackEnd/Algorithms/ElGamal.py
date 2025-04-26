from sympy import isprime, nextprime, mod_inverse
import random


def get_next_prime(approx_value):
    value = int(approx_value)
    if not isprime(value):
        value = nextprime(value)
    return value


def get_generator(p):
    for _ in range(1000):
        rand = random.randint(2, p - 2)
        exp = 1
        next_val = rand % p
        while next_val != 1:
            next_val = (next_val * rand) % p
            exp += 1
        if exp == p - 1:
            return rand
    return None


def encrypt(plaintext, p, g, b):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = pow(b, k, p)

    m = int(plaintext)
    c2 = (c2 * m) % p

    steps = [
        f"Random k = {k}",
        f"c1 = g^k mod p = {g}^{k} mod {p} = {c1}",
        f"Intermediate c2 = b^k mod p = {b}^{k} mod {p} = {pow(b, k, p)}",
        f"Final c2 = (b^k * m) mod p = ({pow(b, k, p)} * {m}) mod {p} = {c2}"
    ]

    return (c1, c2), steps


def decrypt(cipher_pair, p, a):
    c1, c2 = cipher_pair
    temp = pow(c1, a, p)
    temp_inv = mod_inverse(temp, p)
    plaintext = (temp_inv * c2) % p

    steps = [
        f"temp = c1^a mod p = {c1}^{a} mod {p} = {temp}",
        f"temp_inv = modular inverse of temp mod p = {temp_inv}",
        f"plaintext = (temp_inv * c2) mod p = ({temp_inv} * {c2}) mod {p} = {plaintext}"
    ]

    return plaintext, steps


# 👉 This is the main function you will call from your API:
def elgamal_encrypt_from_frontend(approximate_p, plaintext):
    p = get_next_prime(approximate_p)
    g = get_generator(p)

    if g is None:
        return {"error": "No generator found for prime p"}, None

    a = random.randint(2, p - 2)  # Private key
    b = pow(g, a, p)  # Public key

    cipher, encrypt_steps = encrypt(plaintext, p, g, b)

    response = {
        "prime_p": p,
        "generator_g": g,
        "private_key_a": a,
        "public_key_b": b,
        "cipher": {
            "c1": cipher[0],
            "c2": cipher[1]
        },
        "encryption_steps": encrypt_steps
    }
    return response, (p, g, a, b)  # Also returning keys if needed


def elgamal_decrypt_from_frontend(c1, c2, p, a):
    plaintext, decrypt_steps = decrypt((c1, c2), p, a)

    response = {
        "plaintext": plaintext,
        "decryption_steps": decrypt_steps
    }
    return response
