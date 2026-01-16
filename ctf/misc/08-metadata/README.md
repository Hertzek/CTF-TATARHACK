# Challenge 8: Metadata

## Информация для организатора

| Параметр | Значение |
|----------|----------|
| **Название** | Метаданные |
| **Категория** | Misc |
| **Сложность** | Easy |
| **Очки** | 100 |
| **Флаг** | `TATARHACK{m3t4d4t4_1s_3v3rywh3r3}` |

## Описание для участников

> Фотограф прислал нам эту красивую картинку.
> Говорит, что спрятал в ней секретное сообщение.
> Но в самой картинке ничего не видно...
>
> Файл: secret_image.jpg

## Подсказки

1. Изображения хранят не только пиксели
2. Метаданные EXIF содержат много информации
3. Используй exiftool или онлайн-сервис

## Способ решения

### Метод 1: exiftool
```bash
exiftool secret_image.jpg
# или
exiftool secret_image.jpg | grep -i flag
exiftool secret_image.jpg | grep -i comment
```

### Метод 2: Python
```python
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('secret_image.jpg')
exif = img._getexif()
for tag_id, value in exif.items():
    tag = TAGS.get(tag_id, tag_id)
    print(f"{tag}: {value}")
```

### Метод 3: Онлайн
- http://exif.regex.info/exif.cgi
- Загрузить изображение и просмотреть метаданные

## Создание изображения с флагом

```bash
# Создаём тестовое изображение и добавляем EXIF
convert -size 800x600 xc:blue secret_image.jpg
exiftool -Comment="TATARHACK{m3t4d4t4_1s_3v3rywh3r3}" secret_image.jpg
exiftool -UserComment="Flag is hidden in metadata" secret_image.jpg
```

## Образовательная цель

Показать, что файлы содержат скрытую информацию (метаданные).
Научить использовать инструменты для анализа метаданных.
Объяснить важность удаления метаданных перед публикацией.
