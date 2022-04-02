#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 11 天 递归_回溯.py
# @Author: Lin
# @Date  : 2022/2/8 17:38


from collections import defaultdict, Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        r = 0
        cnt = defaultdict(str)
        for num in nums:
            r += cnt[num-k] + cnt[num+k]
            cnt[num] += 1
        return r



# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         res = 0
#         cnt = Counter()
#         print(cnt)
#         for num in nums:
#             res += cnt[num - k] + cnt[num + k]
#             cnt[num] += 1
#         return res

s = Solution()
s.countKDifference([1,2,2,1],1)