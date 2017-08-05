

import socket
import MainData as md

def create_socket():
    md.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    md.udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    md.udp_socket.bind(('',2425))
    md.udp_socket.settimeout(1000)


