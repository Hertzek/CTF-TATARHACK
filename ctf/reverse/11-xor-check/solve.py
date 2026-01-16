# Скрипт для генерации зашифрованных байтов
flag = "TATARHACK{x0r_r3v3rs3}"
key = 0x42

encrypted = [ord(c) ^ key for c in flag]
print("Encrypted bytes:")
print(", ".join(f"0x{b:02x}" for b in encrypted))

# Проверка расшифровки
decrypted = ''.join(chr(b ^ key) for b in encrypted)
print(f"\nDecrypted: {decrypted}")
