#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：example.py
# @Author  ：Lin
# @Date    ：2024/6/13 16:26


"""三、遍历集合
设元素范围从
0
0 到
𝑛
−
1
n−1，枚举范围中的元素
𝑖
i，判断
𝑖
i 是否在集合
𝑠
s 中。"""
# n = 5
#
#
# s = 13
# for i in range(n):
#     if (s >> i) & 1:  # i 在 s 中
#         print(i)
#         print('1101', s >> i)
#
#
#
#
# print( )
# sub = s
# while True:
#     # 处理 sub 的逻辑
#     sub = (sub - 1) & s
#     print(sub)
#     if sub == s:
#         break

# 1101
# 1100
# 1001
# 1000
# 0101
# 0100
# 0010
# 0000

a = [50] * 20
b = [40] * 15
c = [60] * 10
d = 310

