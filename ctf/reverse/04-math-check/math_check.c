#include <stdio.h>

const char *FLAG = "TATARHACK{m4th_1s_3asy}";

int main() {
    int number;
    
    printf("=== Математическая проверка ===\n");
    printf("Введите число: ");
    
    if (scanf("%d", &number) != 1) {
        printf("Ошибка: введите число!\n");
        return 1;
    }
    
    // Простая математическая проверка
    // x * 2 + 10 = 94
    // x = 42
    int result = number * 2 + 10;
    
    if (result == 94) {
        printf("\n✅ Правильно!\n");
        printf("🏴 Флаг: %s\n", FLAG);
    } else {
        printf("\n❌ Неверно! Результат: %d (нужно 94)\n", result);
        printf("Подсказка: x * 2 + 10 = ?\n");
    }
    
    return 0;
}
