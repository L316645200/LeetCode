#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 验证回文串.py
# @Author: Lin
# @Date  : 2021/7/10 11:33
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
# 相关标签
# 双指针
# 字符串



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        else:
            return True