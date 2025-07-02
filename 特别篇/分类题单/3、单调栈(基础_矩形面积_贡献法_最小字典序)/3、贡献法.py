#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/24 16:06
# @Author  : Lin
# @File    : 3、贡献法.py
"""907. 子数组的最小值之和 1976
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
由于答案可能很大，因此 返回答案模 10^9 + 7 。
示例 1：
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：
输入：arr = [11,81,94,43,3]
输出：444
提示：
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
from math import inf
from typing import List

"""
思路：先处理处两个数组，分别是left表示nums[i]左边第一个小于其的数的下标，和right表示右边第一个小于等于其的数的下标right
之后再遍历nums,对nums[i],以i为最小值的数组数为 (right[i]-nums[i])*(nums[i]-left[i])
细节：left[i]默认为-1,right[i]默认为n,n为数组nums的长度
"""
# 贡献：每个nums[i]作为最小值 在k个数组中，则nums[i]总得贡献了k*nums[i]

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = [-1] * n, [n] * n
        st = []
        ans, mod = 0, 10 ** 9 + 7
        for i in range(n-1, -1, -1):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        st.clear()  # 重置栈
        for i in range(n):
            while st and arr[i] <= arr[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            ans = (ans + (right[i]-i)*(i-left[i]) * arr[i]) % mod
        return ans

# s = Solution()
# s.sumSubarrayMins(arr = [3,1,2,4])
"""2104. 子数组范围和（最大值-最小值） O(n) 做法难度大约 2000
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回 nums 中 所有 子数组范围的 和 。
子数组是数组中一个连续 非空 的元素序列。
示例 1：
输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
示例 2：
输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
示例 3：
输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59
提示：
1 <= nums.length <= 1000
-109 <= nums[i] <= 109
进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？
"""
# 暴力
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            max_val, min_val = nums[i], nums[i]
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                ans += max_val - min_val
        return ans

"""
思路：（贡献法）设以nums[i]为最大值的数组有k个，则nums[i]为答案贡献了nums[i]*k，
最小值同理。
可以先算出以 nums[i]左边第一个大于其的数组left[i],右边第一个大于等于其的数组right[i]（因为nums可能存在重复元素，所以一边要取大于等于），
假设以nums[i]为最大值的子数组为nums[l,...r]
则 left[i]<l<=i, i<=r<right[i]
则nums[i]作为最大值的贡献为 (i-left[i])*(right[i]-i)*nums[i],
最小值同理，最小值贡献值为负
"""
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        right_min, right_max = [n] * n, [n] * n
        stack_min, stack_max = [], []
        for i in range(n-1, -1, -1):
            while stack_max and nums[i] > nums[stack_max[-1]]:
                stack_max.pop()
            if stack_max:
                right_max[i] = stack_max[-1]
            stack_max.append(i)

            while stack_min and nums[i] < nums[stack_min[-1]]:
                stack_min.pop()
            if stack_min:
                right_min[i] = stack_min[-1]
            stack_min.append(i)
        left_min, left_max = [-1] * n, [-1] * n
        stack_min, stack_max = [], []
        ans = 0
        for i in range(n):
            while stack_max and nums[i] >= nums[stack_max[-1]]:
                stack_max.pop()
            if stack_max:
                left_max[i] = stack_max[-1]
            stack_max.append(i)

            while stack_min and nums[i] <= nums[stack_min[-1]]:
                stack_min.pop()
            if stack_min:
                left_min[i] = stack_min[-1]
            stack_min.append(i)
            ans -= (i - left_min[i]) * (right_min[i] - i) * nums[i]
            ans += (i - left_max[i]) * (right_max[i] - i) * nums[i]
        return ans
# s = Solution()
# s.subArrayRanges(nums = [1,3,3])
"""1856. 子数组最小乘积的最大值 2051
一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  109 + 7 取余 的结果。
请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
子数组 定义为一个数组的 连续 部分。
示例 1：
输入：nums = [1,2,3,2]
输出：14
解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。
示例 2：
输入：nums = [2,3,3,1,2]
输出：18
解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
3 * (3+3) = 3 * 6 = 18 。
示例 3：
输入：nums = [3,1,5,6,4,2]
输出：60
解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
4 * (5+6+4) = 4 * 15 = 60 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 107
"""
"""
先处理处两个数组，分别是left表示nums[i]左边第一个小于其的数的下标，和right表示右边第一个小于等于其的数的下标right
之后再遍历nums,对nums[i],以i为最小值的数组数为 (right[i]-nums[i])*(nums[i]-left[i])
细节：left[i]默认为-1,right[i]默认为n,n为数组nums的长度
子数组的和可以用前缀和相减得到
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [-1] * n, [n] * n
        st = []
        pre = [0] * (n+1)
        for i in range(n-1,-1,-1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st.clear()
        for i in range(n):
            while st and nums[i] < nums[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            pre[i+1] = pre[i] + nums[i]
        ans = 0
        for x, l, r in zip(nums, left, right):
            ans = max(ans, x * (pre[r] - pre[l+1]))
        return ans % (10 ** 9 + 7)

# s = Solution()
# s.maxSumMinProduct(nums = [1,2,3,2])
# TODO
"""2818. 操作使得分最大 2397
2281. 巫师的总力量和（最小值×和） 2621
3430. 最多 K 个元素的子数组的最值之和 2645
"""