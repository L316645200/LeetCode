#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241119_3243. 新增道路查询后的最短距离 I[medium].py
# @Author  ：Lin
# @Date    ：2024/11/19 10:05

"""给你一个整数 n 和一个二维整数数组 queries。
有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。
示例 1：
输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
输出： [3, 2, 1]
解释：
新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。
新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。
新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。
示例 2：
输入： n = 4, queries = [[0, 3], [0, 2]]
输出： [1, 1]
解释：
新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。
新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。
提示：
3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
查询中没有重复的道路。"""
from collections import defaultdict, deque
from functools import cache
from itertools import count
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        way = [[i + 1] for i in range(n - 1)]
        vis = [-1] * (n + 1)
        res = []
        def bfs(i: int) -> int:
            q = [0]
            for step in count(1):
                tmp = q
                q = []
                for x in tmp:
                    for y in way[x]:
                        if y == n - 1:
                            return step
                        if vis[y] != i:
                            vis[y] = i
                            q.append(y)

        for i, (l, r) in enumerate(queries):
            way[l].append(r)
            res.append(bfs(i))
        return res


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 可以通往当前城市的 其他城市列表
        prev = [[i - 1] for i in range(n)]
        # 通往每个城市的最短距离
        dp = list(range(n))
        res = []
        for u, v in queries:
            # 将新建道路加在 列表
            prev[v].append(u)
            # 新建道路前面的城市最短距离不变，所以从v开始
            for x in range(v, n):
                # 遍历可通往的当前城市的其他城市
                for y in prev[x]:
                    dp[x] = min(dp[x], 1 + dp[y])
            res.append(dp[-1])
        return res


s = Solution()
s.shortestDistanceAfterQueries(n = 5, queries = [[2, 4], [0, 2], [0, 4]])