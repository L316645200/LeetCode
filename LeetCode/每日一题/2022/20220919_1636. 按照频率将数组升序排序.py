#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220919_1636. 按照频率将数组升序排序.py
# @Author: Lin
# @Date  : 2022/9/19 11:00

# 给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 
# 请你返回排序后的数组。
# 示例 1：
# 输入：nums = [1,1,2,2,2,3]
# 输出：[3,1,1,2,2,2]
# 解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
# 示例 2：
# 输入：nums = [2,3,1,3,2]
# 输出：[1,3,3,2,2]
# 解释：'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。
# 示例 3：
# 输入：nums = [-1,1,-6,4,5,-6,1,4,1]
# 输出：[5,-1,4,4,-6,-6,1,1,1]
# 提示：
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = sorted(Counter(nums).items(), key=lambda x: [x[1], -x[0]])
        ans = []
        for k, n in arr:
            ans.extend([k] * n)
        return ans



class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        print(nums)
        nums.sort(key=lambda x: (cnt[x], -x))
        print(nums)
        return nums

s = Solution()
s.frequencySort(nums = [1,1,2,2,2,3])
s.frequencySort(nums = [2,3,1,3,2])