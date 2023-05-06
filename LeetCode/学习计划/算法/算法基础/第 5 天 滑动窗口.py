#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 5 天 滑动窗口.py
# @Author: Lin
# @Date  : 2022/6/13 11:02

# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 提示:
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母
from bisect import bisect_right
from math import log
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if p_count == s_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                ans.append(i+1)
        return ans


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        print(count)
        differ = [c != 0 for c in count].count(True)
        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans


s = Solution()
s.findAnagrams(s = "awecbaebabacd", p = "abc")

# 713. 乘积小于 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 示例 1：
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 示例 2：
# 输入：nums = [1,2,3], k = 0
# 输出：0
# 提示: 
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        ans, n = 0, len(nums)
        logPrefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            logPrefix[i + 1] = logPrefix[i] + log(num)

        logK = log(k)
        for j in range(1, n + 1):
            l = bisect_right(logPrefix, logPrefix[j] - logK + 1e-10, 0, j)
            ans += j - l
        return ans


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = len(nums)
        left, right = 0, 0
        product = 1
        ans = 0
        while right < l:
            if product * nums[right] < k:
                product *= nums[right]
                ans += right - left + 1
                right += 1

            else:
                if left == right:
                    right += 1
                else:
                    product //= nums[left]
                left += 1


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, product = 0, 1
        ans = 0
        for i, n in enumerate(nums):
            product *= n
            while product >= k and left <= i:
                product //= nums[left]
                left += 1
            ans += i - left + 1
        return ans


s = Solution()
s.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)





# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 示例 1：
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 提示：
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 进阶：
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        total, left = 0, 0

        for i, n in enumerate(nums):
            total += n
            while total >= target:
                ans = min(ans, i - left + 1)
                total -= nums[left]
                left += 1
        return ans if ans < len(nums) + 1 else 0


s = Solution()
s.minSubArrayLen(target = 11, nums = [1,2,3,4,5])

















