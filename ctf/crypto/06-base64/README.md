# Challenge 6: Base64

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Странные символы |
| **Категория** | Crypto |
| **Сложность** | Easy |
| **Очки** | 100 |
| **Флаг** | `TATARHACK{b4s364_1s_n0t_3ncrypt10n}` |

## Описание для участников

> Мы нашли странную строку в конфигурационном файле.
> Похоже, это какая-то кодировка...
>
> `VEFUQVJIQUNLe2I0czM2NF8xc19uMHRfM25jcnlwdDEwbn0=`

## Подсказки

1. Обрати внимание на символы: буквы, цифры, + и /
2. Строка заканчивается на =
3. Это очень популярная кодировка

## Способ решения

### Метод 1: Командная строка
```bash
echo "VEFUQVJIQUNLe2I0czM2NF8xc19uMHRfM25jcnlwdDEwbn0=" | base64 -d
```

### Метод 2: Python
```python
import base64
encoded = "VEFUQVJIQUNLe2I0czM2NF8xc19uMHRfM25jcnlwdDEwbn0="
decoded = base64.b64decode(encoded).decode()
print(decoded)
```

### Метод 3: CyberChef или онлайн-декодер

## Образовательная цель

Показать, что Base64 — это кодировка, а не шифрование.
Объяснить разницу между encoding и encryption.
