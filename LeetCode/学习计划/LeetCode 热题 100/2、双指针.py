#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2、双指针.py
# @Author  ：Lin
# @Date    ：2024/2/21 11:23

"""283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]
输出: [0]
提示:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
进阶：你能尽量减少完成的操作次数吗？"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        n = len(nums)

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


# s = Solution()
# s.moveZeroes(nums = [0,1,0,3,12])
"""11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：
输入：height = [1,1]
输出：1
提示：
n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res


s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])

"""15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
提示：
3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            # 去除重复的三元组
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                # 去除重复的三元组
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans


s = Solution()
s.threeSum(nums = [-1,0,1,2,-1,-4])


"""42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""



"""对于下标 i，下雨后水能到达的最大高度等于下标i 两边的最大高度的最小值，
下标 i 处能接的雨水量等于下标 i处的水能到达的最大高度减去 height[i]
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # 双指针
        left, right = 0, n - 1
        # 双指针经过的最高点
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res

s = Solution()
s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])




































