#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241220_3138. 同位字符串连接的最小长度[medium].py
# @Author  ：Lin
# @Date    ：2024/12/21 10:19

"""给你一个字符串 s ，它由某个字符串 t 和若干 t  的 同位字符串 连接而成。

请你返回字符串 t 的 最小 可能长度。

同位字符串 指的是重新排列一个单词得到的另外一个字符串，原来字符串中的每个字符在新字符串中都恰好只使用一次。



示例 1：

输入：s = "abba"

输出：2

解释：

一个可能的字符串 t 为 "ba" 。

示例 2：

输入：s = "cdef"

输出：4

解释：

一个可能的字符串 t 为 "cdef" ，注意 t 可能等于 s 。



提示：

1 <= s.length <= 105
s 只包含小写英文字母。"""
from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            for j in range(i, n, i):
                if Counter(s[:i]) != Counter(s[j: j + i]):
                    break
                if j == n - i:
                    return i
        return n


s = Solution()
s.minAnagramLength("abba")