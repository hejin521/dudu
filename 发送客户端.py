from socket import *

#UDP 客户端发送消息
# addr1 = ('127.0.0.1',8889)
# # apd1 = socket(AF_INET,SOCK_DGRAM)
# # apd1.sendto("hello ni hao".encode(),addr1)
# # apd1.close()

#TCP 客户端发送消息
#发送给谁就需要连接谁，这个谁就是地址
# addr2 = ('0.0.0.0',8889)
# tcp2 = socket()
# tcp2.connect(addr2)
# while True:
#     print(f"已经连接服务器{addr2}")
#     msg = input("请输入：")
#     tcp2.send(msg.encode())
#     if msg == "dudu":
#         break
# tcp2.close()
