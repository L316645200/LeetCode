#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串中的第一个唯一字符.py
# @Author: Lin
# @Date  : 2021/7/10 11:31
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#  
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#  
#
# 提示：你可以假定该字符串只包含小写字母。
#
# 相关标签
# 队列
# 哈希表
# 字符串
# 计数

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        l = len(s)
        for i in range(l):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = l + 1
        r = [d[i] for i in d]
        return min(r) if l > 0 and min(r) < l + 1 else -1