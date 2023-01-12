#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 9 天 字符串.py
# @Author: Lin
# @Date  : 2022/11/15 17:54

# 187. 重复的DNA序列
# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
# 示例 1：
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 提示：
# 0 <= s.length <= 105
# s[i]=='A'、'C'、'G' or 'T'
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = defaultdict(int)
        for i in range(9, len(s)):
            cnt[s[i-9: i+1]] += 1
        return [k for k, v in cnt.items() if v > 1]


s = Solution()
s.findRepeatedDnaSequences(s= "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

#
# 5. 最长回文子串
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        begin, end = 0, 0
        for i in range(n):
            left1, right1 = self.center(s, n, i, i)
            left2, right2 = self.center(s, n, i, i + 1)
            if right1 - left1 > end - begin:
                begin, end = left1, right1
            if right2 - left2 > end - begin:
                begin, end = left2, right2
        return s[begin: end+1]

    def center(self, s, n, left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return [left+1, right-1]


s = Solution()
r = s.longestPalindrome(s = "babad")
print(r)