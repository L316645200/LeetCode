#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240731_3111. 覆盖所有点的最少矩形数目[mid].py
# @Author  ：Lin
# @Date    ：2024/7/31 9:58


"""给你一个二维整数数组 point ，其中 points[i] = [xi, yi] 表示二维平面内的一个点。同时给你一个整数 w 。你需要用矩形 覆盖所有 点。

每个矩形的左下角在某个点 (x1, 0) 处，且右上角在某个点 (x2, y2) 处，其中 x1 <= x2 且 y2 >= 0 ，同时对于每个矩形都 必须 满足 x2 - x1 <= w 。

如果一个点在矩形内或者在边上，我们说这个点被矩形覆盖了。

请你在确保每个点都 至少 被一个矩形覆盖的前提下，最少 需要多少个矩形。

注意：一个点可以被多个矩形覆盖。



示例 1：



输入：points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1

输出：2

解释：

上图展示了一种可行的矩形放置方案：

一个矩形的左下角在 (1, 0) ，右上角在 (2, 8) 。
一个矩形的左下角在 (3, 0) ，右上角在 (4, 8) 。
示例 2：



输入：points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2

输出：3

解释：

上图展示了一种可行的矩形放置方案：

一个矩形的左下角在 (0, 0) ，右上角在 (2, 2) 。
一个矩形的左下角在 (3, 0) ，右上角在 (5, 5) 。
一个矩形的左下角在 (6, 0) ，右上角在 (6, 6) 。
示例 3：



输入：points = [[2,3],[1,2]], w = 0

输出：2

解释：

上图展示了一种可行的矩形放置方案：

一个矩形的左下角在 (1, 0) ，右上角在 (1, 2) 。
一个矩形的左下角在 (2, 0) ，右上角在 (2, 3) 。


提示：

1 <= points.length <= 105
points[i].length == 2
0 <= xi == points[i][0] <= 109
0 <= yi == points[i][1] <= 109
0 <= w <= 109
所有点坐标 (xi, yi) 互不相同。"""
from typing import List


# 贪心+排序
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted([point[0] for point in points])
        res, cur = 1, points[0]
        for p in points:
            if cur + w < p:
                cur = p
                res += 1
        return res

s = Solution()
s.minRectanglesToCoverPoints(points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1)




















