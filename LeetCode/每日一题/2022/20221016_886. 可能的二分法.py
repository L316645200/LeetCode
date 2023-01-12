#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221016_886. 可能的二分法.py
# @Author: Lin
# @Date  : 2022/10/17 17:44
# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
# 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
# 示例 1：
# 输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
# 示例 2：
# 输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
# 示例 3：
# 输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
# 提示：
# 1 <= n <= 2000
# 0 <= dislikes.length <= 104
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# dislikes 中每一组都 不同
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        print(g)
        color = [0] * n  # color[x] = 0 表示未访问节点 x



s = Solution()
r = s.possibleBipartition(n = 10, dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]])
print(r)