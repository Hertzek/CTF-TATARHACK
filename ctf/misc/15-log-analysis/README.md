# Challenge 15: Log Analysis

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Анализ логов |
| **Категория** | Misc |
| **Сложность** | Medium |
| **Очки** | 200 |
| **Флаг** | `TATARHACK{l0g_4n4lys1s_sk1lls}` |

## Описание для участников

> Мы получили логи сервера за последний месяц.
> Где-то в них спрятан флаг...
> Логов много, но ты справишься!
>
> Файл: server.log

## Подсказки

1. Используй grep для поиска по файлу
2. Флаг имеет формат TATARHACK{...}
3. `grep -i "tatarhack" server.log`

## Способ решения

```bash
# Способ 1: grep
grep "TATARHACK" server.log

# Способ 2: grep с контекстом
grep -n "TATARHACK" server.log

# Способ 3: Python
with open('server.log') as f:
    for i, line in enumerate(f, 1):
        if 'TATARHACK' in line:
            print(f"Line {i}: {line.strip()}")
```

## Образовательная цель

Научить работать с большими текстовыми файлами.
Познакомить с инструментами поиска (grep, awk, sed).
