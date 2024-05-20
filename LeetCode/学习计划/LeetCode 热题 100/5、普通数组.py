#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：5、普通数组.py
# @Author  ：Lin
# @Date    ：2024/5/15 15:02


"""53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组
是数组中的一个连续部分。
示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：
输入：nums = [1]
输出：1
示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。"""
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            res = max(res, nums[i])
        return res

# 前缀和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x  # 当前的前缀和
            ans = max(ans, pre_sum - min_pre_sum)  # 减去前缀和的最小值
            min_pre_sum = min(min_pre_sum, pre_sum)  # 维护前缀和的最小值
        return ans


# s = Solution()
# s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])

"""56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
提示：
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= arr[-1][1]:
                arr[-1] = [arr[-1][0], max(arr[-1][1], intervals[i][1])]
            else:
                arr.append(intervals[i])
        return arr


s = Solution()
s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])

"""
189. 轮转数组
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
提示：
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            arr[(i+k)%n] = nums[i]
        nums[:] = arr


# 翻转[0,n]
# 再分别翻转[0,k-1],[k,n]
def reverse(nums: List[int], left, right) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


s = Solution()
s.rotate(nums = [1,2,3,4,5,6,7], k = 3)


































