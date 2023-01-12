#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221203_1796. 字符串中第二大的数字.py
# @Author: Lin
# @Date  : 2022/12/3 10:09

# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
# 混合字符串 由小写英文字母和数字组成。
# 示例 1：
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
# 示例 2：
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
# 提示：
# 1 <= s.length <= 500
# s 只包含小写英文字母和（或）数字。

class Solution:
    def secondHighest(self, s: str) -> int:
        arr = sorted(list(set([int(i) for i in s if i.isdigit() is True])))
        print(arr)
        return -1 if len(arr) < 2 else arr[-2]

class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for c in s:
            if c.isdigit():
                num = int(c)
                if num > first:
                    second = first
                    first = num
                elif second < num < first:
                    second = num
        return second

s = Solution()
s.secondHighest(s = "dfa12321afd")