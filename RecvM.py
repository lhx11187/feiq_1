import MainData as md
from data_deal import *
from Message import *

def recv_message():
    """接收信息"""
    new_socket = md.udp_socket.dup()
    while True:
        data,addr = new_socket.recvfrom(512)
        #md.udp_socket.recvfrom(128)
        #发送回复信息
        response_message = format_message(md.MSG_RESPONSE,md.login_user)
        send_message(response_message,addr[0])
        #处理收到的数据
        data = deal_message(data.decode('gbk',errors='ignore'))
        #获得数据中的命令
        command, opt = get_command(data['command'])
        if command == 3:  
            #print('(%s)%s已经在线' % (addr[0],data['login_user']))
            add_to_list(data,addr)
        elif command == 1:
            #print('%s上线' % data['login_user'])
            add_to_list(data,addr)
        elif command == 2:
            #print('%s下线' % data['login_user'])
            delete_from_list(data,addr)
        elif command == 32:
            print('%s发送: %s' % (data['login_user'],data['option']))
        elif command & 0x00f00000 == 0x00200000:
            #0:mao.py:05b5:5982886d:1:
            add_to_download_list(data)
