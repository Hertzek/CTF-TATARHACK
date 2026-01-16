<!DOCTYPE html>
<html>
<head>
    <title>Загрузчик файлов</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
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
            width: 450px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .upload-form {
            margin: 20px 0;
        }
        input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 2px dashed #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #fa709a;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #e65c87;
        }
        .message {
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        .success {
            background: #d4edda;
            color: #155724;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
        }
        .info {
            font-size: 12px;
            color: #888;
            text-align: center;
            margin-top: 20px;
        }
        a {
            color: #fa709a;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📁 Загрузчик файлов</h1>
        <p>Загрузите ваш файл. Мы принимаем любые файлы!</p>
        
        <form class="upload-form" method="POST" enctype="multipart/form-data" action="">
            <input type="file" name="file" required>
            <button type="submit">Загрузить</button>
        </form>

        <?php
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
            $uploadDir = '/var/www/html/uploads/';
            $fileName = basename($_FILES['file']['name']);
            $targetPath = $uploadDir . $fileName;
            
            // "Проверка" безопасности (намеренно слабая)
            $forbidden = ['exe', 'sh', 'bat'];
            $ext = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
            
            if (in_array($ext, $forbidden)) {
                echo '<div class="message error">❌ Этот тип файла запрещён!</div>';
            } else if (move_uploaded_file($_FILES['file']['tmp_name'], $targetPath)) {
                echo '<div class="message success">';
                echo '✅ Файл успешно загружен!<br>';
                echo 'Путь: <a href="/uploads/' . htmlspecialchars($fileName) . '">/uploads/' . htmlspecialchars($fileName) . '</a>';
                echo '</div>';
            } else {
                echo '<div class="message error">❌ Ошибка при загрузке файла</div>';
            }
        }
        ?>

        <p class="info">
            Подсказка: флаг находится в /flag.txt<br>
            Запрещены только: .exe, .sh, .bat
        </p>
    </div>
</body>
</html>
