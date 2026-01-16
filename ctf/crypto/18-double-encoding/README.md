# Challenge 18: Double Encoding

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Двойная защита |
| **Категория** | Crypto |
| **Сложность** | Hard |
| **Очки** | 300 |
| **Флаг** | `TATARHACK{d0ubl3_3nc0d1ng}` |

## Описание для участников

> Сообщение защищено двумя слоями кодирования.
> Сначала XOR, потом Base64. Или наоборот?
>
> Данные: `Gx4AHAYQFgEIAhAWHxU4EwA5EzY5ETc7EzI=`
>
> Ключ XOR: `SEC`

## Подсказки

1. Попробуй оба порядка: Base64→XOR и XOR→Base64
2. Правильный порядок: Base64 decode → XOR decrypt
3. Ключ XOR применяется циклически

## Способ решения

### Python решение
```python
import base64

data = "Gx4AHAYQFgEIAhAWHxU4EwA5EzY5ETc7EzI="
key = "SEC"

# Шаг 1: Base64 decode
decoded = base64.b64decode(data)

# Шаг 2: XOR decrypt
flag = ""
for i, b in enumerate(decoded):
    flag += chr(b ^ ord(key[i % len(key)]))

print(flag)  # TATARHACK{d0ubl3_3nc0d1ng}
```

## Образовательная цель

Показать комбинирование различных методов кодирования.
Научить определять порядок операций.
