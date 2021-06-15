import socket,sys
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.settimeout(2)
try:
    cs.connect(('125.8.8.1',54321))
    msg = cs.recv(512)
    print(msg.decode('utf-8'))
    print('end of program')
except socket.error as e:
    print('..exp1>>',e)
