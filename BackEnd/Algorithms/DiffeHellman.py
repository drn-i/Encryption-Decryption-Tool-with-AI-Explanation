def encrypt(_, key, additional_key):
    p, g = map(int, additional_key.split(","))
    a = int(key)
    B = int(_)  # Public key of other party
    shared_secret = pow(B, a, p)
    steps = [
        f"Prime (p) = {p}, Primitive Root (g) = {g}",
        f"Private Key (a) = {a}, Other's Public (B) = {B}",
        f"Shared Secret = B^a mod p = {shared_secret}"
    ]
    return str(shared_secret), steps

def decrypt(_, key, additional_key):
    return encrypt(_, key, additional_key)