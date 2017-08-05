

"""保存需要用到的变量及数据"""

udp_socket = None  # udp套接字
feiq_port = 2425  # feiq端口号
login_user = 'new'  # 登陆用户名
login_host = 'localhost'  # 登陆主机名
broadcast_ip = '255.255.255.255'  # 广播地址
user_list = list()
file_queue = dict()
main_queue = None
file_list = list()
download_list = list()
upload_list = list()
download_queue = None

MSG_ONLINE = 0X00000001  # 上线
MSG_OFFLINE = 0X00000002  # 下线
MSG_SEND = 0X00000020  # 发送信息
MSG_RESPONSE = 0X00000021 #回复信息


