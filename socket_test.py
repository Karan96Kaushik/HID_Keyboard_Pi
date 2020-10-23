import socket

host_ip, server_port = "cryers.club", 1337
data = "AB"

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# Establish connection to TCP server and exchange data
	tcp_client.connect((host_ip, server_port))
	tcp_client.sendall(data.encode())

	# Read data from the TCP server and close the connection
	received = tcp_client.recv(1024)
	print("Bytes Received: {}".format(received.decode()))

except:
	tcp_client.close()

while True:
	try:
		received = tcp_client.recv(1024)
		print("Bytes Received: {}".format(received.decode()))
	except:
		print("Err")

print("Bytes Sent:     {}".format(data))
