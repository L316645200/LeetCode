#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天 数组.py
# @Author: Lin
# @Date  : 2021/10/21 15:59
# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x^y,nums)


# 169. 多数元素
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1：
# 输入：[3,2,3]
# 输出：3
# 示例 2：
# 输入：[2,2,1,1,1,2,2]
# 输出：2

# 进阶：
# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)

        return res

# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
#  
# 提示：
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l-2):
            left, right = i + 1, l - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if left - 1 > i and nums[left] == nums[left-1]:
                    left += 1
                elif nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return res


s = Solution()
s.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49])