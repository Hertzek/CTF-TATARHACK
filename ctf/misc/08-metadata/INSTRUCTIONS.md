# Инструкции для этого задания

Флаг: TATARHACK{m3t4d4t4_1s_3v3rywh3r3}

## Создание изображения

### Способ 1: Python (требует pillow и piexif)
```bash
pip install Pillow piexif
python create_image.py
```

### Способ 2: ImageMagick + exiftool
```bash
convert -size 800x600 xc:blue -font Arial -pointsize 40 \
    -fill white -gravity center -annotate 0 "Nothing to see here..." \
    secret_image.jpg

exiftool -Copyright="TATARHACK{m3t4d4t4_1s_3v3rywh3r3}" secret_image.jpg
exiftool -UserComment="Secret: TATARHACK{m3t4d4t4_1s_3v3rywh3r3}" secret_image.jpg
```

### Способ 3: Любое фото + exiftool
```bash
exiftool -Copyright="TATARHACK{m3t4d4t4_1s_3v3rywh3r3}" any_photo.jpg
```

## Раздача участникам

Участникам выдаётся только файл `secret_image.jpg`
