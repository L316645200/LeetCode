#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
from typing import List


# @Time    :2025/3/9 10:32
# @Author  : Lin
# @File    :20250309_第 440 场周赛.py
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m, n = len(fruits), len(baskets)
        mp = set()
        for i, f in enumerate(fruits):
            for j, b in enumerate(baskets):
                if f <= b and j not in mp:
                    mp.add(j)
                    break
        return n - len(mp)

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        nums = list(zip(nums1, nums2, range(n)))
        nums.sort()
        cur = i = 0
        res, heap = [0] * n, []
        heapq.heapify(heap)
        for x, y, z in nums:
            while nums[i][0] < x:
                heapq.heappush(heap, nums[i][1])
                cur += nums[i][1]
                if len(heap) > k:
                    c = heapq.heappop(heap)
                    cur -= c
                i += 1
            res[z] = cur
        return res
s = Solution()
r = s.findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2)
print(r)









