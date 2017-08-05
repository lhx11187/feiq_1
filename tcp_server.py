import socket
import threading
from data_deal import *
import MainData as md

def send_file(conn):
    """发送文件"""
    while True:
        data = conn.recv(1024)
        if data:
            data = data.decode('gbk')
            data = deal_message(data)            
            print(data['option'])
            filename = deal_option(data['option'])
            if filename:
                with open(filename,'rb') as fout:
                    conn.send(fout.read())
            else:
                print('没有找到文件')
        else:
            break
    conn.close()

def tcp_server():
    """创建tcp服务器"""
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #绑定服务器信息
    tcp_server.bind(('', 2425))
    
    #监听模式
    tcp_server.listen(128)

    #分配任务
    while True:
        conn, addr = tcp_server.accept()
        t1 = threading.Thread(target=send_file, args=(conn, ))
        t1.start()
    tcp_server.close()

def classcify_info(queue):
    """将数据分类"""
    #判断信息是否是下载信息
    while True:
        info = queue.get()
        if hasattr(info,'type'):
            md.download_list.append(info)
        else:
            md.upload_list.append(info)

def build_download_message(queue):
    #组织下载文件的信息
    info = queue.get()
    data = info['data']
    

def get_file():
    """下载文件"""
    #组织获取文件的信息

    #连接服务器发送请求

    #获取文件并保存
