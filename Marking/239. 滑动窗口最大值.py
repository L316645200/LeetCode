#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：239. 滑动窗口最大值.py
# @Author  ：Lin
# @Date    ：2024/5/23 16:33

"""239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：
输入：nums = [1], k = 1
输出：[1]
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length"""
import heapq
from collections import deque
from typing import List


# 维护一个先进先出队列，长度不超过k，且第一个值的下标与当前下标差值不超过k，超过则弹出第一个值
# 最后进入队列的值如果比前一个进入的值大，可以直接弹出前面进入的值，
# 一直到队列中没有值或者比最后进入的值大为止


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        ans = []

        for i, num in enumerate(nums):
            while deq and deq[-1][0] <= num:
                deq.pop()
            deq.append([num, i])
            if i >= k-1:
                if deq and i - deq[0][1] == k:
                    deq.popleft()
                ans.append(deq[0][0])
        return ans


# 大根堆Onlogn
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]

        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


# 分块和预处理
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix, suffix = [nums[0]] * n, [nums[-1]] * n
        ans = []
        # 前缀最大值
        for i in range(1, n):
            prefix[i] = nums[i] if i % k == 0 else max(prefix[i-1], nums[i])
        # 后缀最大值
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] if (i + 1) % k == 0 else max(suffix[i+1], nums[i])

        # 取前缀最大值和后缀最大值的较大值
        for i in range(k-1, n):
            j = i - k + 1
            if j % k == 0:
                ans.append(prefix[i])
            else:
                ans.append(max(prefix[i], suffix[j]))
        return ans