#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 14 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/19 16:22

# 5. 最长回文子串
# 给你一个字符串 s，找到 s 中最长的回文子串。
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

# 中心扩散
from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        ans = 1
        begin = 0
        for i in range(1, n):
            left = i - 1
            right = i + 1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>ans:
                    ans = right-left+1
                    begin = left
                left -= 1
                right += 1

        for i in range(1, n):
            if s[i] == s[i-1]:
                if 2>ans:
                    ans = 2
                    begin = i-1
                left = i - 2
                right = i + 1
                while left>=0 and right<n and s[left]==s[right]:
                    if right-left+1>ans:
                        ans = right-left+1
                        begin = left
                    left -= 1
                    right += 1
        return s[begin:begin+ans]




s = Solution()
s.longestPalindrome(s = "babad")


# 413. 等差数列划分
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 子数组 是数组中的一个连续序列。
# 示例 1：
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
# 示例 2：
# 输入：nums = [1]
# 输出：0
# 提示：
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
        poor = nums[0]
        arr = []
        n = 1
        for i in range(1, len(nums)):
            if nums[i] == poor:
                n += 1
            else:
                arr.append(n)
                n = 1
                poor = nums[i]
        arr.append(n)
        return sum([(c * (c - 1)) // 2 for c in arr])


s = Solution()
s.numberOfArithmeticSlices(nums = [1])


















