#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230909_207. 课程表.py
# @Author: Lin
# @Date  : 2023/9/9 10:38

"""你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。


提示：

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        # 存储有向图
        for m, n in prerequisites:
            edges[m].append(n)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 判断有向图中是否有环
        valid = True
        def dfs(u):

            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for num in range(numCourses):
            if valid and edges[num]:
                dfs(num)
        # 如果没有环，那么就有拓扑排序
        return valid


sol = Solution()
r = sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])
print(r)

