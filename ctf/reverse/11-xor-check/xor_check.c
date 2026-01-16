#include <stdio.h>
#include <string.h>

// "TATARHACK{x0r_r3v3rs3}" XOR 0x42
unsigned char encrypted[] = {
    0x16, 0x03, 0x16, 0x03, 0x30, 0x2a, 0x03, 0x21, 0x29, 0x39,
    0x3a, 0x72, 0x30, 0x74, 0x30, 0x77, 0x33, 0x31, 0x77, 0x3d, 0x7d
};

const char *FLAG = "TATARHACK{x0r_r3v3rs3}";
const unsigned char XOR_KEY = 0x42;

int check_password(const char *input) {
    size_t len = strlen(input);
    
    if (len != sizeof(encrypted)) {
        return 0;
    }
    
    for (size_t i = 0; i < len; i++) {
        if ((input[i] ^ XOR_KEY) != encrypted[i]) {
            return 0;
        }
    }
    
    return 1;
}

int main() {
    char input[100];
    
    printf("=== XOR Password Check ===\n");
    printf("Введите пароль: ");
    
    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Ошибка ввода!\n");
        return 1;
    }
    
    input[strcspn(input, "\n")] = 0;
    
    if (check_password(input)) {
        printf("\n✅ Правильно!\n");
        printf("🏴 Флаг: %s\n", FLAG);
    } else {
        printf("\n❌ Неверный пароль!\n");
        printf("Подсказка: изучи как работает XOR\n");
    }
    
    return 0;
}
