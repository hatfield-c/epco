
import time
import traceback
import socket
#import queue
#import threading
#import json

import CONFIG

class EpcListener:

	LISTENING = False

	def __init__(self, timeout):

		self.timeout = timeout

		self.unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.unitySocket.setblocking(False)

		toSumoAddress = (
			CONFIG.ip_addr,
			int(CONFIG.port)
		)

		self.unitySocket.bind(toSumoAddress)

		#self.messageQueue = queue.SimpleQueue()

		#self.readStreamThread = None
		self.listenSocket = None
		self.listenAddress = None

	def startListening(self):
		self.connectToUnityServer()

		self.listen()

		#self.readStreamThread = threading.Thread(
		#	target = self.listen
		#)
		#self.readStreamThread.start()

		#initMessage = self.messageQueue.get(True)
		#sumoManager.processMessage(initMessage)

	def connectToUnityServer(self):
		print("Connecting to Unity...")

		self.unitySocket.listen(1)

		stopWatch = time.time()
		trying = True

		while trying:
			if time.time() - stopWatch > self.timeout:
				print("[ERROR] Connection timed out!")
				exit()
			
			try:
				tmpSocket, tmpAddress = self.unitySocket.accept()
				tmpSocket.setblocking(False)
				trying = False

				print("Connection accepted!")

			except BlockingIOError:
				pass

			except Exception as exception:
				traceback.print_exc()
				print(exception)
				print("[ERROR] Error occured while trying to make connection to Unity Listener.")
				exit()
				
		self.listenSocket = tmpSocket
		self.listenAddress = tmpAddress

	def listen(self):

		buffer = ""
		while True:
			try:
				buffer += self.listenSocket.recv(1024).decode("utf-8")
				
				delimIndex = buffer.find("\n")

				while delimIndex > 0:
					message = buffer[0 : delimIndex]

					if delimIndex != len(buffer) - 1:
						buffer = buffer[delimIndex + 1 : ]
					else:
						buffer = ""

					#self.messageQueue.put(message)
					print(message)

					delimIndex = buffer.find("\n")

			except BlockingIOError:
				pass

			except Exception as exception:
				self.unitySocket.close()

				traceback.print_exc()
				print(exception)
				print("[ERROR] Error occured while trying to receive client name.")
				exit()

test = EpcListener(30)
test.startListening()