#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 有效的括号.py
# @Author: Lin
# @Date  : 2021/7/10 11:56
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
# 示例 2：
#
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
#
# 输入：s = "(]"
# 输出：false
# 示例 4：
#
# 输入：s = "([)]"
# 输出：false
# 示例 5：
#
# 输入：s = "{[]}"
# 输出：true
#  
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成
# 相关标签
# 栈
# 字符串

class Solution:
    def isValid(self, s: str) -> bool:
        t = {'}':'{', ']': '[', ')':'('}
        r = []

        for _ in s:
            if _ not in t:
                r.append(_)
            else:
                if not r:
                    return False
                else:
                    char = r.pop()
                    if char != t[_]:
                        return False
        return not r