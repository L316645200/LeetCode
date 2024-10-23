#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241022_3184. 构成整天的下标对数目 I[easy].py
# @Author  ：Lin
# @Date    ：2024/10/23 11:02

"""给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。

整天 定义为时间持续时间是 24 小时的 整数倍 。

例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。



示例 1：

输入： hours = [12,12,30,24,24]

输出： 2

解释：

构成整天的下标对分别是 (0, 1) 和 (3, 4)。

示例 2：

输入： hours = [72,48,24,3]

输出： 3

解释：

构成整天的下标对分别是 (0, 1)、(0, 2) 和 (1, 2)。



提示：

1 <= hours.length <= 100
1 <= hours[i] <= 109"""
from collections import defaultdict
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for hour in hours:
            hour = hour % 24
            ans += cnt[(24-hour) % 24]
            cnt[hour] += 1
        return ans


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = [0] * 24
        for hour in hours:
            hour = hour % 24
            ans += cnt[(24-hour) % 24]
            cnt[hour] += 1
        return ans
s = Solution()
s.countCompleteDayPairs( hours = [72,48,24,3])