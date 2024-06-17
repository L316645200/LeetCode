#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240524_1673. 找出最具竞争力的子序列.py
# @Author  ：Lin
# @Date    ：2024/5/24 15:59

"""给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
示例 1：
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
示例 2：
输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]
提示：
1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length"""
from collections import deque
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)
        res = []
        for i in range(n):
            # 当前元素如果小于前面的元素，说明当前元素更具竞争力
            while deq and deq[-1] > nums[i]:
                deq.pop()
            deq.append(nums[i])
            # 因为子序列长度至少为k，则最具竞争力子序列的第一个值在下标[0,n-k]之间
            if i >= n - k:
                res.append(deq.popleft())
        return res

# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for i, x in enumerate(nums):
#             while len(res) > 0 and len(nums) - i + len(res) > k and res[-1] > x:
#                 res.pop()
#             res.append(x)
#         return res[:k]



# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         res = []
#         for i, num in enumerate(nums):
#             print(res)
#             while res and i < n - k + len(res) and res[-1] > num:
#                 res.pop()
#             res.append(num)
#         return res[:k]


s = Solution()
s.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4)