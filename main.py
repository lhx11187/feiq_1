from tcp_server import *
from Message import *
from sock import *
import threading
import MainData as md
from RecvM import *
import multiprocessing

def display_window():
    """功能选项界面"""
    print('{0:>10}'.format('1.上线'))
    print('-'*20)
    print('{0:>10}'.format('2.下线'))
    print('-'*20)
    print('{0:>10}'.format('3.发送消息'))
    print('-'*20)
    print('{0:>10}'.format('4.打印列表'))
    print('-'*20)
    print('{0:>15}'.format('5.send file'))
    print()

def main():
    """主函数"""
    create_socket()
    md.main_queue = multiprocessing.Queue()
    t1 = threading.Thread(target=recv_message)
    t1.start()
    p1 = multiprocessing.Process(target=tcp_server)
    p1.start()
    md.download_queue = multiprocessing.Queue()
    while True:
        display_window()  # 显示选项界面
        option = input('选择:')  # 获取功能选项
        if option == '1':
            send_online_message()
        elif option == '2':
            #下线
            send_offline_message()
        elif option == '3':
            #发送消息
            send_chat_message()
        elif option == '4':
            #打印列表
            for i,value in enumerate(md.user_list):
                print(i,value)
        elif option == '5':
            #发送文件
            send_file_message(md.main_queue)
        elif option == '6':
            #打印可下载文件列表
            display_download_list(md.download_queue)
        else:
            #退出
            send_offline_message()
            break
    md.udp_socket.close()

if __name__ == '__main__':
    main()
