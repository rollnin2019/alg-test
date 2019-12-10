# -*-coding:gbk*-

import time
from getrandom import *

def write_log_en(alg,mode,data,key,res,use_time):
    # д����־ ��sign == True ʱִ�� ����
    with open(".\\"+str(alg)+"\\"+str(alg)+"�㷨"+str(mode)+"ģʽ����"+".log",'a+') as f_follow:
        f_follow.write(str(alg)+"�㷨"+str(mode)+"ģʽʹ������"+str(data)+"ʹ����Կ"+str(key)+"���ܵõ����"+str(res)+"��ʱ"+str(use_time)+'ms')
        f_follow.write('\n')
        f_follow.close()
    return

def write_log_de(alg,mode,data,key,res,use_time):
    # д����־ ��sign == True ʱִ�� ����
    with open(".\\"+str(alg)+"\\"+str(alg)+"�㷨"+str(mode)+"ģʽ����"+".log",'a+') as f2:
        f2.write(str(alg)+"�㷨"+str(mode)+"ģʽʹ������"+str(data)+"ʹ����Կ"+str(key)+"���ܵõ����"+str(res)+"��ʱ"+str(use_time)+'ms')
        f2.write('\n')
        f2.close()

def alg_all_test(sign, alg, mode, func_en, func_de):
    """
    :param sign:
    :param alg:
    :param mode:
    :param func_en: �����㷨�ӿ� ���ؽ��
    :param func_de: �����㷨�ӿ� ͬ
    :return:
    """
    all_time_en = 0
    all_time_de = 0
    # �����־
    with open(".\\"+str(alg)+"\\"+str(alg)+"�㷨"+str(mode)+"ģʽ����"+".log",
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
        # д������־
        if sign == True:
            write_log_en(alg=alg,mode=mode,data=data1,key=test_key,res=cyphertext,use_time=used_time)

        # Decrypt data with the same key
        t0 = time.perf_counter()
        plaintext = func_de(mode=mode,data=cyphertext,key=test_key)
        t1 = time.perf_counter()
        used_time = (t1 - t0) * 1000
        all_time_de += used_time

        # д������־
        if sign == True:
            write_log_de(alg=alg, mode=mode, data=cyphertext,key=test_key, res=plaintext, use_time=used_time)

    return (all_time_en,all_time_de)


