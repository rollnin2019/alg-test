# 测试算法接口使用说明

**main入口：**

例：ans = aes.role(sign=True, alg='aes', mode='ecb')
sign：是否打印子日志 True则在当前目录下算法名称（alg）下打印每一次测试数据
mode：支持ecb cbc模式
alg：算法名称

算法需要提供对外加解密接口 名称为encrypt decrypt
使用时直接导包的role方法即可









