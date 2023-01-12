#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221026_862. 和至少为 K 的最短子数组.py
# @Author: Lin
# @Date  : 2022/10/26 15:16

# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
# 子数组 是数组中 连续 的一部分。
# 示例 1：
# 输入：nums = [1], k = 1
# 输出：1
# 示例 2：
# 输入：nums = [1,2], k = 4
# 输出：-1
# 示例 3：
# 输入：nums = [2,-1,2], k = 3
# 输出：3
# 提示：
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 109
from collections import deque
from typing import List
# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/liang-zhang-tu-miao-dong-dan-diao-dui-li-9fvh/


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSumArr = [0]
        res = len(nums) + 1
        for num in nums:
            preSumArr.append(preSumArr[-1] + num)
        print(preSumArr)
        q = deque()
        for i, curSum in enumerate(preSumArr):
            print(i, curSum)
            while q and curSum - preSumArr[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and preSumArr[q[-1]] >= curSum:
                q.pop()
            q.append(i)
        return res if res < len(nums) + 1 else -1


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        ans = n
        arr = [0] * n
        for i in range(1, n):
            arr[i] = arr[i-1] + nums[i-1]
        deq = deque([arr[0]])
        for i in range(1, n):
            while deq and arr[i] - arr[deq[0]] >= k:
                ans = min(ans, i - deq[0])
                deq.popleft()
            while deq and arr[i] <= arr[deq[-1]]:
                deq.pop()

            deq.append(i)
        return ans if n > ans else -1


s = Solution()
s.shortestSubarray(nums = [84,-37,32,40,95], k = 167)


