def encrypt(text, key, _=None):
    try:
        shift = int(key) % 26
    except ValueError:
        raise ValueError ("The Key must be an Integer for the Caesar Cipher.")

    result = ""
    steps = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
            steps.append(f"{char} -> {new_char} (shift + {shift})")
        else:
            result += char
            steps.append(f"{char} -> {char} (non-alpha)")

    return result, steps

def decrypt(text, key, _=None):
    try:
        shift = int(key) % 26
    except ValueError:
        raise ValueError("The Key must be an Integer for the Caesar Cipher.")

    result = ""
    steps = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
            steps.append(f"{char} -> {new_char} (shift - {shift})")
        else:
            result += char
            steps.append(f"{char} -> {char} (non-alpha)")

    return result, steps

