# print('hello world')

"""
这是多行注释
"""
#
# number = "-" * 3
# print(number)

# apple_price = input("apple price:")
# apple_price = float(apple_price)
# apple_num= input("apple number:")
# apple_num = float(apple_num)
# apple_sum_price = apple_price * apple_num
# print(float(apple_sum_price))
# #apple_sum_price = str(apple_sum_price)
# print("apple sum prime = %f" % apple_sum_price)
# print("apple sum prime = %.2f" % apple_sum_price)

# name = 2
# print("my name is %s" % name)


# a = float(0.366)
# print("%.2f%%" % (a * 100))

# age = 7
# if age >= 18:
#     print("满 18 岁")
# else:
#     print("不满 18 岁")
#
# 99 乘法表
# line=1
# while line<=9:
#     i=1
#     while i<=line:
#         print("%d * %d = %d" % (i,line,line*i),end='\t')
#         i+=1
#     print("")
#     line+=1
# a,b=1,2
# print(a,end='\t')
# print(b)

#list 函数使用
# name_list=[]
# name_list.insert(0,"张三")
# name_list.append("李四")
# name2_list=["王五"]
# name_list.extend(name2_list)
# name_list[0]="小1"
# name_list.remove("李四")
# name_list.append("王五")
# print(name_list)
# pup=[1,3,6,2]
# pup.sort()
# pup.sort(reverse=True)
# pup.reverse()
# for i in name_list:
#     print(i)
# print(len(pup))

# name=("xiao","lal","hei")
# name2=list(name)
# name3=tuple(name2)
# print(name3)
#
# 字典
# name={0:1,"s":"ddd",(1,2,3):[1,2,3]}
# for i in name:
#     print(i,name[i])
#
# name3="张三"
# for j in name3:
#     print(j)

#字符串
# str='何晋'
# a=str.encode('utf-8')
# print(a)
# print(a.decode('utf-8'))

#集合
#a=set()
# print(type(a))
#name="hejin"
# def hello():
#     '''
#
#     :return:
#     '''
#     print("1")
#     print("22")
#     print("333")
# hello()
# print(name)

# def sumhanshu(sum1, sum2):
#     return  sum1 + sum2
#
# a = sumhanshu(2, 3)
# print(a)


#类初始化属性、私有属性设置为可访问、可写
# class xiaotianshi():
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name or '无名氏'
#     def __repr__(self):
#         return f'{self.__name}, {self.__old} is xiao xian nv'
#
# xiannv = xiaotianshi("hejin", "18")
#
# xiannv.name = "dudu"
# print(xiannv.name)
# print(xiannv)


#UPD 服务端接受消息
from socket import *

# addr = ('127.0.0.1', 8889)
# upd_socket = socket(AF_INET, SOCK_DGRAM)
# upd_socket.bind(addr)
# msg,add1 = upd_socket.recvfrom(1024)
# print(add1, msg.decode())
# upd_socket.close()

#TCP 服务端接受消息
# tcp1 = socket(AF_INET,SOCK_STREAM)
# # #服务器的地址是一个元组
# # tcp1.bind(('0.0.0.0',8889))
# # #最大可链接的次数，最多是1024次
# # tcp1.listen(5)
# # #等待处理连接中
# # print("等待链接中。。。")
# # while True:
# #     connfd,addr = tcp1.accept()
# #     print(f"{addr}已经连接本服务器。")
# #     data = connfd.recv(1024)
# #     print("他发送的消息是：",data.decode())
# #     connfd.close()
# # tcp1.close()


import requests
from lxml import etree
r = requests.get('http://www.gotokeep.com')
print(r)

