#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230501_1376. 通知所有员工所需的时间.py
# @Author: Lin
# @Date  : 2023/5/4 17:16

# 公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。
# 在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。题目保证从属关系可以用树结构显示。
# 公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。
# 第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。
# 返回通知所有员工这一紧急消息所需要的 分钟数 。
# 示例 1：
#
# 输入：n = 1, headID = 0, manager = [-1], informTime = [0]
# 输出：0
# 解释：公司总负责人是该公司的唯一一名员工。
# 示例 2：
# 输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
# 输出：1
# 解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
# 上图显示了公司员工的树结构。
# 提示：
# 1 <= n <= 10^5
# 0 <= headID < n
# manager.length == n
# 0 <= manager[i] < n
# manager[headID] == -1
# informTime.length == n
# 0 <= informTime[i] <= 1000
# 如果员工 i 没有下属，informTime[i] == 0 。
# 题目 保证 所有员工都可以收到通知。
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_dict = defaultdict(list)
        for i, m in enumerate(manager):
            manager_dict[m].append(i)
        ans = []
        def dfs(index, t):
            if not manager_dict[index]:
                ans.append(t)
            else:
                for i in manager_dict[index]:
                    t = informTime[i] + t
                    dfs(i, t)
                    t = t - informTime[i]

        dfs(headID, informTime[headID])
        return max(ans)

s = Solution()
s.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 使用缓存，存储每个节点到根节点的最长时间
        @cache
        def dfs(cur):
            if cur == headID:  # 当前节点为根节点
                return 0
            # 递归遍历当前节点的直属上级节点，返回时间和
            # 由于 informTime 存储的是当前节点通知下属所需时间，所以使用 manager[cur] 获取上级节点
            return dfs(manager[cur]) + informTime[manager[cur]]
        # 对所有节点遍历，返回最长时间
        return max(dfs(i) for i in range(n))
