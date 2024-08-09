#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240803_3143. 正方形中的最多点数[medium].py
# @Author  ：Lin
# @Date    ：2024/8/3 10:17

"""给你一个二维数组 points 和一个字符串 s ，其中 points[i] 表示第 i 个点的坐标，s[i] 表示第 i 个点的 标签 。
如果一个正方形的中心在 (0, 0) ，所有边都平行于坐标轴，且正方形内 不 存在标签相同的两个点，那么我们称这个正方形是 合法 的。
请你返回 合法 正方形中可以包含的 最多 点数。
注意：
如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
正方形的边长可以为零。
输入：points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"
输出：2
解释：
边长为 4 的正方形包含两个点 points[0] 和 points[1] 。
示例 2：
输入：points = [[1,1],[-2,-2],[-2,2]], s = "abb"
输出：1
解释：
边长为 2 的正方形包含 1 个点 points[0] 。
示例 3：
输入：points = [[1,1],[-1,-1],[2,-2]], s = "ccd"
输出：0
解释：
任何正方形都无法只包含 points[0] 和 points[1] 中的一个点，所以合法正方形中都不包含任何点。
提示：
1 <= s.length, points.length <= 105
points[i].length == 2
-109 <= points[i][0], points[i][1] <= 109
s.length == points.length
points 中的点坐标互不相同。
s 只包含小写英文字母。"""
import math
from collections import defaultdict
from typing import List

# 时间复杂度 nlogn  主要时间在排序
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        p_r = defaultdict(list)
        # 把相同距离的字符放在一起
        for (x, y), val in zip(points, s):
            p_r[max(abs(x), abs(y))].append(val)
        res = 0
        mp = set()
        # 因为距离大的一定包含距离小的，则从小到大遍历
        # 用字典判断字符之前是否出现过
        # 如果当前距离的字符之前都没出现过，则当前距离的字符都是合法的.
        for r in sorted(p_r.keys()):
            for p in p_r[r]:
                if p not in mp:
                    mp.add(p)
                else:
                    return res
            res += len(p_r[r])
        return res

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min2, min_d = float("inf"), defaultdict(lambda: math.inf)

        for (x, y), c in zip(points, s):
            d = max(abs(x), abs(y))
            if d < min_d[c]:
                # d 是目前最小的，那么 min_d[c] 是次小的
                min2 = min(min2, min_d[c])
                min_d[c] = d
            else:
                # d 可能是次小的
                min2 = min(min2, d)
        return sum(d < min2 for d in min_d.values())

s = Solution()
s.maxPointsInsideSquare(points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca")