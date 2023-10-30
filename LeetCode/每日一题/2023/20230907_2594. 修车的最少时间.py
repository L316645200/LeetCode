#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230907_2594. 修车的最少时间.py
# @Author: Lin
# @Date  : 2023/9/8 10:08

"""给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。

同时给你一个整数 cars ，表示总共需要修理的汽车数目。

请你返回修理所有汽车 最少 需要多少时间。

注意：所有机械工可以同时修理汽车。



示例 1：

输入：ranks = [4,2,3,1], cars = 10
输出：16
解释：
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。
示例 2：

输入：ranks = [5,1,8], cars = 6
输出：16
解释：
- 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
- 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
- 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
16 分钟时修理完所有车需要的最少时间。


提示：

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106"""
from typing import List
from collections import deque
import bisect


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort(reverse=True)
        ranks = [[-rank, rank, 1] for rank in ranks]
        ans = 0
        for i in range(cars):
            rank_minutes, rank, minutes = ranks.pop()
            bisect.insort(ranks, [-rank * (minutes + 1) ** 2, rank, minutes+1], key=lambda x: x[0])

        for rank_minutes, rank, minutes in ranks:
            ans = max(ans, rank * (minutes - 1) ** 2)
        return ans
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l , r = 1, ranks[0] * cars * cars
        def check(m: int) -> bool:
            return sum([floor(sqrt(m // x)) for x in ranks]) >= cars
        while l < r:
            m = l + r >> 1
            if check(m):
                r = m
            else:
                l = m + 1
        return l

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, ranks[0] * cars ** 2
        while left <= right:
            mid = (right - left) // 2 + left

            if sum([int(math.sqrt(mid // rank)) for rank in ranks]) >= cars:
                right = mid - 1
            else:
                left = mid + 1
        return left

s = Solution()
s.repairCars(ranks = [4,2,3,1], cars = 10)