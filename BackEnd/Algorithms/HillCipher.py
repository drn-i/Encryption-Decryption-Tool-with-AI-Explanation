import numpy as np


def create_matrix(key):
    # Remove the square brackets and spaces, then split by commas
    key = key.strip("[]").replace(" ", "")
    key_list = list(map(int, key.split(",")))

    if len(key_list) != 4:
        raise ValueError("Key must be a list of 4 integers for a 2x2 Hill matrix.")

    return np.array(key_list).reshape(2, 2)


def mod26(matrix):
    return np.round(matrix).astype(int) % 26


def encrypt(text, key, _=None):
    matrix = create_matrix(key)
    text = text.replace(' ', '').upper()
    if len(text) % 2 != 0:
        text += 'X'  # Padding

    steps = []
    result = ''
    for i in range(0, len(text), 2):
        pair = text[i:i + 2].upper()
        vector = np.array([[ord(pair[0]) - 65], [ord(pair[1]) - 65]])  # plaintext vector
        # Now using p * K instead of K * p
        transformed = np.dot(vector.T, matrix)  # Transpose the vector for p * K
        encrypted = mod26(transformed)
        encrypted_text = ''.join([chr(int(n) + 65) for n in encrypted.flatten()])
        result += encrypted_text
        steps.append(f'{pair} -> {encrypted_text} using matrix {matrix.tolist()}')

    return result, steps


def decrypt(text, key, _=None):
    matrix = create_matrix(key)
    det = int(np.round(np.linalg.det(matrix)))
    if det == 0 or np.gcd(det, 26) != 1:
        raise ValueError("Matrix is not invertible modulo 26.")

    det_inv = pow(det % 26, -1, 26)
    inv_matrix = np.linalg.inv(matrix) * det
    adjugate = mod26(inv_matrix * det_inv)

    text = text.replace(' ', '').upper()
    steps = []
    result = ''
    for i in range(0, len(text), 2):
        pair = text[i:i + 2].upper()
        vector = np.array([[ord(pair[0]) - 65], [ord(pair[1]) - 65]])  # ciphertext vector
        # Decrypting using the inverse matrix
        decrypted = np.dot(vector.T, adjugate)  # Transpose the vector for p * K
        plain = mod26(decrypted)
        plain_text = ''.join([chr(int(n) + 65) for n in plain.flatten()])
        result += plain_text
        steps.append(f'{pair} -> {plain_text} using inverse matrix {adjugate.tolist()}')

    return result, steps
