#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240523_2831. 找出最长等值子数组.py
# @Author  ：Lin
# @Date    ：2024/5/23 10:27


"""给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。

从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。

子数组 是数组中一个连续且可能为空的元素序列。
示例 1：
输入：nums = [1,3,2,3,1,3], k = 3
输出：3
解释：最优的方案是删除下标 2 和下标 4 的元素。
删除后，nums 等于 [1, 3, 3, 3] 。
最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
可以证明无法创建更长的等值子数组。
示例 2：
输入：nums = [1,1,2,2,1,1], k = 2
输出：4
解释：最优的方案是删除下标 2 和下标 3 的元素。
删除后，nums 等于 [1, 1, 1, 1] 。
数组自身就是等值子数组，长度等于 4 。
可以证明无法创建更长的等值子数组。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= nums.length
0 <= k <= nums.length"""
from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)

        pos = defaultdict(list)
        # 等值数放在同一个数组中
        for i, num in enumerate(nums):
            pos[num].append(i)
        for v in pos.values():
            j = 0
            for i in range(len(v)):
                while v[i] - v[j] - (i - j) > k:
                    j += 1
                res = max(res, i-j+1)
        return res

"""方法二：一次遍历优化
思路与算法
根据方法一的可知，假设求给定的区间 [l,r][l,r][l,r] 的等值子数组，则此时区间中最优选择的等值元素一定是 nums[l]\textit{nums}[l]nums[l]，且此时满足 nums[l]=nums[r]\textit{nums}[l] = \textit{nums}[r]nums[l]=nums[r]，nums[l]nums[l]nums[l] 为区间 [l,r][l,r][l,r] 的「众数」。最优选择的等值元素为 xxx，当 xxx 为「众数」时需要删除的元素个数最少，如果此时 x≠nums[l]x \neq \textit{nums}[l]x

=nums[l]，则实际还需要删除 nums[l]\textit{nums}[l]nums[l]，相当于多删除了一次，此时应该将 lll 右移，直到 nums[l]=x\textit{nums}[l] = xnums[l]=x。

我们只需要计算满足 x=nums[l]=nums[r]x = \textit{nums}[l] = \textit{nums}[r]x=nums[l]=nums[r] 且 xxx 为众数的最优区间即可，此时如果区间 [l,r][l,r][l,r] 中除 xxx 以外的元素个数小于等于 kkk 即可构成合法的等值子数组。实际计算时，我们枚举区间的右边界 rrr，此时对于左边界 lll：

如果 nums[l]=nums[r]\textit{nums}[l] = \textit{nums}[r]nums[l]=nums[r]，此时在区间 [l,r][l,r][l,r] 中除 nums[l]\textit{nums}[l]nums[l] 以外的元素个数大于 kkk 时，此时需要将区间向右移动；

如果 nums[l]≠nums[r]\textit{nums}[l] \neq \textit{nums}[r]nums[l]

=nums[r]，此时在区间 [l,r][l,r][l,r] 中除 nums[l]\textit{nums}[l]nums[l] 以外的元素个数大于 kkk 时，此时 nums[l]\textit{nums}[l]nums[l] 一定不是目标等值元素 xxx，此时可以跳过 nums[l]\textit{nums}[l]nums[l]，将区间向右移动；

对于最优解来说需要满足 nums[l]=nums[r]\textit{nums}[l] = \textit{nums}[r]nums[l]=nums[r] 且 nums[l]\textit{nums}[l]nums[l] 可做为目标等值元素。只需要统计满足 nums[l]\textit{nums}[l]nums[l] 可以做为等值元素的区间即可，最优解一定包含在该范围中，此时我们需要计算 nums[r]\textit{nums}[r]nums[r] 出现的次数；
"""
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        j = 0
        cnt = defaultdict(int)
        for i, num in enumerate(nums):
            cnt[num] += 1
            while i - j - cnt[nums[j]] + 1 > k:
                cnt[nums[j]] -= 1
                j += 1
            res = max(res, cnt[nums[i]])
        return res


s = Solution()
# s.longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3)
# s.longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2)


r = s.longestEqualSubarray(nums = [3,1,1], k = 2)
print(r)


