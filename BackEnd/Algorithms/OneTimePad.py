def xor_strings(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def encrypt(input_text, key, additional_key=None):
    if len(key) < len(input_text):
        raise ValueError("Key must be at least as long as the input text")

    ciphertext = xor_strings(input_text, key)
    steps = [
        f"Input text: {input_text}",
        f"Key used: {key}",
        "XOR each character in the text with the corresponding character in the key",
        f"Ciphertext (raw): {ciphertext}",
        f"Ciphertext (hex): {ciphertext.encode().hex()}"
    ]
    return ciphertext.encode().hex(), steps

def decrypt(input_text, key, additional_key=None):
    ciphertext = bytes.fromhex(input_text).decode()
    plaintext = xor_strings(ciphertext, key)
    steps = [
        f"Ciphertext (hex): {input_text}",
        f"Key used: {key}",
        "XOR each character in the ciphertext with the corresponding character in the key",
        f"Recovered plaintext: {plaintext}"
    ]
    return plaintext, steps