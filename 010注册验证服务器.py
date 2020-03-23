from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<ss>valid</ss>")

#检查HOSTS配置
host='127.0.0.1 www.sweetscape.com'
fin=open('C:\WINDOWS\system32\drivers\etc\HOSTS','r')
lines=fin.read().split('\n')
fin.close()
if host not in lines:
    fout=open('C:\WINDOWS\system32\drivers\etc\HOSTS','a')
    if lines[-1]!='':
        fout.write('\n')
    fout.write('#屏蔽010editor\n%s\n'%host)
    fout.close()
    print("HOSTS文件已修改")

#启动验证服务器
server = HTTPServer(("127.0.0.1",80), RequestHandler)
print("验证服务器启动")
server.serve_forever()