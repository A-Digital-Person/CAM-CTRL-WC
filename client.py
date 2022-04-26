import socket
import threading

def get(s):
    while True:
        tm = s.recv(1024)
        print("\nReceived: ",tm.decode('ascii'))

def set_(s):
    while True:
        i=input("\nEnter : ")
        s.send(i.encode('ascii'))

s = socket.socket()
host = socket.gethostname()
port = 9981
s.connect((host,port))
t1=threading.Thread( target = get ,  args = (s,) )
t2=threading.Thread( target = set_ , args = (s,) )
t1.start()
t2.start()
