#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250203_680. 验证回文串 II[easy].py
# @Author  ：Lin
# @Date    ：2025/2/5 10:10
"""680. 验证回文串 II

给你一个字符串s，最多 可以从中删除一个字符。
请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

示例 1：
输入：s = "aba"
输出：true

示例 2：
输入：s = "abca"
输出：true
解释：你可以删除字符 'c' 。

示例 3：
输入：s = "abc"
输出：false

提示：
	1 <= s.length <= 10^5
	s 由小写英文字母组成


https://leetcode.cn/problems/valid-palindrome-ii/description/?envType=daily-question&envId=2025-02-03"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(mark, left, right):
            while left < right:
                if s[left] != s[right]:
                    if not mark:
                        return False
                    return check(False, left, right - 1) or check(False, left + 1, right)
                left += 1
                right -= 1
            return True
        return check(True, 0, len(s) - 1)

s = Solution()
s.validPalindrome(s = "aba")