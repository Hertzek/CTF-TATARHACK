# Challenge 5: Caesar Cipher

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Шифр Цезаря |
| **Категория** | Crypto |
| **Сложность** | Easy |
| **Очки** | 100 |
| **Флаг** | `TATARHACK{c43s4r_w4s_h3r3}` |
| **Сдвиг** | 3 |

## Описание для участников

> Юлий Цезарь использовал простой шифр для секретных сообщений.
> Мы перехватили зашифрованное сообщение. Расшифруй его!
>
> Зашифрованный текст: `WDWDUKDFN{f43v4u_z4v_k3u3}`

## Подсказки

1. Шифр Цезаря — это сдвиг букв на определённое число позиций
2. Флаг начинается с TATARHACK
3. Сдвиг небольшой (1-5)

## Способ решения

### Метод 1: Ручной подбор
T → W = сдвиг 3
Значит нужно сдвинуть обратно на 3

### Метод 2: Python
```python
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

encrypted = "WDWDUKDFN{f43v4u_z4v_k3u3}"
for shift in range(26):
    decrypted = caesar_decrypt(encrypted, shift)
    if "TATARHACK" in decrypted:
        print(f"Shift {shift}: {decrypted}")
```

### Метод 3: CyberChef
1. Открыть CyberChef
2. Добавить операцию "ROT13" или "Caesar Cipher Decode"
3. Подобрать сдвиг

## Образовательная цель

Познакомить с классическим шифром подстановки.
Показать, почему простые шифры легко взламываются.
