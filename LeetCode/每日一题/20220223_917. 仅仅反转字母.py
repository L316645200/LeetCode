#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220223_917. 仅仅反转字母.py
# @Author: Lin
# @Date  : 2022/2/23 15:52

# 给你一个字符串 s ，根据下述规则反转字符串：
#
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。
#
# 示例 1：
# 输入：s = "ab-cd"
# 输出："dc-ba"
# 示例 2：
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 提示
# 1 <= s.length <= 100
# s 仅由 ASCII 值在范围 [33, 122] 的字符组成
# s 不含 '\"' 或 '\\'
from itertools import combinations


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        arr = list(s)
        def is_str(x):
            if (65 <= ord(x) <= 90) or (97 <= ord(x) <= 122):
                return True
            else:
                return False
        while left < right:
            if not is_str(s[left]):
                left += 1
            elif not is_str(s[right]):
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        print(''.join(arr))
        return ''.join(arr)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        arr = list(s)
        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return ''.join(arr)
# 大写A-Z 65-92 小写a-z 97-122
s = Solution()
s.reverseOnlyLetters("AaW;c?[")

print(list(combinations([1,2,3], 2)))
