import MainData as md

def add_to_list(data,addr):
    # 向列表中添加在线的用户
    temp_dict = dict()
    temp_dict['ip'] = addr[0]
    temp_dict['username'] = data['login_user']
    if temp_dict not in md.user_list:
        md.user_list.append(temp_dict)

def delete_from_list(data,addr):
    # 从列表中删除下线的用户
    temp_dict = dict()
    temp_dict['ip'] = addr[0]
    temp_dict['username'] = data['login_user']
    if temp_dict in md.user_list:
        md.user_list.remove(temp_dict)

def add_to_download_list(data):
    """将文件下载信息加入到列表中"""
    #0:mao.py:05b5:5982886d:1:
    temp_dict = dict()
    data_list = data.split(":")
    temp_dict['file_name'] = data_list[1]
    temp_dict['file_size'] = int(data_list[2],16)
    temp_dict['package_id'] = int(data_list[3])
    temp_dict['file_id'] = int(data_list[0])
    down_info = dict()
    down_info['type'] = 'download'
    down_info['data'] = temp_dict
    md.download.put(down_info)


