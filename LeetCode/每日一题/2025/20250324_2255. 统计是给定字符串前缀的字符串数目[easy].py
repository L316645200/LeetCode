#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/24 10:53
# @Author  : Lin
# @File    : 20250324_2255. 统计是给定字符串前缀的字符串数目[easy].py
"""给你一个字符串数组 words 和一个字符串 s ，其中 words[i] 和 s 只包含 小写英文字母 。

请你返回 words 中是字符串 s 前缀 的 字符串数目 。

一个字符串的 前缀 是出现在字符串开头的子字符串。子字符串 是一个字符串中的连续一段字符序列。



示例 1：

输入：words = ["a","b","c","ab","bc","abc"], s = "abc"
输出：3
解释：
words 中是 s = "abc" 前缀的字符串为：
"a" ，"ab" 和 "abc" 。
所以 words 中是字符串 s 前缀的字符串数目为 3 。
示例 2：

输入：words = ["a","a"], s = "aa"
输出：2
解释：
两个字符串都是 s 的前缀。
注意，相同的字符串可能在 words 中出现多次，它们应该被计数多次。


提示：

1 <= words.length <= 1000
1 <= words[i].length, s.length <= 10
words[i] 和 s 只 包含小写英文字母。"""
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if s.startswith(word):
                res += 1
        return res

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c, mp = '', set()
        for char in s:
            c += char
            mp.add(c)
        return sum([1 if word in mp else 0 for word in words])


s = Solution()
s.countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc")
