#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211201_1446. 连续字符.py
# @Author: Lin
# @Date  : 2021/12/4 17:45
# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
# 请你返回字符串的能量。
#
# 示例 1：
# 输入：s = "leetcode"
# 输出：2
# 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
# 示例 2：
# 输入：s = "abbcccddddeeeeedcba"
# 输出：5
# 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
# 示例 3：
# 输入：s = "triplepillooooow"
# 输出：5
# 示例 4：
# 输入：s = "hooraaaaaaaaaaay"
# 输出：11
# 示例 5：
# 输入：s = "tourist"
# 输出：1
#
# 提示：
# 1 <= s.length <= 500
# s 只包含小写英文字母。


class Solution:
    def maxPower(self, s: str) -> int:
        t, n, r = '', 1, 0
        for i in s:
            if i==t:
                n += 1
            else:
                n = 1
                t = i
            r = max(r, n)
        return r
