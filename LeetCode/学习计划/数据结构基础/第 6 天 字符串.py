#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天 字符串.py
# @Author: Lin
# @Date  : 2022/10/25 11:49
# 415. 字符串相加
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 示例 1：
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 示例 3：
# 输入：num1 = "0", num2 = "0"
# 输出："0"
# 提示：
# 1 <= num1.length, num2.length <= 104
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
from collections import Counter


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        if m < n:
            num1, num2 = num2, num1
            m, n = n, m
        a = 0
        ans = ""
        for i in range(1, n + 1):
            a, b = divmod((int(int(num1[-i])+int(num2[-i])+a)), 10)
            ans = str(b) + ans
        for i in range(n + 1, m + 1):
            a, b = divmod((int(int(num1[-i])+a)), 10)
            ans = str(b) + ans
        if a == 1:
            ans = '1' + ans
        return ans


s = Solution()
s.addStrings(num1 = "456", num2 = "77")


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res

# 409. 最长回文串
# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
# 示例 1:
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 示例 2:
# 输入:s = "a"
# 输入:1
# 提示:
# 1 <= s.length <= 2000
# s 只由小写 和/或 大写英文字母组成


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for c in cnt.values():
            ans += c if c % 2 == 0 else c - 1
        return ans if len(s) == ans else ans + 1


s = Solution()
s.longestPalindrome(s = "abccccdd")

