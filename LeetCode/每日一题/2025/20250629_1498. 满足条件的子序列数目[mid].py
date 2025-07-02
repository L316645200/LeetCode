#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/29 9:17
# @Author  : Lin
# @File    : 20250629_1498. 满足条件的子序列数目[mid].py
"""给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 109 + 7 取余后返回。
示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
示例 2：
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
示例 3：
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106"""
from typing import List

"""虽然本题要求的是子序列，但由于我们只关心子序列的最小值和最大值，并不关心元素的位置，所以可以先把 nums 排序，从而方便计算
从小到大排序后，对于任意子序列，第一个数一定是最小的，最后一个数一定是最大的。
⚠注意：子序列的最小值和最大值可以是同一个数，此时子序列长度为 1。
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return ans % (10 ** 9 + 7)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        f = [1] + [0] * (n - 1)
        mod = 10 ** 9 + 7
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % mod
        nums.sort()
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += f[right - left]
                left += 1
            else:
                right -= 1
        return ans % mod
s = Solution()
s.numSubseq(nums = [3,5,6,7], target = 9)
