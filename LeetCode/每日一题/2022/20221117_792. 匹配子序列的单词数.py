#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221117_792. 匹配子序列的单词数.py
# @Author: Lin
# @Date  : 2022/11/17 16:38

# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
# 例如， “ace” 是 “abcde” 的子序列。
# 示例 1:
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
# Example 2:
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
# 提示:
# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# words[i]和 s 都只由小写字母组成。
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            i, j = 0, 0
            m, n = len(s), len(word)
            while i < m and j < n:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == n:
                ans += 1
        return ans


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        ans = len(words)
        for i in range(len(s)):
            pos[s[i]].append(i)
        for word in words:
            index = -1
            if len(word) > len(s):
                ans -= 1
                continue
            for w in word:
                c = bisect_right(pos[w], index)
                if c == len(pos[w]):
                    ans -= 1
                    break
                index = pos[w][c]
        return ans


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        p = defaultdict(list)
        for i, w in enumerate(words):
            print(i,w)
            p[w[0]].append((i, 0))
        ans = 0
        print(p)


s = Solution()
s.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])