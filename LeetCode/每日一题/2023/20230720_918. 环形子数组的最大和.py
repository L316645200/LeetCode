#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230720_918. 环形子数组的最大和.py
# @Author: Lin
# @Date  : 2023/7/20 11:34


# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
# 示例 1：
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 示例 2：
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 示例 3：
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
# 提示：
# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104​​​​​​​
from typing import List

# 方法一：动态规划
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        leftmax = [0] * n
        leftmax[0], leftsum = nums[0], nums[0]
        res, pre = nums[0], nums[0]
        for i in range(1, n):
            pre = max(pre + nums[i], nums[i])
            res = max(pre, res)
            leftsum += nums[i]
            leftmax[i] = max(leftmax[i-1], leftsum)

        rightsum = 0
        for j in range(n-1, 0, -1):
            rightsum += nums[j]
            res = max(res, rightsum + leftmax[j - 1])
        return res

# 方法二：取反

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        minpre, maxpre = nums[0], nums[0]
        maxres, minres = nums[0], nums[0]
        s = nums[0]
        for i in range(1, n):
            minpre = max(minpre + nums[i], nums[i])
            minres = max(minpre, minres)
            maxpre = max(maxpre + nums[i], nums[i])
            maxres = max(maxpre, maxres)
            s += nums[i]

        if maxres < 0:
            return maxres
        else:
            return max(maxres, s - minres)


from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        pre, res = nums[0], nums[0]
        q.append((0, pre))
        for i in range(1, 2 * n):
            while len(q) > 0 and q[0][0] < i - n:
                q.popleft()
            pre += nums[i % n]
            res = max(res, pre - q[0][1])
            while len(q) > 0 and q[-1][1] >= pre:
                q.pop()
            q.append((i, pre))
        return res



s = Solution()
s.maxSubarraySumCircular(nums = [5,-3,5])