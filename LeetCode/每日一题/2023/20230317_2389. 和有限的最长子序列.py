#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230317_2389. 和有限的最长子序列.py
# @Author: Lin
# @Date  : 2023/3/17 9:43
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + nums[i-1] if i > 0 else nums[i]
        answer = []
        for target in queries:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            answer.append(left)
        return answer

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = list(accumulate(sorted(nums)))
        return [bisect_right(f, q) for q in queries]


s = Solution()
r =  s.answerQueries(nums = [4,5,2,1], queries = [3,10,21])
print(r)