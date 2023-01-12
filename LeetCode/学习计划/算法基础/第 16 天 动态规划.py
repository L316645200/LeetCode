#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 16 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/20 16:04

# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 提示：
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
# 进阶：
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
import bisect
from typing import List, Callable


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect.bisect_left(arr, n)] = n
        return len(arr)

s = Solution()
s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])


# 673. 最长递增子序列的个数
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
# 注意 这个数列必须是 严格 递增的。
# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 提示: 
# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        g = [1] * n
        ans = 0
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    g[i] = g[j]
                elif nums[i] == nums[j]:
                    g[i] += g[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = g[i]
            elif dp[i] == max_len:
                ans += g[i]
        return ans
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        g = [1] * n
        max_len = 0
        ans = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        g[i] = g[j]
                    elif dp[i] == dp[j] + 1:
                        g[i] += g[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = g[i]
            elif dp[i] == max_len:
                ans += g[i]

        return ans
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def bisect(n: int, f: Callable[[int], bool]) -> int:
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if f(mid):
                    r = mid
                else:
                    l = mid + 1
            return l
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
            print('d', d)
            print('cnt', cnt)
        return cnt[-1][-1]



s = Solution()
s.findNumberOfLIS(nums = [1,3,2,5,4,7])