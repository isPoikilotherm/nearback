import socket


def send_msg(udp_socket):
    msg = input("输入要发送的数据：")
    if msg.isdigit():
        ip = "192.168.0.111"
        port = 8080
        udp_socket.sendto(msg.encode("utf_8"), (ip, port))

    else:
        print("请输入数字！")




def send():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_msg(udp_socket)


if __name__ == '__main__':
    send()




















