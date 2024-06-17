#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240616_第 402 场周赛.py
# @Author  ：Lin
# @Date    ：2024/6/16 10:29
from collections import Counter
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        is_visited = [0] * 24
        res = 0
        for i in range(len(hours)):
            res += is_visited[(24 - hours[i] % 24) % 24]
            is_visited[hours[i] % 24] += 1
        return res


s = Solution()
s.countCompleteDayPairs(hours = [72,48,24,3])


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        cnt[-3] = 0
        arr = sorted([[k, v, k*v] for k, v in cnt.items()])
        res = arr[1][2]
        for i in range(2, len(arr)):
            j = i - 1
            while arr[j][0] + 2 >= arr[i][0]:
                j -= 1
            arr[i][2] = max(arr[i][2] + arr[j][2], arr[i-1][2])
            res = max(res, arr[i][2])
        return res

# class Solution:
#     def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         ans = []
#         for m, i, j in queries:
#             if m == 2:
#                 nums[i] = j
#             else:
#                 c = 0
#                 for k in range(i+1, j):
#                     if nums[k] > nums[k-1] and nums[k] > nums[k+1]:
#                         c += 1
#                 ans.append(c)
#         return ans

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        is_peak = [0] * n
        for i in range(1, n-1):
            pre[i] = pre[i - 1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                pre[i] += 1
                is_peak[i] = 1
        pre[n-1] = pre[n-2]
        print(pre)
        res = []
        for m, i, j in queries:
            if m == 1:
                ...
            else:

                ...



s = Solution()
s.countOfPeaks(nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]])








