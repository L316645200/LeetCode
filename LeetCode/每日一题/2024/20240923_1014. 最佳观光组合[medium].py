#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240923_1014. 最佳观光组合[medium].py
# @Author  ：Lin
# @Date    ：2024/9/23 9:41


"""给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

返回一对观光景点能取得的最高分。



示例 1：

输入：values = [8,1,5,2,6]
输出：11
解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
示例 2：

输入：values = [1,2]
输出：2


提示：

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
"""
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        pre = [i for i in range(n)]
        for i in range(n-2, -1, -1):
            j = pre[i+1]
            if values[j] - j + i > values[i]:
                pre[i] = j
        return max([values[i] + values[pre[i+1]] - pre[i+1] + i for i in range(n-1)])


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        pre = [values[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            if pre[i+1] - 1 > values[i]:
                pre[i] = pre[i+1] - 1
        return max([values[i] + pre[i+1] for i in range(n-1)])


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        mx = values[0] + 0
        for j in range(1, len(values)):
            ans = max(ans, mx + values[j] - j)
            mx = max(mx, values[j] + j)
        return ans

s = Solution()
s.maxScoreSightseeingPair(values = [8,1,5,2,6])