# Инструкция по импорту заданий в CTFd

## Способ 1: Ручной импорт

### 1. Запустите CTFd
```bash
docker run -p 8000:8000 ctfd/ctfd
```

### 2. Начальная настройка
1. Откройте http://localhost:8000
2. Пройдите Setup Wizard
3. Создайте учётную запись администратора

### 3. Добавление заданий
1. Перейдите в Admin Panel → Challenges
2. Нажмите "Create Challenge"
3. Заполните поля из README каждого задания

### Структура задания:
- **Name**: Название
- **Category**: Web / Reverse / Crypto / Pwn / Misc
- **Value**: Очки (100 / 200 / 300)
- **Description**: Описание для участников
- **Type**: Standard
- **State**: Visible
- **Flag**: Флаг в формате TATARHACK{...}

---

## Способ 2: Импорт через JSON

### 1. Используйте CTFd API

```python
import requests
import json

CTFd_URL = "http://localhost:8000"
TOKEN = "your_api_token"  # Получите в Admin → Settings → Access Tokens

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

with open("challenges.json") as f:
    data = json.load(f)

for challenge in data["challenges"]:
    # Создаём задание
    resp = requests.post(
        f"{CTFd_URL}/api/v1/challenges",
        headers=headers,
        json={
            "name": challenge["name"],
            "category": challenge["category"],
            "description": challenge["description"],
            "value": challenge["value"],
            "type": "standard",
            "state": "visible"
        }
    )
    
    if resp.status_code == 200:
        challenge_id = resp.json()["data"]["id"]
        
        # Добавляем флаг
        for flag in challenge["flags"]:
            requests.post(
                f"{CTFd_URL}/api/v1/flags",
                headers=headers,
                json={
                    "challenge_id": challenge_id,
                    "type": flag["type"],
                    "content": flag["content"]
                }
            )
        
        # Добавляем подсказки
        for hint in challenge.get("hints", []):
            requests.post(
                f"{CTFd_URL}/api/v1/hints",
                headers=headers,
                json={
                    "challenge_id": challenge_id,
                    "content": hint["content"],
                    "cost": hint["cost"]
                }
            )
        
        print(f"✓ Created: {challenge['name']}")
    else:
        print(f"✗ Failed: {challenge['name']}")
```

---

## Способ 3: Импорт через плагин

### 1. Установите CTFd-import плагин
```bash
cd CTFd/CTFd/plugins
git clone https://github.com/CTFd/ctfd-import-plugin
```

### 2. Используйте ZIP-архив
1. Создайте ZIP с файлами заданий
2. В Admin Panel → Config → Backup
3. Импортируйте архив

---

## Файлы для раздачи участникам

### Web задания
Не требуют файлов — доступны по URL

### Reverse задания
Раздать скомпилированные бинарники:
- `password_check`
- `math_check`
- `xor_check`
- `loop_check`
- `obfuscated`

### Crypto задания
Раздать текстовые файлы:
- `cipher.txt` (Caesar, XOR, Substitution, Double Encoding)
- `encoded.txt` (Base64)

### Misc задания
- `secret_image.jpg` (Metadata)
- `server.log` (Log Analysis)
- `part1-4.txt`, `hint.txt` (Puzzle)

### Pwn задания
- `vuln.c` (исходный код для изучения)

---

## Настройка хостов

Замените `HOST` в описаниях на реальный адрес сервера:
- Локально: `localhost`
- В сети: IP-адрес сервера

---

## Порядок проведения

1. Запустите docker-compose для web-сервисов
2. Подготовьте файлы для раздачи
3. Импортируйте задания в CTFd
4. Проверьте работу всех сервисов
5. Раздайте участникам доступ к CTFd
