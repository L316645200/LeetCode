#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天 双指针.py
# @Author: Lin
# @Date  : 2021/7/27 12:20

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#  
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# 557. 反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#  
#
# 示例：
#
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#  
#
# 提示：
#
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x: x[::-1], s.split(' '))))
