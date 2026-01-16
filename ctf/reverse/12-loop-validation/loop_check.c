#include <stdio.h>
#include <string.h>

const char *FLAG = "TATARHACK{l00p_ch3ck}";
const char *PASSWORD = "TATARHACK{l00p_ch3ck}";

int check_password(const char *input) {
    size_t expected_len = strlen(PASSWORD);
    
    if (strlen(input) != expected_len) {
        return 0;
    }
    
    // Посимвольная проверка (легко анализируется в декомпиляторе)
    for (size_t i = 0; i < expected_len; i++) {
        if (input[i] != PASSWORD[i]) {
            printf("Ошибка на позиции %zu\n", i);
            return 0;
        }
    }
    
    return 1;
}

int main() {
    char input[100];
    
    printf("=== Loop Validation ===\n");
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
        printf("❌ Неверный пароль!\n");
    }
    
    return 0;
}
