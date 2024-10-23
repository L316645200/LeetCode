#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240919_2414. 最长的字母序连续子字符串的长度[medium].py
# @Author  ：Lin
# @Date    ：2024/9/19 9:30


"""字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。

例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
示例 1：
输入：s = "abacaba"
输出：2
解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
"ab" 是最长的字母序连续子字符串。
示例 2：
输入：s = "abcde"
输出：5
解释："abcde" 是最长的字母序连续子字符串。
提示：
1 <= s.length <= 105
s 由小写英文字母组成"""

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res, cur = 1, 1
        for i in range(1, len(s)):
            if ord(s[i-1]) + 1 == ord(s[i]):
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
            i += 1
        return res

s = Solution()
s.longestContinuousSubstring(s = "abacaba")