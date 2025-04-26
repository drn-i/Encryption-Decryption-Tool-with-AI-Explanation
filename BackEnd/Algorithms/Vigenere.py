def repeat_key(key, length):
    return (key * (length // len(key))) + key[:length % len(key)]

def encrypt(text, key, _=None):
    key = repeat_key(key, len(text))
    result = ""
    steps = []

    for t_char, k_char in zip(text, key):
        if t_char.isalpha():
            base = ord('A') if t_char.isupper() else ord('a')
            k = ord(k_char.lower()) - ord('a')
            new_char = chr((ord(t_char) - base + k) % 26 + base)
            result += new_char
            steps.append(f"{t_char} + {k_char} -> {new_char} (shift {k})")
        else:
            result += t_char
            steps.append(f"{t_char} -> {t_char} (non-alpha)")

    return result, steps

def decrypt(text, key, _=None):
    key = repeat_key(key, len(text))
    result = ""
    steps = []
    for t_char, k_char in zip(text, key):
        if t_char.isalpha():
            base = ord('A') if t_char.isupper() else ord('a')
            k = ord(k_char.lower()) - ord('a')
            new_char = chr((ord(t_char) - base - k) % 26 + base)
            result += new_char
            steps.append(f"{t_char} - {k_char} -> {new_char} (shift -{k})")
        else:
            result += t_char
            steps.append(f"{t_char} -> {t_char} (non-alpha)")
    return result, steps