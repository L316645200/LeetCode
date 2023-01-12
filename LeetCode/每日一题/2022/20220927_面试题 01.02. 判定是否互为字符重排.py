#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220927_面试题 01.02. 判定是否互为字符重排.py
# @Author: Lin
# @Date  : 2022/9/27 9:49

# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
# 示例 1：
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
# 示例 2：
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
# 说明：
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100
from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # return Counter(s1) == Counter(s2)
        return sorted(s1) == sorted(s2)




s = Solution()
s.CheckPermutation( s1 = "abc", s2 = "bca")


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        a, s = 0, 0
        for v in s1:
            a ^= ord(v)
            s += ord(v)
        for v in s2:
            a ^= ord(v)
            s -= ord(v)
        return len(s1) == len(s2) and a == 0 and s == 0

        return len(s1) == len(s2) and sum([ord(v) for v in s1]) == sum([ord(v) for v in s2]) and reduce(lambda a, b: a ^ ord(b), s1+s2, 0) == 0
        return len(s1) == len(s2) and reduce(lambda a, b: a+ord(b), s1, 0) == reduce(lambda a, b: a+ord(b), s2, 0) and reduce(lambda a, b: a ^ ord(b), s1+s2, 0) == 0

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        a = [0]*26
        for v in s1:
            a[ord(v)-ord('a')] += 1
        for v in s2:
            a[ord(v)-ord('a')] -= 1
            if a[ord(v)-ord('a')] < 0:
                return False
        return len(s1) == len(s2)

        a = defaultdict(int)
        for v in s1:
            a[v] += 1
        for v in s2:
            a[v] -= 1
            if a[v] < 0:
                return False
        return len(s1) == len(s2)

        return Counter(s1) == Counter(s2)
        return sorted(s1) == sorted(s2)