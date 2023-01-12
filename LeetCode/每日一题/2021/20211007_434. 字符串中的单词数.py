#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211011_434. 字符串中的单词数.py
# @Author: Lin
# @Date  : 2021/10/11 17:54

# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:

# 输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


class Solution:
    def countSegments(self, s: str) -> int:
        return sum(i != "" for i in s.split(" "))



so = Solution()
arr = so.countSegments(", , , ,        a, eaefa")
print(arr)