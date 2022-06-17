#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20. 有效的括号.py
# @Author: Lin
# @Date  : 2022/5/1 16:28

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 示例 1：
# 输入：s = "()"
# 输出：true
# 示例 2：
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
# 输入：s = "(]"
# 输出：false
# 示例 4：
# 输入：s = "([)]"
# 输出：false
# 示例 5：
# 输入：s = "{[]}"
# 输出：true
# 提示：
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        deq = deque()
        dic = {']': '[', ')': '(', '}': '{'}
        for i in s:
            if i in dic:
                if deq and deq.pop() == dic[i]:
                    continue
                else:
                    return False
            else:
                deq.append(i)
        return not deq



s = Solution()
res = s.isValid("[")
print(res)