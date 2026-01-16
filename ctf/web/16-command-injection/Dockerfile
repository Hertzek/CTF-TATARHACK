FROM python:3.9-slim

RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаем флаг
RUN echo "TATARHACK{c0mm4nd_1nj3ct10n_1s_cr1t1c4l}" > /flag.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
