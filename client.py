import os
import socket
import time


serverName = '10.0.2.2'
serverPort = 12200
packetLossArr = [1,5,10,15,20]
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def transfer(cmd,n,latency,pkloss):
	print cmd
	os.system(cmd)
	ts_ms = 0
	recv_ts_ms = 0 
	
	total = 0
	sentence = 'a'*1024*1024*5
	loop = 2

	# for x in xrange(1,loop):
	# 	recvSentence = 0
	# 	ts_ms= time.time()
	# 	clientSocket.sendall(sentence)
	# 	while recvSentence < len(sentence):
	# 		recvSentence += len(clientSocket.recv(1024))

	# 	recv_ts_ms = time.time()

	# 	rtt_ms= recv_ts_ms-ts_ms
	# 	total += rtt_ms
	# ave = total / loop
	recvSentence = 0
	ts_ms= time.time()
	clientSocket.sendall(sentence)
	while recvSentence < len(sentence):
		recvSentence += len(clientSocket.recv(1024))

	recv_ts_ms = time.time()

	rtt_ms= recv_ts_ms-ts_ms
	# th = recvSentence*8/1e6/(ave/2)
	th = recvSentence/1e6/(rtt_ms/2)


	f = open("data.txt", "a")	

	# latency th loss
	f.write(str(latency)+" "+str(th)+" "+str(pkloss)+"\n")
	f.close()
def main():

	#3 latency, 1ms,10ms,100ms

	latencyArr = [1,10,100,500,1000]
	
	
	
	for x in xrange(0,len(latencyArr)):
		n = 0
		os.system("tc qdisc del dev eth2 root")
		os.system("tc qdisc add dev eth2 root handle 1: tbf rate 175mbps burst 50kbit latency 400")
		for y in xrange(0,len(packetLossArr)+1):
			if n ==0 :
				cmd = "tc qdisc add dev eth2 parent 1: handle 2: netem delay "+str(latencyArr[x])+"ms"
				
				#cmd = "tc qdisc add dev eth2 root netem latency 10ms loss "+str(packetLossArr[y]*100)+"%"
				print "latency: "+str(latencyArr[x])+". packet loss: 0"
				transfer(cmd,n,latencyArr[x],0)
				n = 1

			else:
				#cmdTh = "tc qdisc replace dev eth2 parent 1: handle 2: tbf rate 100mbit burst 32kbit latency 10ms"
				cmd = "tc qdisc replace dev eth2 parent 1: handle 2: netem delay "+str(latencyArr[x])+"ms loss "+str(packetLossArr[y-1])+"%"
				#cmd = "tc qdisc replace dev eth2 root netem latency 10ms loss "+str(packetLossArr[y]*100)+"%"
				print "latency: "+str(latencyArr[x])+". packet loss:"+str(packetLossArr[y-1])
				transfer(cmd,n,latencyArr[x],packetLossArr[y-1])	

	

if __name__== "__main__":
  
  main()
