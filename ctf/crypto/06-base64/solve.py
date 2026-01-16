import base64

flag = "TATARHACK{b4s364_1s_n0t_3ncrypt10n}"

# Кодирование
encoded = base64.b64encode(flag.encode()).decode()
print(f"Encoded: {encoded}")

# Декодирование
decoded = base64.b64decode(encoded).decode()
print(f"Decoded: {decoded}")
