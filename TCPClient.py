import socket
from struct import pack
import foo_pb2
import sys

HOST, PORT = "localhost", 9999
data = foo_pb2.Person()
data.name = "client msg"
data.id = 30

print(data.__str__)
encoded = data.SerializeToString()
new_data = foo_pb2.Person()
# new_data.ParseFromString(encoded)
# print(new_data)
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(encoded)

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     {}".format(encoded))
print("Received: {}".format(received))

# HOST, PORT = "localhost", 9999
#
# sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#
# try:
#     sock.connect((HOST, PORT))
#     msg = foo_pb2.Person()
#     msg.name = "client msg"
#     msg.id = 30
#     encoded = msg.SerializeToString()
#     x = pack('>I', len(encoded))
#     sock.sendall(x)
#     sock.sendall(encoded)
#
# finally:
#     sock.close()
#
# print("Sent:     {}").format(encoded)