#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最长公共前缀.py
# @Author: Lin
# @Date  : 2021/7/10 11:34
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#  
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#  
#
# 提示：
#
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 相关标签
# 字符串
#
# Python3


class Solution:
    def longestCommonPrefix(self, l: List[str]) -> str:
        s = ''
        for n in zip(*l):
            if len(set(n)) == 1:
                s += n[0]
            else:
                break
        return s