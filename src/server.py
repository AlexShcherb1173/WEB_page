from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Получаем длину данных
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")

        # Парсим данные из формы
        parsed_data = urllib.parse.parse_qs(post_data)

        print("\n📩 Получены данные из формы:")
        for key, value in parsed_data.items():
            print(f"{key.capitalize()}: {value[0]}")

        # Возвращаем ответ пользователю
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = "<h2>✅ Спасибо! Данные получены.</h2>"
        self.wfile.write(response.encode("utf-8"))


if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"🚀 Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()