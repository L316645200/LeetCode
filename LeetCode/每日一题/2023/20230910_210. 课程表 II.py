#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230910_210. 课程表 II.py
# @Author: Lin
# @Date  : 2023/9/11 12:13

"""现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2：

输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
示例 3：

输入：numCourses = 1, prerequisites = []
输出：[0]


提示：
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
所有[ai, bi] 互不相同"""
from typing import List
from collections import defaultdict, deque


# 深度优先
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        # 存储有向图
        for info in prerequisites:
            edges[info[0]].append(info[1])
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 判断有向图中是否有环
        valid = True
        arr = []

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
            # 将节点入栈 #
            arr.append(u)
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        # 如果没有环，那么就有拓扑排序
        return arr if valid else []


# 广度优先
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = defaultdict(list)
        # 存储每个节点的入度
        indegree = [0] * numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indegree[info[0]] += 1
        # 将所有入度为 0 的节点放入队列中
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []
        while q:
            # 从队首取出一个节点 放入答案中
            u = q.popleft()
            result.append(u)
            for v in edges[u]:
                indegree[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indegree[v] == 0:
                    q.append(v)
        # 答案和总数不等说明还有不能加入答案的课程，则返回空数组
        if len(result) != numCourses:
            return []
        return result


s = Solution()
s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])






























