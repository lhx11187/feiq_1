from Add_Dele import *
import MainData as md
import time
from data_deal import deal_message,get_command
import os
import time
import copy


def format_message(command,option):
    """格式化信息"""
    msg_form = "%d:%d:%s:%s:%d:%s"
    md.file_queue['package'] = int(time.time())
    message = msg_form % (1, md.file_queue['package'], md.login_user,
                          md.login_host,command,option)
    return message

def send_message(message,ip):
    """发送信息"""
    try:
        md.udp_socket.sendto(message.encode('gbk'),(ip,md.feiq_port))
    except:
        exit()

def send_online_message():
    """发送上线信息"""
    #获取格式化信息
    message = format_message(md.MSG_ONLINE,md.login_user)
    #发送信息
    send_message(message,md.broadcast_ip)

def send_offline_message():
    """发送下线信息"""
    #获取格式化信息
    message = format_message(md.MSG_OFFLINE,md.login_user)
    #发送消息
    send_message(message,md.broadcast_ip)

def send_chat_message():
    """发送聊天信息"""
    #获取目标ip
    #ip = input('Ip:')
    #通过列表获取ip
    choose = input('Num:')
    #获取要发送的聊天信息
    chat_msg = input('Message:')
    #格式化信息
    message = format_message(md.MSG_SEND,chat_msg)
    #发送信息
    ip = md.user_list[int(choose)]['ip']
    send_message(message,ip)

def build_file_message(file_name):
    """构建文件信息"""
    try:
        file_size = os.path.getsize(file_name)  # 获取文件大小
        file_time = os.path.getctime(file_name)  # 获取文件修改时间
    except:
        print('没有该文件')
    else:
        #创建信息命令
        # 文件序号:文件名:文件大小:修改时间:文件的属性
        option_form = '%d:%s:%x:%x:%x:' 
        option = option_form % (0, file_name, file_size, int(file_time),
                0x00000001)
        command = 0x00200000 | 0x00000020
        option = "\0" + option
        message = format_message(command, option)  # 获取格式化信息

        md.file_queue['file_name'] = file_name
        md.file_queue['discriptor'] = 0
        temp_dict = copy.copy(md.file_queue)
        print(temp_dict,md.file_queue)
        md.main_queue.put(temp_dict)
        md.file_queue.clear()
        return message

def send_file_message(queue):
    """发送文件信息"""
    command = None
    # 通过列表获取ip
    choose = input('Num:')
    # 获取要发送的文件名
    file_name = input('FileName:')
    message = build_file_message(file_name)
    ip = md.user_list[int(choose)]['ip']
    send_message(message, ip)


def display_download_list(queue):
    """展示可下载列表"""
    while True:
        info = queue.get()
        print(info)


