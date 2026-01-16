# Генерация и решение Substitution cipher

flag = "TATARHACK{subst1tut10n_c1ph3r}"

# Таблица подстановки
substitution = {
    'A': 'Z', 'B': 'J', 'C': 'F', 'E': '3', 'H': 'X', 
    'I': '1', 'K': 'P', 'N': 'G', 'O': '0', 'P': 'S',
    'R': 'K', 'S': 'W', 'T': 'Z', 'U': 'Q',
    '_': '_', '{': '{', '}': '}'
}

# Шифрование
cipher = ''.join(substitution.get(c.upper(), c) for c in flag)
print(f"Cipher: {cipher}")

# Обратная таблица
reverse = {v: k for k, v in substitution.items()}

# Расшифровка
plaintext = ''.join(reverse.get(c, c).lower() if c.islower() else reverse.get(c, c) for c in cipher)
print(f"Plaintext: {plaintext}")
