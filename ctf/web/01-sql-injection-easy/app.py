from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

FLAG = "TATARHACK{sql_1nj3ct10n_1s_d4ng3r0us}"

# Создаем базу данных в памяти
def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecretpassword123')")
    c.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
    conn.commit()
    return conn

# Глобальное соединение (для простоты)
db_conn = None

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Школьная библиотека - Вход</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            width: 350px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #667eea;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: #5a6fd6;
        }
        .error {
            color: red;
            text-align: center;
            margin-top: 15px;
        }
        .success {
            color: green;
            text-align: center;
            margin-top: 15px;
            font-weight: bold;
            word-break: break-all;
        }
        .hint {
            color: #888;
            font-size: 12px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h1>📚 Библиотека</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Логин" required>
            <input type="password" name="password" placeholder="Пароль" required>
            <button type="submit">Войти</button>
        </form>
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}
        {% if flag %}
        <p class="success">🎉 Добро пожаловать, admin!<br>Ваш секрет: {{ flag }}</p>
        {% endif %}
        <p class="hint">Подсказка: иногда ввод пользователя может быть опасен...</p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    global db_conn
    error = None
    flag = None
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Пересоздаем БД для каждого запроса (изоляция)
        db_conn = init_db()
        
        # УЯЗВИМЫЙ КОД - SQL Injection!
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        
        try:
            cursor = db_conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            
            if result:
                flag = FLAG
            else:
                error = "Неверный логин или пароль"
        except Exception as e:
            error = f"Ошибка базы данных: {str(e)}"
        finally:
            db_conn.close()
    
    return render_template_string(LOGIN_PAGE, error=error, flag=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
