#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 12 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/16 16:58

# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
# 示例 1：
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2：
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 3：
# 输入：nums = [1,2,3]
# 输出：3
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        arr = nums[:]
        arr[1] = max(arr[1], arr[0])
        nums[2] = max(nums[2], nums[1])
        for i in range(2, n-1):
            arr[i] = max(arr[i] + arr[i-2], arr[i-1])

        for i in range(3, n):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])

        return max(nums[-1], arr[-2])


s = Solution()
s.rob(nums = [94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72])

# 55. 跳跃游戏
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
#
# 示例 1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
# 提示：
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] <= 105

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        l, r = 0, 0
        while l <= r:
            nums[l] += l
            r = max(r, nums[l])
            l += 1
            if r >= n:
                return True
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num = 0
        for i in range(len(nums)):
            num = max(num, nums[i] + i)
            if num >= len(nums)-1:
                return True
            if num < i + 1:
                return False

s = Solution()
r = s.canJump([0])
print(r)