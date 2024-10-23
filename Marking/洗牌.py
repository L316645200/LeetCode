#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：洗牌.py
# @Author  ：Lin
# @Date    ：2024/9/13 17:30
import random




def shuffle(x):
    arr = [i for i in range(1, x+1)]
    for i in range(x, 0, -1):
        k = random.randint(1, i)
        arr[i-1], arr[k-1] = arr[k-1], arr[i-1]
    print(arr)
    return arr


shuffle(54)