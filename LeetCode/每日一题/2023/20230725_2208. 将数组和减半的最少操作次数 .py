#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230725_2208. 将数组和减半的最少操作次数 .py
# @Author: Lin
# @Date  : 2023/7/25 9:29
from heapq import heappush, heappop
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heappush(pq, -num)
        s1 = -sum(pq)
        s2 = 0
        res = 0
        while s2 * 2 < s1:
            num = heappop(pq) / 2
            s2 -= num
            heappush(pq, num)
            res += 1
        return res


s = Solution()

s.halveArray(nums = [5,19,8,1])


