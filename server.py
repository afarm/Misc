from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Разбираем URL и параметры запроса
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Логируем параметры в файл
        with open("queries.log", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - {self.client_address[0]} - {query_params}\n")

        # Отправляем ответ
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Query parameters received and logged.")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
