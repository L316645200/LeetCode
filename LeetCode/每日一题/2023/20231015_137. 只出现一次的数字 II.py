#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231015_137. 只出现一次的数字 II.py
# @Author: Lin
# @Date  : 2023/10/16 14:23

"""给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。



示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99


提示：

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次"""
from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k, v in cnt:
            if v == 1:
                ans = k
        return ans


s = Solution()
s.singleNumber(nums = [0,1,0,1,0,1,99])