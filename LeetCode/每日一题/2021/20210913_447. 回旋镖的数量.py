#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210913_447. 回旋镖的数量.py
# @Author: Lin
# @Date  : 2021/9/13 9:42
# 中等
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
#
# 返回平面上所有回旋镖的数量。
# 示例 1：
# 输入：points = [[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
# 示例 2：
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：2
# 示例 3：
#
# 输入：points = [[1,1]]
# 输出：0
#
# 提示：
#
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -104 <= xi, yi <= 104
# 所有点都 互不相同
from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            points_distance_num = defaultdict(int)
            for j in range(n):
                points_distance_num[self.points_distance(points[i], points[j])] += 1

            for v in points_distance_num.values():
                ans += v * (v-1)
        return int(ans)

    def points_distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


so = Solution()

so.numberOfBoomerangs([[1,1],[2,2],[3,3]])