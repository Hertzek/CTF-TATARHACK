# Challenge 13: XOR Cipher

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | XOR Шифр |
| **Категория** | Crypto |
| **Сложность** | Medium |
| **Очки** | 200 |
| **Флаг** | `TATARHACK{x0r_1s_r3v3rs1bl3}` |
| **Ключ** | `KEY` |

## Описание для участников

> Сообщение зашифровано с помощью XOR.
> Ключ короткий и повторяется.
> Ты знаешь, что флаг начинается с "TATARHACK"
>
> Зашифрованные байты (hex):
> `1f0016000c0a1c050a0c160f350e02760f32700135083b193b04`

## Подсказки

1. XOR с одним и тем же ключом даёт исходный текст
2. Если знаешь часть открытого текста, можно найти ключ
3. TATARHACK XOR cipher = KEY (повторяющийся)

## Способ решения

### Python решение
```python
cipher_hex = "1f0016000c0a1c050a0c160f350e02760f32700135083b193b04"
cipher = bytes.fromhex(cipher_hex)

# Известно: флаг начинается с TATARHACK
known = "TATARHACK"

# Находим ключ
key = ""
for i, c in enumerate(known):
    key += chr(cipher[i] ^ ord(c))
print(f"Key pattern: {key}")  # KEYKEYKEY...

# Ключ = "KEY"
key = "KEY"
plaintext = ""
for i, b in enumerate(cipher):
    plaintext += chr(b ^ ord(key[i % len(key)]))
print(plaintext)
```

## Образовательная цель

Показать атаку на XOR с известным открытым текстом (known-plaintext attack).
Объяснить слабости повторяющегося ключа.
