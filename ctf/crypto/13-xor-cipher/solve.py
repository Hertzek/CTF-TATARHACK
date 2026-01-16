# Генерация и решение XOR cipher

flag = "TATARHACK{x0r_1s_r3v3rs1bl3}"
key = "KEY"

# Шифрование
def xor_encrypt(plaintext, key):
    cipher = []
    for i, c in enumerate(plaintext):
        cipher.append(ord(c) ^ ord(key[i % len(key)]))
    return bytes(cipher)

cipher = xor_encrypt(flag, key)
print(f"Cipher (hex): {cipher.hex()}")

# Расшифровка (known-plaintext attack)
known = "TATARHACK"
recovered_key = ""
for i, c in enumerate(known):
    recovered_key += chr(cipher[i] ^ ord(c))
print(f"Recovered key pattern: {recovered_key}")

# Расшифровка с найденным ключом
def xor_decrypt(cipher, key):
    plaintext = ""
    for i, b in enumerate(cipher):
        plaintext += chr(b ^ ord(key[i % len(key)]))
    return plaintext

decrypted = xor_decrypt(cipher, "KEY")
print(f"Decrypted: {decrypted}")
