from flask import Flask, render_template_string

app = Flask(__name__)

# Шаблон одной страницы "Контакты"
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta chae="viewport" content="width=device-width, initial-scale=1">
  <title>rset="UTF-8">
  <meta namКонтакты</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { overflow-x: hidden; }
    .sidebar { min-height: 100vh; }
  </style>
</head>
<body>
<div class="container-fluid">
  <div class="row">
    <!-- Боковое меню -->
    <nav class="col-md-2 col-lg-2 d-md-block bg-dark sidebar text-white">
      <div class="d-flex flex-column p-3">
        <a href="#" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
          <span class="fs-4">🅱 Меню</span>
        </a>
        <hr>
        <ul class="nav nav-pills flex-column mb-auto">
          <li class="nav-item"><a href="#" class="nav-link text-white">Главная</a></li>
          <li><a href="#" class="nav-link text-white">Категории</a></li>
          <li><a href="#" class="nav-link text-white">Заказы</a></li>
          <li><a href="#" class="nav-link active text-white">Контакты</a></li>
        </ul>
        <hr>
        <div class="dropdown">
          <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
             id="dropdownUser" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="https://via.placeholder.com/32" alt="" width="32" height="32" class="rounded-circle me-2">
            <strong>Пользователь</strong>
          </a>
          <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser">
            <li><a class="dropdown-item" href="#">Профиль</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Выход</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Контент -->
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="d-flex justify-content-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Контакты</h1>
      </div>

      <div class="row">
        <!-- Форма -->
        <div class="col-md-6">
          <form>
            <div class="mb-3">
              <label for="name" class="form-label">Имя</label>
              <input type="text" class="form-control" id="name" placeholder="Ваше имя">
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Почта</label>
              <div class="input-group">
                <span class="input-group-text">@</span>
                <input type="email" class="form-control" id="email" placeholder="email@example.com">
              </div>
            </div>
            <div class="mb-3">
              <label for="message" class="form-label">Сообщение</label>
              <textarea class="form-control" id="message" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
          </form>
        </div>

        <!-- Текст -->
        <div class="col-md-6">
          <h4 class="fw-bold">Наши контакты</h4>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
            aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
            cillum dolore eu fugiat nulla pariatur.
          </p>
          <p>
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
            est laborum.
          </p>
        </div>
      </div>
    </main>
  </div>
</div>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Один обработчик для любых GET-запросов
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def contacts(path):
    # читаем HTML-шаблон из файла
    with open("templates/contacts.html", encoding="utf-8") as f:
        html_content = f.read()
    return Response(html_content, mimetype="text/html")


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5000)