# -*- coding: utf-8 -*-
# @Time : 2021/3/28 下午3:01
# @Author : ddz

# 源字符串srcStr进行若干次移位，判断是否包含另一字符串desStr。
# 举个例子，srcStr="AABBCD" desStr="CDAA" ,则符合上面的叙述，只需要将srcStr中的CD先后左移即可
def test(src, des):
    # 思路一：将源字符串左移或者右移源字符串长度，得到的新字符串进行判断
    # for i in range(1, len(src)):
    #     # src[len(src)-i:] + src[:len(src)-i] 旋转拼接
    #     if des in src[len(src)-i:] + src[:len(src)-i]:
    #         return True
    #         break
    # return False

    # 思路二：组合两个字符串，进行判断，空间换时间
    return des in (src + src)


if __name__ == '__main__':
    src = '112a3434'
    des = '34112'
    print(test(src, des))
