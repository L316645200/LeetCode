#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天.py
# @Author: Lin
# @Date  : 2023/5/8 17:33

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
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        pre_sum, left = 0, 0
        for i, n in enumerate(nums):
            pre_sum += n
            while pre_sum >= target:
                ans = min(ans, i - left + 1)
                pre_sum -= nums[left]
                left += 1
        return ans if ans < len(nums) + 1 else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums) + 1
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i - 1]
        ans = n
        for i in range(n):

            left, right = i, n - 1

            while left <= right:
                mid = left + (right - left) // 2
                if prefix_sum[mid] - prefix_sum[i] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < n:
                ans = min(ans, left - i)
        return ans if ans < n else 0


# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0才
#
#         n = len(nums)
#         ans = n + 1
#         sums = [0]
#         for i in range(n):
#             sums.append(sums[-1] + nums[i])
#
#         for i in range(1, n + 1):
#             target = s + sums[i - 1]
#             bound = bisect.bisect_left(sums, target)
#             if bound != len(sums):
#                 ans = min(ans, bound - (i - 1))
#
#         return 0 if ans == n + 1 else ans



s = Solution()
s.minSubArrayLen(target = 11, nums = [1,2,3,4,5])



# 611. 有效三角形的个数
# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
# 示例 1:
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 示例 2:
# 输入: nums = [4,2,3,4]
# 输出: 4
# 提示:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#





class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left, right = j + 1, n - 1
                while left <= right:
                    mid = (right + left) // 2
                    if nums[i] + nums[j] > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += left - j - 1
        return ans


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            k = i
            for j in range(i + 1, n):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1

                ans += max(0, k - j - 1)

        return ans

s = Solution()

r = s.triangleNumber(nums = [2,2,3,4])

print(r)









































































