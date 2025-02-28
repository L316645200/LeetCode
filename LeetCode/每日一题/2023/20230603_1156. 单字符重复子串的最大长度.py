#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230603_1156. 单字符重复子串的最大长度.py
# @Author: Lin
# @Date  : 2023/6/3 10:21


# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
# 示例 1：
# 输入：text = "ababa"
# 输出：3
# 示例 2：
# 输入：text = "aaabaaa"
# 输出：6
# 示例 3：
# 输入：text = "aaabbaaa"
# 输出：4
# 示例 4：
# 输入：text = "aaaaa"
# 输出：5
# 示例 5：
# 输入：text = "abcdef"
# 输出：1
# 提示：
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        cut = []
        c, n = text[0], 1
        for i in range(1, len(text)):
            if text[i] != c:
                cut.append([c, n])
                n = 1
                c = text[i]
            else:
                n += 1
        cut.append([c, n])
        n, res = len(cut), 0
        for i in range(n):
            t = cut[i][1] + 1
            if i < n - 2 and cut[i+1][1] == 1 and cut[i][0] == cut[i + 2][0]:
                t += cut[i + 2][1]
            res = max(res, min(t, cnt[cut[i][0]]))
        return res
# class Solution:
#     def maxRepOpt1(self, text: str) -> int:
#         cnt = Counter(text)
#         n = len(text)
#         res = 0
#         i = 0
#         while i < n:
#             j = i + 1
#             while j < n and text[i] == text[j]:
#                 j += 1
#             res = max(res, j - i)
#             k = j + 1
#             while k < n and text[i] == text[k]:
#                 k += 1
#             res = max(res, min(k - i, cnt[text[i]]))
#             i = j
#         return res

s = Solution()
s.maxRepOpt1(text = "aaabbaaa")

