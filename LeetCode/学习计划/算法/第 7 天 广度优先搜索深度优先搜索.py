#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 7 天 广度优先搜索深度优先搜索.py
# @Author: Lin
# @Date  : 2021/7/31 17:36
# 733. 图像渲染
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
#
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
#
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
# 最后返回经过上色渲染后的图像。
#
# 示例 1:
#
# 输入:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析:
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
# 注意:
#
# image 和 image[0] 的长度在范围 [1, 50] 内。
# 给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
# image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        m, n = len(image), len(image[0])
        t = image[sr][sc]
        image[sr][sc] = newColor
        deq = collections.deque([(sr, sc)])
        while deq:
            sr, sc = deq.popleft()
            for i,j in [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]:
                if 0 <= i < m and 0 <= j < n and image[i][j] == t:
                    image[i][j] = newColor
                    deq.append((i, j))
        return image


# 695.岛屿的最大面积
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#
#  
#
# 示例 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
#
# 示例 2:
#
# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。
#
#  
#
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxn = 0
        deq = collections.deque()
        for i in range(m):
            for j in range(n):
                maxt = 0
                if grid[i][j] == 1:
                    deq.append((i, j))
                    grid[i][j] = 0
                    maxt += 1
                    while deq:
                        sr, sc = deq.popleft()
                        for c, v in [(sr-1,sc), (sr+1,sc), (sr,sc-1), (sr,sc+1)]:
                            if 0 <= c < m and 0 <= v < n and grid[c][v] == 1:
                                deq.append((c, v))
                                grid[c][v] = 0
                                maxt += 1
                    maxn = max(maxn, maxt)
        return maxn

