import http.server
import socketserver

port = 2222
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",port),Handler) as httpd:
    print("Server Activ!\nPort: ",port)
    print("http://localhost:2222/")
    httpd.serve_forever()