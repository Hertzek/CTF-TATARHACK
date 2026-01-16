#!/usr/bin/env python3
"""
Скрипт для создания изображения с флагом в метаданных.
Требует: pip install Pillow piexif
"""

from PIL import Image
import piexif
import io

FLAG = "TATARHACK{m3t4d4t4_1s_3v3rywh3r3}"

def create_image_with_metadata():
    # Создаём простое изображение
    img = Image.new('RGB', (800, 600), color='#4a90d9')
    
    # Добавляем текст (опционально)
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    draw.text((200, 250), "Nothing to see here...", fill='white', font=font)
    draw.text((250, 300), "Or is there? 🤔", fill='white', font=font)
    
    # Создаём EXIF данные с флагом
    exif_dict = {
        "0th": {
            piexif.ImageIFD.ImageDescription: "Just a normal image",
            piexif.ImageIFD.Make: "CTF Camera",
            piexif.ImageIFD.Model: "TatarHack 2026",
            piexif.ImageIFD.Software: "Python PIL",
            piexif.ImageIFD.Artist: "CTF Player",
            piexif.ImageIFD.Copyright: FLAG,  # Флаг в Copyright!
        },
        "Exif": {
            piexif.ExifIFD.UserComment: f"Secret: {FLAG}".encode('utf-8'),
            piexif.ExifIFD.DateTimeOriginal: "2026:01:16 12:00:00",
        },
        "GPS": {},
        "1st": {},
        "thumbnail": None
    }
    
    exif_bytes = piexif.dump(exif_dict)
    
    # Сохраняем
    img.save("secret_image.jpg", "JPEG", exif=exif_bytes, quality=95)
    print(f"Created: secret_image.jpg")
    print(f"Flag hidden in: Copyright and UserComment EXIF fields")
    print(f"\nTo verify, run: exiftool secret_image.jpg")

if __name__ == "__main__":
    try:
        create_image_with_metadata()
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install Pillow piexif")
        
        # Создаём placeholder файл с инструкциями
        with open("secret_image.txt", "w") as f:
            f.write(f"""
Для создания изображения с метаданными:

1. Установите зависимости:
   pip install Pillow piexif

2. Запустите этот скрипт:
   python create_image.py

Или создайте изображение вручную:
   convert -size 800x600 xc:blue secret_image.jpg
   exiftool -Comment="{FLAG}" secret_image.jpg
   exiftool -Copyright="{FLAG}" secret_image.jpg

Флаг: {FLAG}
""")
        print("Created: secret_image.txt with instructions")
