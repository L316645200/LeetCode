#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3、滑动窗口.py
# @Author  ：Lin
# @Date    ：2024/2/24 16:58

"""3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成"""
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = 0  # 当前无重复的最小下标
        is_exist = dict()  # 遍历过的字符的最大下标
        res = 0  # 结果值
        for i, c in enumerate(s):
            # 当前字符的最大重复下标
            index = is_exist.get(c, -1)
            # 重复下标是否小于 current
            if index < current:
                res = max(res, i - current + 1)
            else:
                current = index + 1
            # 更新当前字符的最大下标
            is_exist[c] = i
        return res





s = Solution()
s.lengthOfLongestSubstring(s = "pwwkew")




"""438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:
1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slide = [0] * 26
        compare = [0] * 26
        m, n = len(s), len(p)
        if m < n:
            return []
        ans = []
        # 作比较的数组
        for c in p:
            compare[ord(c)-97] += 1
        # 滑动数组
        for i in range(n-1):
            slide[ord(s[i])-97] += 1
        #
        for i in range(m-n+1):
            slide[ord(s[i+n-1])-97] += 1
            if slide == compare:
                ans.append(i)
            slide[ord(s[i])-97] -= 1
        return ans


s = Solution()
s.findAnagrams(s = "cbaebabacd", p = "abc")





































