from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Читаем HTML-шаблон (всегда contacts.html)
        try:
            with open("contacts.html", "r", encoding="utf-8") as f:
                html = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("404: Файл contacts.html не найден".encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    web_dir = os.path.join(os.path.dirname(__file__), ".")
    os.chdir(web_dir)

    server_address = ("", PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"🚀 Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()