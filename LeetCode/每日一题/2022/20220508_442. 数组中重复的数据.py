#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220508_442. 数组中重复的数据.py
# @Author: Lin
# @Date  : 2022/5/12 10:01

# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。
# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
# 示例 1：
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[2,3]
# 示例 2：
# 输入：nums = [1,1,2]
# 输出：[1]
# 示例 3：
# 输入：nums = [1]
# 输出：[]
# 提示：
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# nums 中的每个元素出现 一次 或 两次
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
            if dic[n] > 1:
                arr.append(n)
        return arr
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [nums[i] for i in range(len(nums)) if nums[i]-1 != i]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans

s = Solution()
s.findDuplicates([4,3,2,7,8,2,3,1])

