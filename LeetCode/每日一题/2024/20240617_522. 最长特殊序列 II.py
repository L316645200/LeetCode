#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240617_522. 最长特殊序列 II.py
# @Author  ：Lin
# @Date    ：2024/6/17 10:20


"""给定字符串列表 strs ，返回其中 最长的特殊序列 的长度。如果最长特殊序列不存在，返回 -1 。

特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。

 s 的 子序列可以通过删去字符串 s 中的某些字符实现。

例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。


示例 1：

输入: strs = ["aba","cdc","eae"]
输出: 3
示例 2:

输入: strs = ["aaa","aaa","aa"]
输出: -1


提示:

2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] 只包含小写英文字母"""
from collections import defaultdict
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # def is_subsequence(str1, str2):
        #     n1, n2 = len(str1), len(str2)
        #     i, j = 0, 0
        #     while i < n1:
        #         while j < n2 and str1[i] != str2[j]:
        #             j += 1
        #         if j == n2:
        #             break
        #         elif str1[i] == str2[j]:
        #             i += 1
        #             j += 1
        #     return i != n1

        def is_subseq(s: str, t: str) -> bool:
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1
            return pt_s != len(s)

        strs.sort(key=lambda x: len(x))
        n = len(strs)
        for i in range(n-1, -1, -1):
            mark = True
            for j in range(n-1, -1, -1):
                if i == j:
                    continue
                if len(strs[i]) > len(strs[j]):
                    break
                elif len(strs[i]) == len(strs[j]):
                    if strs[i] == strs[j]:
                        mark = False
                        break
                else:
                    mark = is_subseq(strs[i], strs[j])
                    if mark is False:
                        break
            if mark:
                return len(strs[i])
        return -1


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1
            return pt_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and is_subseq(s, t):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))

        return ans


s = Solution()
# s.findLUSlength(strs = ["aba","cdc","eae"])


r = s.findLUSlength(strs = ["aaa","aaa","aa"])
print(r)