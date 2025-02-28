#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241120_3244. 新增道路查询后的最短距离 II[hard].py
# @Author  ：Lin
# @Date    ：2024/11/20 9:16

"""给你一个整数 n 和一个二维整数数组 queries。
有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
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
提示:
3 <= n <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
查询中不存在重复的道路。
不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。"""
from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        prev = [[i-1] for i in range(n)]
        dp = list(range(n))
        res = []
        for x, y in queries:
            prev[y].append(x)

            for i in range(y, n):
                for j in prev[i]:
                    dp[i] = min(dp[i], dp[j] + 1)
            res.append(dp[-1])
        return res


"""记录跳转位置"""

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        f = {i: i + 1 for i in range(n - 1)}
        res = []
        for i, j in queries:
            if i in f and f[i] < j:
                v = f[i]
                while v < j:
                    v = f.pop
                f[i] = j
            res.append(len(f))
        return res

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        f = list(range(1, n))
        k = n - 1
        res = []

        for i, j in queries:
            if f[i] < j:
                v = f[i]
                while v < j:
                    f[v], v = n, f[v]
                    k -= 1
                f[i] = j
            res.append(k)
        return res
s = Solution()
s.shortestDistanceAfterQueries( n = 4, queries = [[0,3],[0,2]])