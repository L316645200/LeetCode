#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 7 天 字符串.py
# @Author: Lin
# @Date  : 2022/10/26 15:42
# 290. 单词规律
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 示例 2:
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 示例 3:
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
# 提示:
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        dict1 = {}
        dict2 = {}
        for ch, word in zip(pattern, words):
            if (ch in dict1 and dict1[ch] != word) or (word in dict2 and dict2[word] != ch):
                return False
            dict1[ch] = word
            dict2[word] = ch
        return True

s = Solution()
s.wordPattern(pattern = "abba", s = "dog cat cat dog")
r = s.wordPattern(pattern = "abba", s = "dog cat cat fish")
r = s.wordPattern(pattern = "aaaa", s = "dog cat cat dog")

# 763. 划分字母区间
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
# 示例：
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
# 提示：
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxidict = {v: i for i, v in enumerate(s)}
        ans, n = [], len(s)
        left, right, f = 0, 0, 0
        while left <= right and left < n:
            right = max(right, maxidict[s[left]])
            left += 1
            if left > right:
                right += 1
                ans.append(right-f)
                f = left
        return ans
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxidict = {v: i for i, v in enumerate(s)}
        ans, n = [], len(s)
        left, right = 0, 0
        for i in range(n):
            right = max(right, maxidict[s[i]])
            if i == right:
                ans.append(right-left+1)
                left = right + 1
        return ans
s = Solution()
s.partitionLabels(s = "ababcbacadefegdehijhklij")



































