#0.01
import uuid
import os
import socket
import asyncore

topology = []

class Bot(asyncore.dispatcher):

	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		
		self.uuid = uuid.uuid4()

		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)
		
	def handle_read(self, sock):
		print self.uuid
		data = sock.recv(8192)
		if data:
			sock.send(data)
	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print 'Incoming connection from %s' % repr(addr)
			handler = self.handle_read(sock)


server = Bot("localhost", 8888)
asyncore.loop()
