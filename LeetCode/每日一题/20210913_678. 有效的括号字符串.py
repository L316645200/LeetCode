#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210913_678. 有效的括号字符串.py
# @Author: Lin
# @Date  : 2021/9/13 10:14
# 中等
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
#
# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。
# 示例 1:
#
# 输入: "()"
# 输出: True
# 示例 2:
#
# 输入: "(*)"
# 输出: True
# 示例 3:
#
# 输入: "(*))"
# 输出: True
# 注意:
#
# 字符串大小将在 [1，100] 范围内。

from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        left = deque()
        asterisk = deque()
        for i, v in enumerate(s):
            if v == '(':
                left.append(i)
            elif v == '*':
                asterisk.append(i)
            else:
                if left:
                    left.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False
        while left and asterisk:
            if left[-1] < asterisk[-1]:
                left.pop()
                asterisk.pop()
            else:
                return False
        return False if left else True


class Solution:
    def checkValidString(self, s: str) -> bool: # ???
        left = 0
        right = 0
        for i in s:
            if i == '(':
                left += 1
                right += 1
            elif i == '*':
                left -= 1
                right += 1
            else:
                left -= 1
                right -= 1
            if left < 0:
                left += 1
            if right < 0:
                return False
        return left == 0
