import socket
s = socket.socket()
s.connect(('www.google.com', 80))
print("We are connected to %s:%d" % s.getpeername())