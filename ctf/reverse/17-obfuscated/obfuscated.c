#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char *FLAG = "TATARHACK{0bfusc4t3d}";
const char *REAL_PASSWORD = "hidden_key";

// Бесполезные функции для запутывания
int fake_check_1(int x) {
    int result = 0;
    for (int i = 0; i < 100; i++) {
        result += i * x;
        result ^= 0xDEADBEEF;
    }
    return result;
}

int fake_check_2(const char *s) {
    int sum = 0;
    while (*s) {
        sum += *s++;
        sum *= 31;
    }
    return sum % 1000;
}

void do_nothing(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = arr[i] ^ 0x55 ^ 0x55; // XOR дважды = ничего
    }
}

// Реальная проверка (спрятана среди мусора)
int real_check(const char *input) {
    return strcmp(input, REAL_PASSWORD) == 0;
}

int another_fake(int a, int b) {
    int c = a + b;
    c = c * 2 / 2;  // Бесполезно
    return c - a - b + a + b - c + c;  // = c
}

int main() {
    char input[100];
    int garbage[50];
    
    printf("=== Super Secure Program v3.0 ===\n");
    printf("Введите пароль: ");
    
    if (fgets(input, sizeof(input), stdin) == NULL) {
        return 1;
    }
    input[strcspn(input, "\n")] = 0;
    
    // Куча бесполезных операций
    int x = fake_check_1(42);
    int y = fake_check_2(input);
    int z = another_fake(x, y);
    
    for (int i = 0; i < 50; i++) {
        garbage[i] = rand() % 100;
    }
    do_nothing(garbage, 50);
    
    // Ещё мусор
    volatile int temp = 0;
    for (int i = 0; i < 1000; i++) {
        temp += i;
        temp -= i;
    }
    
    // Настоящая проверка!
    if (real_check(input)) {
        printf("\n✅ Доступ разрешён!\n");
        printf("🏴 Флаг: %s\n", FLAG);
    } else {
        // Мусорные вычисления перед выводом
        x = x ^ y ^ z;
        printf("\n❌ Доступ запрещён! [код ошибки: %d]\n", x % 100);
    }
    
    return 0;
}
