# -*-coding:gbk*-

import time
from getrandom import *

def write_log_en(alg,mode,data,key,res,use_time):
    # 写从日志 在sign == True 时执行 加密
    with open(".\\"+str(alg)+"\\"+str(alg)+"算法"+str(mode)+"模式测试"+".log",'a+') as f_follow:
        f_follow.write(str(alg)+"算法"+str(mode)+"模式使用数据"+str(data)+"使用密钥"+str(key)+"加密得到结果"+str(res)+"用时"+str(use_time)+'ms')
        f_follow.write('\n')
        f_follow.close()
    return

def write_log_de(alg,mode,data,key,res,use_time):
    # 写从日志 在sign == True 时执行 解密
    with open(".\\"+str(alg)+"\\"+str(alg)+"算法"+str(mode)+"模式测试"+".log",'a+') as f2:
        f2.write(str(alg)+"算法"+str(mode)+"模式使用数据"+str(data)+"使用密钥"+str(key)+"解密得到结果"+str(res)+"用时"+str(use_time)+'ms')
        f2.write('\n')
        f2.close()

def alg_all_test(sign, alg, mode, func_en, func_de):
    """
    :param sign:
    :param alg:
    :param mode:
    :param func_en: 加密算法接口 返回结果
    :param func_de: 解密算法接口 同
    :return:
    """
    all_time_en = 0
    all_time_de = 0
    # 清空日志
    with open(".\\"+str(alg)+"\\"+str(alg)+"算法"+str(mode)+"模式测试"+".log",
              'w') as f_follow:
        f_follow.close()

    for i in range(1000):
        test_key = T_key
        data1 = get_random_16bytes()
        t0 = time.perf_counter()
        cyphertext = func_en(mode=mode,data=data1,key=test_key)
        t1 = time.perf_counter()
        used_time = (t1 - t0) * 1000
        all_time_en += used_time
        # 写加密日志
        if sign == True:
            write_log_en(alg=alg,mode=mode,data=data1,key=test_key,res=cyphertext,use_time=used_time)

        # Decrypt data with the same key
        t0 = time.perf_counter()
        plaintext = func_de(mode=mode,data=cyphertext,key=test_key)
        t1 = time.perf_counter()
        used_time = (t1 - t0) * 1000
        all_time_de += used_time

        # 写解密日志
        if sign == True:
            write_log_de(alg=alg, mode=mode, data=cyphertext,key=test_key, res=plaintext, use_time=used_time)

    return (all_time_en,all_time_de)


