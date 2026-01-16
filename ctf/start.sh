#!/bin/bash
echo "========================================"
echo "  TatarHack CTF - Quick Start"
echo "========================================"
echo ""

echo "[1/2] Starting Docker containers..."
docker-compose up -d

echo ""
echo "[2/2] Waiting for services to start..."
sleep 5

echo ""
echo "========================================"
echo "  Services are running!"
echo "========================================"
echo ""
echo "Web Challenges:"
echo "  - SQL Injection Easy:    http://localhost:5001"
echo "  - Hidden Page:           http://localhost:5002"
echo "  - SQL Blind:             http://localhost:5003"
echo "  - File Upload:           http://localhost:5004"
echo "  - Command Injection:     http://localhost:5005"
echo "  - Robots.txt:            http://localhost:5006"
echo ""
echo "Pwn Challenges:"
echo "  - Buffer Overflow:       nc localhost 5019"
echo ""
echo "========================================"
echo "  To stop: docker-compose down"
echo "========================================"
