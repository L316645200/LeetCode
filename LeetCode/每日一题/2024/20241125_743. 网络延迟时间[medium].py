#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241125_743. 网络延迟时间[medium].py
# @Author  ：Lin
# @Date    ：2024/11/25 16:44

"""有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。



示例 1：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1
示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1


提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）"""
from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 是否访问过
        visited = {k: 0}
        # 列表转为以u源节点为key的字典
        times_dict = defaultdict(list)
        for u, v, w in times:
            times_dict[u].append([v, w])
        deq = [k]
        while deq:
            t = []
            for u in deq:
                for v, w in times_dict[u]:
                    # 未访问过或者传递时间比原来的少就重新访问
                    if v not in visited or visited[u] + w < visited[v]:
                        visited[v] = visited[u] + w
                        t.append(v)
            deq = t
        return max(visited.values()) if len(visited) == n else -1


"""Dijkstra 算法"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[inf for _ in range(n)] for _ in range(n)]
        for u, v, w in times:
            g[u-1][v-1] = w

        dis = [inf] * n
        dis[k-1] = 0
        done = [False] * n
        while True:

            x = -1
            for i, d in enumerate(done):
                if not d and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0:
                return max(dis)  # 最后一次算出的最短路就是最大的
            if dis[x] == inf:  # 有节点无法到达
                return -1

            for i, d in enumerate(g[x]):
                if dis[x] + d < dis[i]:
                    dis[i] = dis[x] + d
            done[x] = True # 最短路长度已确定（无法变得更小）



s = Solution()
r = s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)

# r = s.networkDelayTime(times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1)
print(r)
