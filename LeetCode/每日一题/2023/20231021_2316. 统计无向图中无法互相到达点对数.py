#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231021_2316. 统计无向图中无法互相到达点对数.py
# @Author: Lin
# @Date  : 2023/10/21 10:45

"""给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。

请你返回 无法互相到达 的不同 点对数目 。



示例 1：



输入：n = 3, edges = [[0,1],[0,2],[1,2]]
输出：0
解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
示例 2：



输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
输出：14
解释：总共有 14 个点对互相无法到达：
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
所以我们返回 14 。


提示：

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
不会有重复边。"""
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.connect(x, y)
        ans = 0
        for i in range(n):
            ans += n - uf.size[uf.find(i)]
        return ans // 2


# 并查集的实现
class UnionFind:
    def __init__(self, n: int):
        # 创建父节点列表
        self.parents = [i for i in range(n)]
        # 并查集大小
        self.size = [1] * n

    def find(self, x: int) -> int:
        # 路径压缩：沿路径返回时，顺便把x所属的集合改为根节点
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def connect(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            # 小的集合向大的集合 合并
            if self.get_size(rx) < self.get_size(ry):
                self.parents[rx] = self.parents[ry]
                self.size[ry] += self.size[rx]
            else:
                self.parents[ry] = self.parents[rx]
                self.size[rx] += self.size[ry]

    def get_size(self, x) -> int:
        return self.size[x]


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        visited = [False] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(x: int):
            visited[x] = True
            count = 1
            for i in graph[x]:
                if not visited[i]:
                    count += dfs(i)
            return count

        res = 0
        for i in range(n):
            if not visited[i]:
                count = dfs(i)
                res += count * (n - count)
        return res


s = Solution()
s.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]])