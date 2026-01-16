from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

FLAG = "TATARHACK{bl1nd_sql_1s_sl0w_but_w0rks}"

def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)''')
    c.execute('''CREATE TABLE secrets (id INTEGER PRIMARY KEY, flag TEXT)''')
    c.execute("INSERT INTO users (username) VALUES ('admin')")
    c.execute("INSERT INTO users (username) VALUES ('user')")
    c.execute("INSERT INTO users (username) VALUES ('guest')")
    c.execute(f"INSERT INTO secrets (flag) VALUES ('{FLAG}')")
    conn.commit()
    return conn

MAIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Проверка пользователя</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        input[type="text"] {
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
            background: #4facfe;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #3d9ae8;
        }
        .result {
            text-align: center;
            padding: 15px;
            margin-top: 20px;
            border-radius: 5px;
        }
        .exists {
            background: #d4edda;
            color: #155724;
        }
        .not-exists {
            background: #f8d7da;
            color: #721c24;
        }
        .info {
            font-size: 12px;
            color: #888;
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Проверка пользователя</h1>
        <p>Введите имя пользователя для проверки:</p>
        <form method="POST" action="/check">
            <input type="text" name="username" placeholder="Имя пользователя" required>
            <button type="submit">Проверить</button>
        </form>
        {% if result is not none %}
        <div class="result {{ 'exists' if result else 'not-exists' }}">
            {% if result %}
            ✅ Пользователь существует
            {% else %}
            ❌ Пользователь не найден
            {% endif %}
        </div>
        {% endif %}
        <p class="info">
            Подсказка: флаг хранится в таблице <code>secrets</code>, колонка <code>flag</code>
        </p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(MAIN_PAGE, result=None)

@app.route('/check', methods=['POST'])
def check():
    username = request.form.get('username', '')
    
    conn = init_db()
    cursor = conn.cursor()
    
    # УЯЗВИМЫЙ КОД - Blind SQL Injection!
    query = f"SELECT * FROM users WHERE username='{username}'"
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        exists = result is not None
    except Exception as e:
        exists = False
    finally:
        conn.close()
    
    return render_template_string(MAIN_PAGE, result=exists)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
