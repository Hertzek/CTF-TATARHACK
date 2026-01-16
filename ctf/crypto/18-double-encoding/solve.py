import base64

flag = "TATARHACK{d0ubl3_3nc0d1ng}"
key = "SEC"

# Кодирование: XOR → Base64
def encode(plaintext, key):
    # Шаг 1: XOR
    xored = bytes([ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(plaintext)])
    # Шаг 2: Base64
    encoded = base64.b64encode(xored).decode()
    return encoded

# Декодирование: Base64 → XOR
def decode(data, key):
    # Шаг 1: Base64 decode
    decoded = base64.b64decode(data)
    # Шаг 2: XOR decrypt
    plaintext = ''.join(chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(decoded))
    return plaintext

# Генерация
encoded = encode(flag, key)
print(f"Encoded: {encoded}")

# Проверка
decoded = decode(encoded, key)
print(f"Decoded: {decoded}")
