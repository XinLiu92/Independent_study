#!/usr/bin/env python

import socket,errno

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12200        # Port to listen on (non-privileged ports are > 1023)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(1)



total = 0
sumSend = 1048576*5
sentence = ""
while True:
#receive
	print "server ready to receive"
	conn, addr = serverSocket.accept()
	while True:
		data = conn.recv(1024)
		if not data:
			break;
		conn.sendall(data)
		# sumSend  = sumSend - 1024
		# if sumSend == 0:
		# 	break;



	# except socket.error as e:
	# 	if isinstance(e.args,tuple):
	# 		print "errno is %d" % e[0]
	# 		if e[0] == errno.EPIPE:
	# 			print "detected remote disconnect"
	# 		else:
	# 			print "other error"
	# 	else:
	# 		print "socket error: ", e
	# 	conn.close()
	# 	break
	# except IOError as e:
	# 	print "goe IOError: ",e
	# 	break
	