# -*-coding:gbk*-

import aes
import des3
import sm4
import rc4

def write_main_log(alg,ans):
    with open('log-main-test.log','a+') as f:
        f.write(alg + "加密1000次耗时"+str(ans[0])+"ms")
        f.write('\n')
        f.write(alg + "解密1000次耗时"+str(ans[1])+"ms")
        f.write('\n')
        f.close()

if __name__ == "__main__":
    # # aes.role 加密算法入口
    ans = des3.role(sign=True,alg='des3',mode='ecb')
    write_main_log('des3-ecb', ans)

    ans = des3.role(sign=True,alg='des3',mode='cbc')
    write_main_log('des3-cbc', ans)

    ans = sm4.role(sign=True,alg='des3',mode='ecb')
    write_main_log('sm4-ecb', ans)

    ans = sm4.role(sign=True,alg='sm4',mode='cbc')
    write_main_log('sm4-cbc',ans)

    ans = aes.role(sign=True, alg='aes', mode='ecb')
    write_main_log('aes-ecb', ans)

    ans = aes.role(sign=True, alg='aes', mode='cbc')
    write_main_log('aes-cbc', ans)

    ans = rc4.role(sign=True,alg='rc4',mode='ecb')
    write_main_log('rc4', ans)

