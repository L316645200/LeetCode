#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231118_2342. 数位和相等数对的最大和.py
# @Author  ：Lin
# @Date    ：2023/11/18 9:54

"""给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。

请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。



示例 1：

输入：nums = [18,43,36,13,7]
输出：54
解释：满足条件的数对 (i, j) 为：
- (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
- (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
所以可以获得的最大和是 54 。
示例 2：

输入：nums = [10,12,19,14]
输出：-1
解释：不存在满足条件的数对，返回 -1 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109"""
from typing import List
from collections import defaultdict
import bisect


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # digital_sum
        ds = defaultdict(list)
        res = -1
        for num in nums:
            s = 0
            tnum = num
            while tnum:
                s += tnum % 10
                tnum = tnum // 10
            bisect.insort_right(ds[s], num)
            if len(ds[s]) >= 2:
                res = max(res, ds[s][-1] + ds[s][-2])
        return res



class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # digital_sum
        ds = defaultdict(int)
        res = -1
        for num in nums:
            s = 0
            tnum = num
            while tnum:
                s += tnum % 10
                tnum = tnum // 10
            if ds[s]:
                res = max(res, ds[s] + num)
            # 维护数位和的最大值即可
            ds[s] = max(ds[s], num)
        return res


s = Solution()
s.maximumSum(nums = [18,43,36,13,7])
