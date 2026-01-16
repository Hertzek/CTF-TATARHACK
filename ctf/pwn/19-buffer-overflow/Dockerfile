FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    gcc \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /challenge

COPY vuln.c .

# Компилируем с отключенными защитами
RUN gcc -fno-stack-protector -z execstack -no-pie -o vuln vuln.c

# Создаём пользователя для запуска
RUN useradd -m ctf

# Копируем бинарник
RUN chown ctf:ctf vuln && chmod 755 vuln

USER ctf

EXPOSE 9999

# Запускаем через socat
CMD ["socat", "-T60", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./vuln,pty,stderr,setsid,sigint,sane"]
