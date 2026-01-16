#!/bin/bash
# Скрипт для компиляции всех reverse заданий

echo "Building all reverse challenges..."

cd "$(dirname "$0")"

# Challenge 3: Password Check
echo "[1/5] Building password_check..."
cd 03-password-check
gcc -o password_check password_check.c
cd ..

# Challenge 4: Math Check
echo "[2/5] Building math_check..."
cd 04-math-check
gcc -o math_check math_check.c
cd ..

# Challenge 11: XOR Check
echo "[3/5] Building xor_check..."
cd 11-xor-check
gcc -o xor_check xor_check.c
cd ..

# Challenge 12: Loop Validation
echo "[4/5] Building loop_check..."
cd 12-loop-validation
gcc -o loop_check loop_check.c
cd ..

# Challenge 17: Obfuscated
echo "[5/5] Building obfuscated..."
cd 17-obfuscated
gcc -O0 -o obfuscated obfuscated.c
cd ..

echo ""
echo "All reverse challenges compiled!"
echo ""
echo "Binaries created:"
ls -la */password_check */math_check */xor_check */loop_check */obfuscated 2>/dev/null
