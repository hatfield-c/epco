
import time
import traceback
import socket

import CONFIG

class EpcoManager:

	LISTENING = False

	def __init__(self, timeout):

		self.timeout = timeout

		self.unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.python_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.unity_socket.setblocking(False)
		self.python_socket.setblocking(False)

		to_unity_address = (
			CONFIG.ip_addr,
			int(CONFIG.to_unity_port)
		)
		
		to_python_address = (
			CONFIG.ip_addr,
			int(CONFIG.to_python_port)
		)

		self.unity_socket.bind(to_unity_address)
		self.python_socket.bind(to_python_address)
		
		self.read_stream = None
		self.read_address = None
		
		self.write_stream = None
		self.write_address = None

	def inference(self):
		self.connect_read()
		self.connect_write()
		
		self.listen()

	def connect_read(self):
		print("Connecting to read Unity...")

		self.python_socket.listen(1)

		stopWatch = time.time()
		trying = True

		while trying:
			if time.time() - stopWatch > self.timeout:
				print("    [ERROR] Connection timed out!\n")
				exit()
			
			try:
				tmp_stream, tmp_address = self.python_socket.accept()
				tmp_stream.setblocking(False)
				trying = False

				print("    Connection accepted!")

			except BlockingIOError:
				pass

			except Exception as exception:
				traceback.print_exc()
				print(exception)
				print("\n[ERROR] Error occured while trying to make connection to Unity Listener.")
				exit()
				
		self.read_stream = tmp_stream
		self.read_address = tmp_address
		
	def connect_write(self):
		print("Connecting to write Unity...")

		self.unity_socket.listen(1)

		stopWatch = time.time()
		trying = True

		while trying:
			if time.time() - stopWatch > self.timeout:
				print("    [ERROR] Connection timed out!")
				exit()
			
			try:
				tmp_stream, tmp_address = self.unity_socket.accept()
				tmp_stream.setblocking(False)
				trying = False

				print("    Connection accepted!")

			except BlockingIOError:
				pass

			except Exception as exception:
				traceback.print_exc()
				print(exception)
				print("\n[ERROR] Error occured while trying to make connection to Unity Listener.")
				exit()
				
		self.write_stream = tmp_stream
		self.write_address = tmp_address

	def listen(self):
		print("\n")
		
		buffer = ""
		while True:
			try:
				buffer += self.read_stream.recv(1024).decode("utf-8")
				
				delimIndex = buffer.find("\n")

				while delimIndex > 0:
					message = buffer[0 : delimIndex]

					if delimIndex != len(buffer) - 1:
						buffer = buffer[delimIndex + 1 : ]
					else:
						buffer = ""

					print("[MSG] " + message)

					delimIndex = buffer.find("\n")
					
					self.respond()

			except BlockingIOError:
				pass

			except Exception as exception:
				self.read_stream.close()

				traceback.print_exc()
				print(exception)
				print("\n[ERROR] Error occured while trying to receive client name.")
				exit()

	def respond(self):
		message = "Query received. Here is the response.\n"
		
		self.write_stream.send(message.encode())