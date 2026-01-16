from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask(__name__)

MAIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Ping Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%);
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
            width: 500px;
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
            background: #2c3e50;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #34495e;
        }
        .output {
            background: #1a1a2e;
            color: #00ff00;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            white-space: pre-wrap;
            margin-top: 20px;
            max-height: 300px;
            overflow-y: auto;
        }
        .info {
            font-size: 12px;
            color: #888;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Ping Tool</h1>
        <p>Введите IP-адрес или домен для проверки доступности:</p>
        <form method="POST">
            <input type="text" name="host" placeholder="Например: 127.0.0.1" required>
            <button type="submit">Ping!</button>
        </form>
        {% if output %}
        <div class="output">{{ output }}</div>
        {% endif %}
        <p class="info">
            Инструмент для системных администраторов.<br>
            Версия 1.0 (без проверки ввода 😈)
        </p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    
    if request.method == 'POST':
        host = request.form.get('host', '')
        
        # УЯЗВИМЫЙ КОД - Command Injection!
        # Ввод пользователя напрямую передается в shell
        try:
            cmd = f"ping -c 2 {host}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            output = "Timeout: команда выполнялась слишком долго"
        except Exception as e:
            output = f"Ошибка: {str(e)}"
    
    return render_template_string(MAIN_PAGE, output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
