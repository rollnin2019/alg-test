# -*-coding:utf-8-*-
import random
#  随机数生成盒
ran_box = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def get_random_16bytes():
    # 得到随机加密的字节数组
    res_ans = ""
    for i in range(32):
        res_ans += ran_box[random.randint(0, len(ran_box)-1)]
    return res_ans

# key
T_key = '404142434445464748494A4B4C4D4E4F'




