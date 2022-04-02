#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211122_384. 打乱数组.py
# @Author: Lin
# @Date  : 2021/11/25 16:23
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_copy = nums.copy()

    def reset(self) -> List[int]:
        return self.nums_copy

    def shuffle(self) -> List[int]:
        return random.shuffle(self.nums)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()