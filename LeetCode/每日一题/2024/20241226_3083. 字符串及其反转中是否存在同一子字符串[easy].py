#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241226_3083. 字符串及其反转中是否存在同一子字符串[easy].py
# @Author  ：Lin
# @Date    ：2024/12/26 11:18

"""给你一个字符串 s ，请你判断字符串 s 是否存在一个长度为 2 的子字符串，在其反转后的字符串中也出现。

如果存在这样的子字符串，返回 true；如果不存在，返回 false 。



示例 1：

输入：s = "leetcode"

输出：true

解释：子字符串 "ee" 的长度为 2，它也出现在 reverse(s) == "edocteel" 中。

示例 2：

输入：s = "abcba"

输出：true

解释：所有长度为 2 的子字符串 "ab"、"bc"、"cb"、"ba" 也都出现在 reverse(s) == "abcba" 中。

示例 3：

输入：s = "abcd"

输出：false

解释：字符串 s 中不存在满足「在其反转后的字符串中也出现」且长度为 2 的子字符串。"""
from itertools import pairwise


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        for i in range(n-1):
            if s[i:i+2][::-1] in s:
                return True
        return False



class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        visited = set()
        for i in range(n-1):
            visited.add(s[i:i+2][::-1])
            if s[i:i+2] in visited:
                return True
        return False

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        vis = set()
        for x, y in pairwise(s):
            vis.add(x + y)
            if y + x in vis:
                return True
        return False

s = Solution()
s.isSubstringPresent("abcba")