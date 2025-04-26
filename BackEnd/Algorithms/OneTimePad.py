def encrypt(plaintext, key, additional_key):
    # Ensure the key is at least as long as the plaintext
    if len(key) < len(plaintext):
        raise ValueError("Key must be at least as long as the plaintext")

    ciphertext = ""
    steps = []

    # Loop over each character in the plaintext and the key
    for i, (p, k) in enumerate(zip(plaintext, key)):
        # Convert characters to their positions in the alphabet (0 = A, 1 = B, ..., 25 = Z)
        p_pos = ord(p) - ord('A')
        k_pos = ord(k) - ord('A')

        # Apply the XOR operation using modular arithmetic and wrap around with modulo 26
        cipher_pos = (p_pos + k_pos) % 26

        # Convert the result back to a character
        cipher_char = chr(cipher_pos + ord('A'))

        # Add the character to the ciphertext
        ciphertext += cipher_char

        # Document the calculation for each step
        steps.append(f"Step {i+1}: '{p}' (Position {p_pos}) + '{k}' (Position {k_pos}) = "
                     f"({p_pos} + {k_pos}) % 26 = {cipher_pos} -> {cipher_char}")

    return ciphertext, steps

def decrypt(ciphertext, key, additional_key):
    # Ensure the key is at least as long as the ciphertext
    if len(key) < len(ciphertext):
        raise ValueError("Key must be at least as long as the ciphertext")

    plaintext = ""
    steps = []

    # Loop over each character in the ciphertext and the key
    for i, (c, k) in enumerate(zip(ciphertext, key)):
        # Convert characters to their positions in the alphabet (0 = A, 1 = B, ..., 25 = Z)
        c_pos = ord(c) - ord('A')
        k_pos = ord(k) - ord('A')

        # Reverse the XOR operation for decryption
        plain_pos = (c_pos - k_pos) % 26

        # Convert the result back to a character
        plain_char = chr(plain_pos + ord('A'))

        # Add the character to the plaintext
        plaintext += plain_char

        # Document the calculation for each step
        steps.append(f"Step {i+1}: '{c}' (Position {c_pos}) - '{k}' (Position {k_pos}) = "
                     f"({c_pos} - {k_pos}) % 26 = {plain_pos} -> {plain_char}")

    return plaintext, steps