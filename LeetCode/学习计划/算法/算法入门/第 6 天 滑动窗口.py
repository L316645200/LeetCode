#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天 滑动窗口.py
# @Author: Lin
# @Date  : 2021/7/29 19:13
# 3. 无重复字符的最长子串
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 示例 4:
#
# 输入: s = ""
# 输出: 0
#  
# 提示：
#
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        n = len(s)
        res = 0
        r = 0
        for i in range(n):
            if i > 0:
                se.remove(s[i-1])

            while r < n and s[r] not in se:
                se.add(s[r])
                r += 1
            res = max(res, len(se))
        return res

# 567. 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#  
#
# 示例 1：
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 示例 2：
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
#
# 提示：
#
# 1 <= s1.length, s2.length <= 104
# s1 和 s2 仅包含小写字母

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        dics = defaultdict(int)
        n = len(s2)
        left = 0
        right = len(s1) - 1
        for i in s1:
            dic[i] += 1
        for i in s2[:right]:
            dics[i] += 1

        while right < n:
            dics[s2[right]] += 1
            if dic == dics:
                return True
            dics[s2[left]] -= 1
            if dics[s2[left]] == 0:
                dics.pop(s2[left])
            right += 1
            left += 1
        return False