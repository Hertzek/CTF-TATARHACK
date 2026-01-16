#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Флаг
const char *FLAG = "TATARHACK{buff3r_0v3rfl0w_b4s1cs}";

int main() {
    // Отключаем буферизацию для корректной работы через сеть
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    
    // УЯЗВИМАЯ СТРУКТУРА!
    // Переменные расположены последовательно в памяти
    char buffer[32];    // Буфер для ввода
    int is_admin = 0;   // Флаг администратора (после буфера в памяти!)
    
    printf("=== Система авторизации v1.0 ===\n");
    printf("Буфер для ввода: 32 байта\n");
    printf("Переменная is_admin = %d\n\n", is_admin);
    
    printf("Введите ваше имя: ");
    
    // УЯЗВИМОСТЬ: gets() не проверяет размер ввода!
    // Если ввести больше 32 символов, перезапишем is_admin
    gets(buffer);
    
    printf("\nПривет, %s!\n", buffer);
    printf("Значение is_admin после ввода: %d\n\n", is_admin);
    
    // Проверка "прав администратора"
    if (is_admin != 0) {
        printf("🎉 Вы каким-то образом стали администратором!\n");
        printf("🏴 Флаг: %s\n", FLAG);
    } else {
        printf("❌ Вы обычный пользователь.\n");
        printf("💡 Подсказка: что если ввести очень длинное имя?\n");
    }
    
    return 0;
}
