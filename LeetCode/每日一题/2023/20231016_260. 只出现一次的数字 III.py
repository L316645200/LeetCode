#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231016_260. 只出现一次的数字 III.py
# @Author: Lin
# @Date  : 2023/10/16 16:51

"""给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。



示例 1：

输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
示例 2：

输入：nums = [-1,0]
输出：[-1,0]
示例 3：

输入：nums = [0,1]
输出：[1,0]


提示：

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
除两个只出现一次的整数外，nums 中的其他数字都出现两次"""
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, occ in freq.items() if occ == 1]
