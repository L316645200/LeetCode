#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240726_2740. 找出分区值[mid].py
# @Author  ：Lin
# @Date    ：2024/7/27 9:50
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = 10 ** 9
        for i in range(len(nums) - 1):
            res = min(res, nums[i+1] - nums[i])
        return res


s = Solution()
s.findValueOfPartition(nums = [1,3,2,4])
