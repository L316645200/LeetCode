#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241106_3254. 长度为 K 的子数组的能量值 I[medium].py
# @Author  ：Lin
# @Date    ：2024/11/6 9:45

"""给你一个长度为 n 的整数数组 nums 和一个正整数 k 。
一个数组的 能量值 定义为：
如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
否则为 -1 。
你需要求出 nums 中所有长度为 k 的
子数组
 的能量值。
请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。
示例 1：
输入：nums = [1,2,3,4,3,2,5], k = 3
输出：[3,4,-1,-1,-1]
解释：
nums 中总共有 5 个长度为 3 的子数组：
[1, 2, 3] 中最大元素为 3 。
[2, 3, 4] 中最大元素为 4 。
[3, 4, 3] 中元素 不是 连续的。
[4, 3, 2] 中元素 不是 上升的。
[3, 2, 5] 中元素 不是 连续的。
示例 2：
输入：nums = [2,2,2,2,2], k = 4
输出：[-1,-1]
示例 3：
输入：nums = [3,2,3,2,3,2], k = 2
输出：[-1,3,-1,3,-1]
提示：
1 <= n == nums.length <= 500
1 <= nums[i] <= 105
1 <= k <= n"""
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n - k + 1)
        # k为1，所有元素都为能量值
        if k == 1:
            return nums
        # 记录滑动窗口连续且上升的次数
        cnt = 0
        # 先记录前k-1个元素有多少是连续且上升的
        for i in range(1, k-1):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
        for i in range(k-1, n):
            # 滑动右指针
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            # 当有k-1次连续上升时，即有一个长度为k的子数组，当前元素即为最大元素，即能量值
            if cnt == k - 1:
                results[i+1-k] = nums[i]
            # 将最左边的元素剔除掉
            if nums[i-k+2] == nums[i-k+1] + 1:
                cnt -= 1
        return results

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n - k + 1)
        cnt = 0
        for i in range(n):
            cnt = 1 if i == 0 or nums[i] - nums[i-1] != 1 else cnt + 1
            if cnt >= k:
                results[i - k + 1] = nums[i]
        return results

s = Solution()
s.resultsArray(nums = [1,2,3,4,3,2,5], k = 3)
# s.resultsArray(nums = [1,3,4], k = 2)
