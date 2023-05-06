#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230318_1616. 分割两个字符串得到回文串.py
# @Author: Lin
# @Date  : 2023/3/18 9:39


# 给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。
#
# 当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
#
# 如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
#
# 注意， x + y 表示连接字符串 x 和 y 。
# 示例 1：
# 输入：a = "x", b = "y"
# 输出：true
# 解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# 那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。
# 示例 2：
#
# 输入：a = "abdef", b = "fecab"
# 输出：true
# 示例 3：
#
# 输入：a = "ulacfd", b = "jizalu"
# 输出：true
# 解释：在下标为 3 处分割：
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# 那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
# 提示：
#
# 1 <= a.length, b.length <= 105
# a.length == b.length
# a 和 b 都只包含小写英文字母
# 双指针
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        return self.checkPalindrome(a, b, n) or self.checkPalindrome(b, a, n) or \
               self.checkPalindrome(a[::-1], b[::-1], n) or self.checkPalindrome(b[::-1], a[::-1], n)

    def checkPalindrome(self, a, b, n):
        left, right = 0, n - 1
        mark = 1
        while left < right:
            if mark == 1:
                if a[left] == b[right]:
                    left += 1
                    right -= 1
                else:
                    mark = 0
            else:
                if a[left] == a[right]:
                    left += 1
                    right -= 1
                else:
                    break
        return True if left >= right else False


# 中心扩展
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        self.n = len(a)
        left = self.n // 2 - 1
        left = min(self.check(a, a, left), self.check(b, b, left))
        left = min(self.check(a, b, left), self.check(b, a, left))
        return left == -1

    def check(self, str_left, str_right, left):
        right = self.n - left - 1
        while left >= 0 and right < self.n:
            if str_left[left] != str_right[right]:
                break
            left -= 1
            right += 1
        return left


s = Solution()
s.checkPalindromeFormation(a = "pvhmupgqeltozftlmfjjde", b = "yjgpzbezspnnpszebzmhvp")

