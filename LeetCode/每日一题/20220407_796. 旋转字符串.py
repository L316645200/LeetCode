#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220407_796. 旋转字符串.py
# @Author: Lin
# @Date  : 2022/4/7 9:41
# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
# 示例 1:
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
# 示例 2:
# 输入: s = "abcde", goal = "abced"
# 输出: false
# 提示:
# 1 <= s.length, goal.length <= 100
# s 和 goal 由小写英文字母组成

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if (l := len(s)) != len(goal):
            return False
        for i in [i for i in range(l) if goal[i] == s[0]]:
            n = 0
            while n < l:
                if s[n] == goal[(i+n) % l]:
                    n += 1
                else:
                    break
            if n == l:
                return True
        return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in (s+s) if len(s) == len(goal) else False

s = Solution()
res = s.rotateString("abcde", "cdeab")
print(res)