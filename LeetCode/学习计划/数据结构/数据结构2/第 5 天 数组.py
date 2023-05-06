#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 5 天 数组.py
# @Author: Lin
# @Date  : 2022/10/21 16:35
# 334. 递增的三元子序列
# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
# 示例 2：
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组
# 示例 3：
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
# 提示：
# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
# 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
from collections import Counter, defaultdict
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float('inf'), float('inf')

        for n in nums:
            if n < b:
                if n < a:
                    a = n
                elif n > a:
                    b = n
            elif n > b:
                return True
        return False


s = Solution()
s.increasingTriplet(nums = [1,2,3,4,5])



class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float('inf'), float('inf')

        for n in nums:
            if n > b:
                return True
            elif n < a:
                a = n
            elif a < n < b:
                b = n

        return False

# 238. 除自身以外数组的乘积
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
# 提示：
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        L, R = [1] * n, [1] * n

        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            R[i] = R[i+1] * nums[i+1]

        for i in range(n):
            ans[i] = L[i] * R[i]
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        t = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(n-1, -1, -1):
            t *= nums[i+1] if i < n - 1 else 1
            ans[i] = ans[i] * t
        return ans
s = Solution()
s.productExceptSelf([1,2,3,4])



# 560. 和为 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 提示：
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# 枚举，python超出时间
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s = s + nums[j]
                ans += 1 if s == k else 0
        return ans


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        su, ans = 0, 0
        for num in nums:
            su += num
            ans += prefix[su - k]
            prefix[su] += 1
        return ans


s = Solution()
s.subarraySum(nums = [1,2,1,2,1], k = 3)

s.subarraySum(nums = [1], k = 0)









