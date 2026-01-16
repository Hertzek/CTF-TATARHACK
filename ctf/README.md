# 🏴‍☠️ TatarHack CTF - Образовательные задания по кибербезопасности

## Описание
Набор из 20 CTF-заданий для детей и подростков (10-16 лет), ориентированных на обучение основам кибербезопасности.

## Формат флагов
Все флаги имеют формат: `TATARHACK{...}`

## Таблица всех заданий

| # | Название | Категория | Сложность | Очки | Флаг |
|---|----------|-----------|-----------|------|------|
| 1 | Baby SQL | Web | Easy | 100 | `TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us}` |
| 2 | Секретная страница | Web | Easy | 100 | `TATARHACK{h1dd3n_p4g3s_4r3_n0t_s3cur3}` |
| 3 | Простой пароль | Reverse | Easy | 100 | `TATARHACK{str1ngs_4r3_v1s1bl3}` |
| 4 | Математика | Reverse | Easy | 100 | `TATARHACK{m4th_1s_3asy}` |
| 5 | Шифр Цезаря | Crypto | Easy | 100 | `TATARHACK{c43s4r_w4s_h3r3}` |
| 6 | Странные символы | Crypto | Easy | 100 | `TATARHACK{b4s364_1s_n0t_3ncrypt10n}` |
| 7 | Роботы | Misc | Easy | 100 | `TATARHACK{r0b0ts_txt_1s_publ1c}` |
| 8 | Метаданные | Misc | Easy | 100 | `TATARHACK{m3t4d4t4_1s_3v3rywh3r3}` |
| 9 | Слепой SQL | Web | Medium | 200 | `TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}` |
| 10 | Загрузчик файлов | Web | Medium | 200 | `TATARHACK{f1l3_upl04d_1s_d4ng3r0us}` |
| 11 | XOR Проверка | Reverse | Medium | 200 | `TATARHACK{x0r_r3v3rs3}` |
| 12 | Посимвольная проверка | Reverse | Medium | 200 | `TATARHACK{l00p_ch3ck}` |
| 13 | XOR Шифр | Crypto | Medium | 200 | `TATARHACK{x0r_1s_r3v3rs1bl3}` |
| 14 | Подстановка | Crypto | Medium | 200 | `TATARHACK{subst1tut10n_c1ph3r}` |
| 15 | Анализ логов | Misc | Medium | 200 | `TATARHACK{l0g_4n4lys1s_sk1lls}` |
| 16 | Пинг-понг | Web | Hard | 300 | `TATARHACK{c0mm4nd_1nj3ct10n_1s_cr1t1c4l}` |
| 17 | Запутанный код | Reverse | Hard | 300 | `TATARHACK{0bfusc4t3d}` |
| 18 | Двойная защита | Crypto | Hard | 300 | `TATARHACK{d0ubl3_3nc0d1ng}` |
| 19 | Переполнение буфера | Pwn | Hard | 300 | `TATARHACK{buff3r_0v3rfl0w_b4s1cs}` |
| 20 | Пазл | Misc | Hard | 300 | `TATARHACK{p1ec3s_t0g3th3r}` |

## Структура проекта

```
ctf/
├── docker-compose.yml      # Запуск всех web-сервисов
├── web/                    # Web-задания
│   ├── 01-sql-injection-easy/
│   ├── 02-hidden-page/
│   ├── 09-sql-blind/
│   ├── 10-file-upload/
│   └── 16-command-injection/
├── reverse/                # Reverse Engineering
│   ├── 03-password-check/
│   ├── 04-math-check/
│   ├── 11-xor-check/
│   ├── 12-loop-validation/
│   └── 17-obfuscated/
├── crypto/                 # Криптография
│   ├── 05-caesar/
│   ├── 06-base64/
│   ├── 13-xor-cipher/
│   ├── 14-substitution/
│   └── 18-double-encoding/
├── pwn/                    # Binary Exploitation
│   └── 19-buffer-overflow/
├── misc/                   # Разное
│   ├── 07-robots/
│   ├── 08-metadata/
│   ├── 15-log-analysis/
│   └── 20-puzzle/
└── ctfd-export/           # Файлы для импорта в CTFd
```

## Быстрый старт

### Требования
- Docker и Docker Compose
- GCC (для компиляции reverse/pwn заданий)
- Python 3.x

### Запуск web-сервисов

```bash
cd ctf
docker-compose up -d
```

После запуска сервисы будут доступны:
- SQL Injection Easy: http://localhost:5001
- Hidden Page: http://localhost:5002
- SQL Blind: http://localhost:5003
- File Upload: http://localhost:5004
- Command Injection: http://localhost:5005
- Robots.txt: http://localhost:5006

### Компиляция reverse заданий

```bash
cd reverse
./build_all.sh
```

### Компиляция pwn заданий

```bash
cd pwn/19-buffer-overflow
./build.sh
```

## Уровни сложности

### Easy (8 заданий) - 100 очков
1. SQL Injection Easy (Web)
2. Hidden Page (Web)
3. Password Check (Reverse)
4. Math Check (Reverse)
5. Caesar Cipher (Crypto)
6. Base64 (Crypto)
7. Robots.txt (Misc)
8. Metadata (Misc)

### Medium (7 заданий) - 200 очков
9. SQL Blind (Web)
10. File Upload (Web)
11. XOR Check (Reverse)
12. Loop Validation (Reverse)
13. XOR Cipher (Crypto)
14. Substitution (Crypto)
15. Log Analysis (Misc)

### Hard (5 заданий) - 300 очков
16. Command Injection (Web)
17. Obfuscated Logic (Reverse)
18. Double Encoding (Crypto)
19. Buffer Overflow (Pwn)
20. Puzzle (Misc)

## Импорт в CTFd

1. Запустите CTFd
2. Зайдите в Admin Panel → Import
3. Загрузите файл `ctfd-export/challenges.json`
4. Или добавьте задания вручную, используя информацию из README каждого задания

## Рекомендуемые инструменты для участников

- **Web**: Браузер, Burp Suite, curl
- **Reverse**: Ghidra, IDA Free, strings, ltrace
- **Crypto**: CyberChef, Python
- **Pwn**: GDB, Python/pwntools
- **Misc**: exiftool, grep, base64

## Безопасность

⚠️ Все задания предназначены ТОЛЬКО для образовательных целей!
- Не используйте полученные знания во вред
- Атакуйте только те системы, на которые у вас есть разрешение
- CTF — это обучение, а не взлом!

## Авторы
Создано для TatarHack CTF 2026

## Лицензия
MIT License - свободное использование в образовательных целях
