from flask import Flask, render_template_string

app = Flask(__name__)

FLAG = "TATARHACK{h1dd3n_p4g3s_4r3_n0t_s3cur3}"

MAIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Добро пожаловать!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
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
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
            line-height: 1.6;
        }
        .hint {
            color: #999;
            font-size: 12px;
            margin-top: 30px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Добро пожаловать на наш сайт!</h1>
        <p>Это обычный сайт. Здесь нет ничего интересного.</p>
        <p>Или есть? 🤔</p>
        <p class="hint">Подсказка: иногда самое интересное спрятано там, куда не ведут ссылки...</p>
    </div>
</body>
</html>
'''

SECRET_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Секретная страница</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #333;
        }
        .flag {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            font-size: 18px;
            word-break: break-all;
            margin: 20px 0;
        }
        .congrats {
            color: #e91e63;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Ты нашёл секретную страницу!</h1>
        <p class="congrats">Поздравляем!</p>
        <p>Вот твой флаг:</p>
        <div class="flag">{{ flag }}</div>
        <p>Урок: скрытые страницы без авторизации — это не защита!</p>
    </div>
</body>
</html>
'''

NOT_FOUND_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>404 - Не найдено</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #333;
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .container {
            text-align: center;
        }
        h1 {
            font-size: 72px;
            margin: 0;
        }
        p {
            color: #999;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>Страница не найдена. Но может быть, ты ищешь что-то другое?</p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(MAIN_PAGE)

@app.route('/secret')
def secret():
    return render_template_string(SECRET_PAGE, flag=FLAG)

@app.errorhandler(404)
def not_found(e):
    return render_template_string(NOT_FOUND_PAGE), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
