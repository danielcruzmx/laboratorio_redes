import SimpleHTTPServer
import SocketServer

PORT = 80

handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",PORT), handler)

print("Despachando por el puerto %s", PORT)

httpd.serve_forever()

