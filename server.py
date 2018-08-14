import BaseHTTPServer
import os
import shutil
import time

class handle(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(s):
		if s.path == '/':
			s.path = '/primer.html'
		try:
			file_to_open = open(self.path[1:]).read()
			s.send_response(200)
		except:
			file_to_open = 'file not found'
			s.send_response(404)
		
		s.end_headers()

		with open('/home/oriol/game' + s.path, 'r') as file:
			s.wfile.write(file.read())
	def do_POST(s):
		print s.path
		adr, cli = s.client_address
		print adr + ' ' + str(cli)
		s.send_response(200)
		s.wfile.write('Holahola')
if __name__ == '__main__':

	HOST = '192.168.1.50'
	PORT = 8000
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST,PORT), handle)
	print time.asctime(), "Server Starts - %s:%s" % (HOST,PORT)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % (HOST,PORT)

