#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240903_2708. 一个小组的最大实力值[medium].py
# @Author  ：Lin
# @Date    ：2024/9/3 9:24


"""给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为 nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。

请你返回老师创建的小组能得到的最大实力值为多少。



示例 1：

输入：nums = [3,-1,-5,2,5,-9]
输出：1350
解释：一种构成最大实力值小组的方案是选择下标为 [0,2,3,4,5] 的学生。实力值为 3 * (-5) * 2 * 5 * (-9) = 1350 ，这是可以得到的最大实力值。
示例 2：

输入：nums = [-4,-5,-4]
输出：20
解释：选择下标为 [0, 1] 的学生。得到的实力值为 20 。我们没法得到更大的实力值。


提示：

1 <= nums.length <= 13
-9 <= nums[i] <= 9"""
from math import inf
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # 负数数量和零数量
        negative_cnt, zero_cnt = 0, 0
        product = 1
        max_negative = -9  # 最大的负值
        # 求除0以外的乘积
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                if num < 0:
                    negative_cnt += 1
                    max_negative = max(max_negative, num)
                product *= num
        # 如果负数只有一个其余全是0，或者全是0，结果就是0
        if (negative_cnt == 1 and zero_cnt == n - 1) or zero_cnt == n:
            return 0
        elif negative_cnt % 2:  # 如果负数个数为奇数
            return product // max_negative
        return product


s = Solution()
s.maxStrength(nums = [3,-1,-5,2,5,-9])