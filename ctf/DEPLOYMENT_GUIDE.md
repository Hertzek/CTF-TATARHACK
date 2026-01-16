# 🚀 Руководство по развёртыванию CTF на Debian VM с CTFd

## Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    Debian VM (CTFd сервер)                  │
│                                                             │
│  ┌─────────────┐    ┌─────────────────────────────────────┐│
│  │   CTFd      │    │      CTF Challenges (Docker)        ││
│  │  :8000      │    │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   ││
│  │             │    │  │:5001│ │:5002│ │:5003│ │...  │   ││
│  └─────────────┘    │  └─────┘ └─────┘ └─────┘ └─────┘   ││
│                     └─────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Network
                              ▼
                    ┌─────────────────┐
                    │   Участники     │
                    │  (браузеры)     │
                    └─────────────────┘
```

---

## Вариант 1: Запустить задания на той же Debian VM

### Шаг 1: Установка Docker на Debian

```bash
# Обновляем систему
sudo apt update && sudo apt upgrade -y

# Устанавливаем зависимости
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Добавляем GPG ключ Docker
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Добавляем репозиторий
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Устанавливаем Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Добавляем пользователя в группу docker
sudo usermod -aG docker $USER
newgrp docker

# Проверяем
docker --version
docker compose version
```

### Шаг 2: Копирование файлов на Debian VM

**С Windows (через SCP):**
```powershell
# В PowerShell на Windows
scp -r C:\Users\Ilsaf\source\repos\asm\ctf user@debian-vm-ip:/home/user/
```

**Или через Git:**
```bash
# На Debian VM
git clone <your-repo-url>
cd ctf
```

**Или через WinSCP/FileZilla** — просто скопируйте папку ctf

### Шаг 3: Запуск заданий на Debian

```bash
cd /home/user/ctf
docker compose up -d --build

# Проверка
docker ps
```

### Шаг 4: Настройка CTFd

1. Откройте CTFd Admin Panel
2. Перейдите в **Admin → Challenges**
3. Добавьте задания вручную или через API

**Пример добавления задания:**

| Поле | Значение |
|------|----------|
| Name | Baby SQL |
| Category | Web |
| Value | 100 |
| Description | Мы нашли старую страницу входа...<br><br>http://DEBIAN_VM_IP:5001 |
| Flag | TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us} |

### Шаг 5: Импорт через API (автоматически)

```bash
# На Debian VM
cd /home/user/ctf/ctfd-export

# Получите API токен в CTFd: Admin → Settings → Access Tokens → Generate

# Запустите импорт
python3 import_to_ctfd.py http://localhost:8000 YOUR_API_TOKEN
```

**Важно:** Замените `HOST` в challenges.json на IP вашей VM:

```bash
# Замените HOST на реальный IP
sed -i 's/HOST/192.168.1.100/g' challenges.json
```

---

## Вариант 2: Задания на Windows, CTFd на Debian

### Сетевая конфигурация

1. Узнайте IP вашего Windows компьютера:
```powershell
ipconfig | Select-String "IPv4"
```

2. На Debian в CTFd укажите адреса заданий:
   - `http://WINDOWS_IP:5001` — SQL Injection
   - `http://WINDOWS_IP:5002` — Hidden Page
   - и т.д.

### Настройка Firewall на Windows

```powershell
# Разрешить входящие подключения на порты CTF
New-NetFirewallRule -DisplayName "CTF Challenges" -Direction Inbound -Protocol TCP -LocalPort 5001-5006,5019 -Action Allow
```

### Проверка доступности с Debian

```bash
curl http://WINDOWS_IP:5001
```

---

## Вариант 3: Docker на Windows, доступ из сети

### Настройка Docker Desktop для сетевого доступа

По умолчанию Docker на Windows слушает только localhost. Для доступа из сети:

1. **docker-compose.yml** уже настроен правильно (порты открыты)
2. Нужно только разрешить firewall

```powershell
# PowerShell от администратора
netsh advfirewall firewall add rule name="CTF-5001" dir=in action=allow protocol=TCP localport=5001
netsh advfirewall firewall add rule name="CTF-5002" dir=in action=allow protocol=TCP localport=5002
netsh advfirewall firewall add rule name="CTF-5003" dir=in action=allow protocol=TCP localport=5003
netsh advfirewall firewall add rule name="CTF-5004" dir=in action=allow protocol=TCP localport=5004
netsh advfirewall firewall add rule name="CTF-5005" dir=in action=allow protocol=TCP localport=5005
netsh advfirewall firewall add rule name="CTF-5006" dir=in action=allow protocol=TCP localport=5006
netsh advfirewall firewall add rule name="CTF-5019" dir=in action=allow protocol=TCP localport=5019
```

---

## Настройка заданий в CTFd

### Описания для каждого задания

#### Web Challenges

| # | Название | URL | Очки | Флаг |
|---|----------|-----|------|------|
| 1 | Baby SQL | http://IP:5001 | 100 | `TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us}` |
| 2 | Секретная страница | http://IP:5002 | 100 | `TATARHACK{h1dd3n_p4g3s_4r3_n0t_s3cur3}` |
| 9 | Слепой SQL | http://IP:5003 | 200 | `TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}` |
| 10 | Загрузчик файлов | http://IP:5004 | 200 | `TATARHACK{f1l3_upl04d_1s_d4ng3r0us}` |
| 16 | Пинг-понг | http://IP:5005 | 300 | `TATARHACK{c0mm4nd_1nj3ct10n_1s_cr1t1c4l}` |
| 7 | Роботы | http://IP:5006 | 100 | `TATARHACK{r0b0ts_txt_1s_publ1c}` |

#### Pwn Challenges

| # | Название | Подключение | Очки | Флаг |
|---|----------|-------------|------|------|
| 19 | Переполнение буфера | `nc IP 5019` | 300 | `TATARHACK{buff3r_0v3rfl0w_b4s1cs}` |

#### Файлы для скачивания

Загрузите в CTFd как файлы заданий:

**Reverse:**
- `reverse/03-password-check/password_check` (нужно скомпилировать)
- `reverse/04-math-check/math_check`
- `reverse/11-xor-check/xor_check`
- `reverse/12-loop-validation/loop_check`
- `reverse/17-obfuscated/obfuscated`

**Crypto:**
- `crypto/05-caesar/cipher.txt`
- `crypto/06-base64/encoded.txt`
- `crypto/13-xor-cipher/cipher.txt`
- `crypto/14-substitution/cipher.txt`
- `crypto/18-double-encoding/cipher.txt`

**Misc:**
- `misc/08-metadata/secret_image.jpg` (нужно создать)
- `misc/15-log-analysis/server.log`
- `misc/20-puzzle/` (все файлы: part1-4.txt, hint.txt)

---

## Скрипт автоматической настройки для Debian

Создайте файл `setup_debian.sh`:

```bash
#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}=== TatarHack CTF Setup ===${NC}"

# 1. Проверка Docker
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
fi

# 2. Запуск контейнеров
echo "Starting CTF challenges..."
cd /home/$USER/ctf
docker compose up -d --build

# 3. Проверка
echo ""
echo -e "${GREEN}=== Status ===${NC}"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 4. Получение IP
IP=$(hostname -I | awk '{print $1}')
echo ""
echo -e "${GREEN}=== URLs ===${NC}"
echo "SQL Injection:      http://$IP:5001"
echo "Hidden Page:        http://$IP:5002"
echo "SQL Blind:          http://$IP:5003"
echo "File Upload:        http://$IP:5004"
echo "Command Injection:  http://$IP:5005"
echo "Robots.txt:         http://$IP:5006"
echo "Buffer Overflow:    nc $IP 5019"
```

---

## Проверка работоспособности

### На Windows (текущее состояние)

```powershell
# Все сервисы запущены и работают:
# Port 5001 : OK (SQL Injection)
# Port 5002 : OK (Hidden Page)
# Port 5003 : OK (SQL Blind)
# Port 5004 : OK (File Upload)
# Port 5005 : OK (Command Injection)
# Port 5006 : OK (Robots.txt)
```

### Тест SQL Injection

1. Открыть http://localhost:5001
2. Ввести в логин: `' OR 1=1 --`
3. Пароль: любой
4. Получить флаг!

---

## Troubleshooting

### Контейнеры не запускаются

```bash
# Посмотреть логи
docker compose logs

# Перезапустить
docker compose down
docker compose up -d
```

### Порт занят

```bash
# Найти процесс
netstat -tulpn | grep :5001

# Изменить порт в docker-compose.yml
ports:
  - "5101:5000"  # вместо 5001
```

### Нет доступа из сети

1. Проверить firewall
2. Проверить что контейнер слушает 0.0.0.0
3. Проверить маршрутизацию в сети

```bash
# На Debian
sudo ufw allow 5001:5006/tcp
sudo ufw allow 5019/tcp
```
