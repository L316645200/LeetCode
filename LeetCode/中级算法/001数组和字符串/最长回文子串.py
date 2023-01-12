#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最长回文子串.py
# @Author: Lin
# @Date  : 2021/8/28 15:43
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
#
# 输入：s = "a"
# 输出："a"
# 示例 4：
#
# 输入：s = "ac"
# 输出："a"
#  
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母（大写和/或小写）组成

# 中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        ans = 1
        begin = 0
        for i in range(1, n):
            left = i - 1
            right = i + 1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>ans:
                    ans = right-left+1
                    begin = left
                left -= 1
                right += 1

        for i in range(1, n):
            if s[i] == s[i-1]:
                if 2>ans:
                    ans = 2
                    begin = i-1
                left = i - 2
                right = i + 1
                while left>=0 and right<n and s[left]==s[right]:
                    if right-left+1>ans:
                        ans = right-left+1
                        begin = left
                    left -= 1
                    right += 1
        return s[begin:begin+ans]
class Solution:
    def center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        begin = 0
        end = 0
        for i in range(n):
            left1, right1 = self.center(s, i, i)
            left2, right2 = self.center(s, i, i + 1)
            if right1 - left1 > end - begin:
                begin, end = left1, right1
            if right2 - left2 > end - begin:
                begin, end = left2, right2
        return s[begin: end+1]

s = Solution()
res = s.longestPalindrome('beeeaaaaabb')
print(res)