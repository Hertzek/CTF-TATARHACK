#include <stdio.h>
#include <string.h>

// Флаг, который будет показан при правильном пароле
const char *FLAG = "TATARHACK{str1ngs_4r3_v1s1bl3}";

// Пароль хранится прямо в коде (уязвимость!)
const char *PASSWORD = "secretpass123";

int main() {
    char input[100];
    
    printf("=== Секретная программа ===\n");
    printf("Введите пароль: ");
    
    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Ошибка ввода!\n");
        return 1;
    }
    
    // Убираем символ новой строки
    input[strcspn(input, "\n")] = 0;
    
    // Проверка пароля через strcmp (легко найти через strings/ltrace)
    if (strcmp(input, PASSWORD) == 0) {
        printf("\n✅ Правильный пароль!\n");
        printf("🏴 Флаг: %s\n", FLAG);
    } else {
        printf("\n❌ Неверный пароль. Попробуй ещё!\n");
    }
    
    return 0;
}
