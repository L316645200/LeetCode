#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220513_面试题 01.05. 一次编辑.py
# @Author: Lin
# @Date  : 2022/5/13 16:19

# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
# 示例 1:
# 输入:
# first = "pale"
# second = "ple"
# 输出: True
# 示例 2:
# 输入:
# first = "pales"
# second = "pal"
# 输出: False
import requests


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if abs(len1 - len2) > 1:
            return False
        left, right = 0, 0
        n = 0
        if len1 == len2:
            while left < len1:
                if first[left] != second[right]:
                    n += 1
                left += 1
                right += 1
        else:
            if len1 < len2:
                first, second = second, first
                left, right = right, left
                len1, len2 = len2, len1

            while left < len1 and right < len2:
                if first[left] != second[right]:
                    n += 1
                    left += 1
                else:
                    left += 1
                    right += 1
        return n <= 1

s = Solution()
s.oneEditAway(first = "teacher", second = "bleacher")



class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]  # 注：改用下标枚举可达到 O(1) 空间复杂度
        return True



def get_access_token_v2():
    print(111)
    # 服务端API v2
    req = {'appKey': 'dingtx08f7gkgjddtjbb',
           'appSecret': 'ba15g3dPZbvq9Ysd7_bJjo2Knflkuj_LypGx0_ZXtil3dsgNV1VWBeEqLscnBaTs'}
    url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
    res = requests.post(url, json=req).json()

    access_token = res['accessToken']
    print(access_token)
    expire_in = res['expireIn']
    return access_token


get_access_token_v2()