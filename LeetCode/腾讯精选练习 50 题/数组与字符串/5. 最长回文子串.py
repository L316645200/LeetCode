#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 5. 最长回文子串.py
# @Author: Lin
# @Date  : 2022/4/15 16:33
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def palindrome(x):
            m, n = 0, len(s)
            arr = s[0] if x == 1 else []
            for i in range(n):
                t = 0
                left, right = i-1, i+x
                while left >= 0 and right <= n-1 and s[left] == s[right]:
                    t += 2
                    left -= 1
                    right += 1
                if t > m:
                    m = t
                    arr = s[left+1:right]
            return m, arr
        m1, arr1 = palindrome(0)
        m2, arr2 = palindrome(1)
        return arr1 if m1 > m2 else arr2


s = Solution()
r = s.longestPalindrome('a')
print(r)


