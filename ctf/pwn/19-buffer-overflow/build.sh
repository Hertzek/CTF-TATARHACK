#!/bin/bash
# Компиляция с отключенными защитами для демонстрации
gcc -fno-stack-protector -z execstack -no-pie -o vuln vuln.c
echo "Compiled: vuln"
echo "Run with: ./vuln"
echo "Or via Docker: docker-compose up buffer-overflow"
