import MainData as md


def deal_option(data):
    """处理文件下载命令"""    
    #598273b3:0:0:
    data = data.split(":")
    package_message = data[0]
    info = md.main_queue.get()
    if info:
        package_id = int(package_message, 16)
        print(package_id,info['package'])
        if package_id == int(info['package']):  # 判断是否包名相同
        return info['file_name']

def deal_message(message):
    """处理信息并格式化"""
    response_msg = message.split(":", 5)
    #将信息按照关键字保存在字典中
    response_dict = dict()
    response_dict['version'] = response_msg[0]
    response_dict['packet_v'] = response_msg[1]
    response_dict['login_user'] = response_msg[2]
    response_dict['login_host'] = response_msg[3]
    response_dict['command'] = response_msg[4]
    response_dict['option'] = response_msg[5]

    return response_dict

def get_command(info):
    command = int(info) & 0x000000ff  # 获取命令
    opt = int(info) & 0xffffff00  # 获取??

    return command,opt


