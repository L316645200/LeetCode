#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：KMP.py
# @Author  ：Lin
# @Date    ：2024/10/12 16:22

# 前缀表 next或prefix

"""
文本串
aabaabaaf
模式串
aabaaf
010120
"""


def strStr(s):
    n = len(s)
    pre = [0] * n
    j = 0
    print(s)
    # j前缀最后一个，i后缀最后一个，构造最大的前后缀相等长度数组pre
    for i in range(1, n):
        # 当j>0且前缀最后一个和后缀最后一个不相等，j倒退
        while j > 0 and s[i] != s[j]:
            j = pre[j-1]
        # 当前缀最后一个和后缀最后一个相等，更新pre数组的值
        if s[i] == s[j]:
            j += 1
            pre[i] = j
    print(
        pre
    )

"""28. 找出字符串中第一个匹配项的下标
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
示例 1：
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
提示：
1 <= haystack.length, needle.length <= 104
haystack 和 needle 仅由小写英文字符组成
"""

# KMP 算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        pre = [0] * n
        j = 0
        # j前缀最后一个，i后缀最后一个，构造最大的前后缀相等长度数组pre
        for i in range(1, n):
            # 当j>0且前缀最后一个和后缀最后一个不相等，j倒退
            while j > 0 and needle[i] != needle[j]:
                j = pre[j - 1]
            # 当前缀最后一个和后缀最后一个相等，更新pre数组的值
            if needle[i] == needle[j]:
                j += 1
                pre[i] = j
        print(pre)
        j = 0
        for i in range(m):
            print(i, j, haystack[i], needle[j])
            while j > 0 and haystack[i] != needle[j]:
                j = pre[j-1]

            if haystack[i] == needle[j]:
                j += 1
                if j == n:
                    return i - j + 1
        return -1


s = Solution()
r = s.strStr(haystack = "mississippi", needle = "issip")
print(r)

"""459. 重复的子字符串
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
示例 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:
输入: s = "aba"
输出: false
示例 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
提示：
1 <= s.length <= 104
s 由小写英文字母组成"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        pre = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pre[j-1]
            if s[i] == s[j]:
                j += 1
                pre[i] = j
        return pre[-1]>0 and n % (n - pre[-1]) == 0

# s = Solution()
# s.repeatedSubstringPattern(s = "ababba")