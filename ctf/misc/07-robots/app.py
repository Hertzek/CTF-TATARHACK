from flask import Flask, render_template_string, Response

app = Flask(__name__)

FLAG = "TATARHACK{r0b0ts_txt_1s_publ1c}"

MAIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Обычный сайт</title>
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
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 500px;
        }
        h1 { color: #333; }
        p { color: #666; }
        .hint {
            color: #999;
            font-size: 12px;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Добро пожаловать!</h1>
        <p>Это обычный сайт. Ничего интересного.</p>
        <p>Мы очень заботимся о том, чтобы поисковые роботы не нашли наши секреты... 🤖</p>
        <p class="hint">Подсказка: где сайты указывают правила для роботов?</p>
    </div>
</body>
</html>
'''

FLAG_PAGE = '''
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
        }
        h1 { color: #333; }
        .flag {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            font-size: 18px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Ты нашёл секрет!</h1>
        <p>robots.txt не защищает страницы — он просто просит роботов не заходить.</p>
        <div class="flag">{{ flag }}</div>
        <p>Урок: никогда не прячь секреты через robots.txt!</p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(MAIN_PAGE)

@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Disallow: /super_secret_flag_page
Disallow: /admin
Disallow: /private

# Пожалуйста, не заходите на /super_secret_flag_page
# Там очень важные данные!
"""
    return Response(content, mimetype='text/plain')

@app.route('/super_secret_flag_page')
def secret():
    return render_template_string(FLAG_PAGE, flag=FLAG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
