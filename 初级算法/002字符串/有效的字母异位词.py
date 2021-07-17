#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 有效的字母异位词.py
# @Author: Lin
# @Date  : 2021/7/10 11:32
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#  
#
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#  
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
# 相关标签
# 哈希表
# 字符串
# 排序
import collections


# 计数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)