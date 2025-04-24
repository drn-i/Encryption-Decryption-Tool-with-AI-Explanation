def create_column_order(key):
    return sorted(list(enumerate(key)), key=lambda x: x[1])

def encrypt(text, key, _=None):
    key_len = len(key)
    text = text.replace(" ", "")
    while len(text) % key_len != 0:
        text += 'X'

    rows = [text[i:i+key_len] for i in range(0, len(text), key_len)]
    col_order = create_column_order(key)
    result = ""
    steps = []

    for idx, _ in col_order:
        col = ''.join(row[idx] for row in rows)
        result += col
        steps.append(f"Column {idx+1}: {col}")
    return result, steps

def decrypt(text, key, _=None):
    key_len = len(key)
    col_order = create_column_order(key)
    col_height = len(text) // key_len

    cols = [''] * key_len
    start = 0
    for idx, _ in col_order:
        cols[idx] = text[start:start+col_height]
        steps = [f"Column {idx+1}: {cols[idx]}"]
        start += col_height

    result = ""
    for i in range(col_height):
        for j in range(key_len):
            result += cols[j][i]

    return result, steps
