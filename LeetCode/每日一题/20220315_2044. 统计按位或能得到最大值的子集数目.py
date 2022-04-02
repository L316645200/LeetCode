#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220315_2044. 统计按位或能得到最大值的子集数目.py
# @Author: Lin
# @Date  : 2022/3/15 16:15
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        n = len(nums)

        def hasback(arr, index):
            res.append(arr)
            for i in range(index, n):
                hasback(arr + [nums[i]], i+1)
        hasback([], 0)

        res = [reduce(lambda x, y: x | y, r) for r in res if r]
        return Counter(res).get(max(res))


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        n = len(nums)

        def hasback(val, index):
            res.append(val)
            for i in range(index, n):
                hasback(val | nums[i], i+1)
        hasback(0, 0)
        return Counter(res).get(max(res))


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor, cnt = 0, 0
        def hasback(val, index):
            nonlocal maxor, cnt
            if val > maxor:
                maxor, cnt = val, 1
            elif val == maxor:
                cnt += 1
            for i in range(index, len(nums)):
                hasback(val | nums[i], i+1)
        hasback(0, 0)
        return cnt


s = Solution()
s.countMaxOrSubsets([1,2,3])
