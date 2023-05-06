#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Lin
# @Date  : 2023/4/22 11:15


def is_predecessor(word1, word2):
    print(word1, word2)
    i, j = 0, 0
    n = len(word1)
    while i < n and j < n + 1:
        if word1[i] == word2[j]:
            i += 1
            j += 1
        else:
            j += 1
    print(i,j)
    return True if j - 1 <= i == n else False


is_predecessor('xb', 'xbc')