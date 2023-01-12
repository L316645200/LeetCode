#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210819_345. 反转字符串中的元音字母.py
# @Author: Lin
# @Date  : 2021/8/19 10:45
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1：
#
# 输入："hello"
# 输出："holle"
# 示例 2：
#
# 输入："leetcode"
# 输出："leotcede"
#
# 提示：
#
# 元音字母不包含字母 "y" 。

class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch):
            return ch in 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < len(s) and not is_vowel(s[l]):
                l += 1
            while r > 0 and not is_vowel(s[r]):
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)

s = Solution()
s.reverseVowels('leetcode')