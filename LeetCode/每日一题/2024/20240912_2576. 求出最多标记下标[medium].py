#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240912_2576. 求出最多标记下标[medium].py
# @Author  ：Lin
# @Date    ：2024/9/12 11:18


"""给你一个下标从 0 开始的整数数组 nums 。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。



示例 1：

输入：nums = [3,5,2,4]
输出：2
解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
示例 2：

输入：nums = [9,2,5,4]
输出：4
解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
示例 3：

输入：nums = [7,6,8]
输出：0
解释：没有任何可以执行的操作，所以答案为 0 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109"""
from typing import List


# 双指针
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = (n - 1) // 2
        res = 0
        left, right = 0, m + 1
        while left <= m and right < n:
            if nums[left] * 2 <= nums[right]:
                res += 2
                left += 1
            right += 1
        return res


# 二分答案
# class Solution:
#     def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         left, right = 0, n // 2 + 1
#         res = 0
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if all([nums[i]*2 <= nums[n-mid+i] for i in range(mid)]):
#                 left += 1
#                 res = mid * 2
#             else:
#                 right -= 1
#         return res
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n // 2 + 1
        res = 0
        while left + 1 < right:
            mid = (left + right) // 2
            if all([nums[i]*2 <= nums[n-mid+i] for i in range(mid)]):
                left = mid
                res = mid * 2
            else:
                right = mid
        return res
s = Solution()
s.maxNumOfMarkedIndices([3,5,2,4])