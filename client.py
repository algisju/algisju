import socket
#import pickle

HEADER = 64
PORT = 8008
SERVER = "193.191.212.2"
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))

	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))
	
send("YIHAA!")
input()
send("YIHAA!")
send("YIHAA!")
send(DISCONNECT_MESSAGE)
