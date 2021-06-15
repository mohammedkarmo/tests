import socket
ssocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ssocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
print('.....server waiting for udp connection')
ssocket.bind(('localhost',54321))
while True :
    data, addr = ssocket.recvfrom(4096)
    print(repr(data))
    ssocket.sendto( resp.encode('utf-8'),addr)
    resp = "...this data from udp server"
