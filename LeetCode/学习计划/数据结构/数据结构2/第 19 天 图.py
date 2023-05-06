#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 19 天 图.py
# @Author: Lin
# @Date  : 2022/11/23 11:43

# 997. 找到小镇的法官
# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
# 如果小镇法官真的存在，那么：
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
# 示例 1：
# 输入：n = 2, trust = [[1,2]]
# 输出：2
# 示例 2：
# 输入：n = 3, trust = [[1,3],[2,3]]
# 输出：3
# 示例 3：
# 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
# 提示：
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# trust 中的所有trust[i] = [ai, bi] 互不相同
# ai != bi
# 1 <= ai, bi <= n
from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for a, b in trust:
            cnt[b] += 1
        for k, v in cnt.items():
            if v == n - 1:
                for a, b in trust:
                    if a == k:
                        return -1
                return k
        return -1 if n > 1 else 1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        print(list((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0)))
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)



s = Solution()
s.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])
s.findJudge(n = 3, trust = [[1,3],[2,3]])



# 1557. 可以到达所有点的最少点数目
# 给你一个 有向无环图 ， n 个节点编号为 0 到 n-1 ，以及一个边数组 edges ，其中 edges[i] = [fromi, toi] 表示一条从点  fromi 到点 toi 的有向边。
# 找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。
# 你可以以任意顺序返回这些节点编号。
# 示例 1：
# 输入：n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# 输出：[0,3]
# 解释：从单个节点出发无法到达所有节点。从 0 出发我们可以到达 [0,1,2,5] 。从 3 出发我们可以到达 [3,4,2,5] 。所以我们输出 [0,3] 。
# 示例 2：
# 输入：n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# 输出：[0,2,3]
# 解释：注意到节点 0，3 和 2 无法从其他节点到达，所以我们必须将它们包含在结果点集中，这些点都能到达节点 1 和 4 。
# 提示：
# 2 <= n <= 10^5
# 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
# edges[i].length == 2
# 0 <= fromi, toi < n
# 所有点对 (fromi, toi) 互不相同。

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        direct = set()
        arr = []
        for edge in edges:
            direct.add(edge[1])
        for i in range(n):
            if i not in direct:
                arr.append(i)
        return arr
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        direct = set(y for x, y in edges)
        return [i for i in range(n) if i not in direct]

s = Solution()
s.findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]])


# 841. 钥匙和房间
# 有 n 个房间，房间按从 0 到 n - 1 编号。最初，除 0 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。
# 当你进入一个房间，你可能会在里面找到一套不同的钥匙，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。
# 给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。如果能进入 所有 房间返回 true，否则返回 false。
# 示例 1：
# 输入：rooms = [[1],[2],[3],[]]
# 输出：true
# 解释：
# 我们从 0 号房间开始，拿到钥匙 1。
# 之后我们去 1 号房间，拿到钥匙 2。
# 然后我们去 2 号房间，拿到钥匙 3。
# 最后我们去了 3 号房间。
# 由于我们能够进入每个房间，我们返回 true。
# 示例 2：
# 输入：rooms = [[1,3],[3,0,1],[2],[0]]
# 输出：false
# 解释：我们不能进入 2 号房间。
# 提示：
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# 所有 rooms[i] 的值 互不相同

print()

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_set = set(rooms[0])
        arr = rooms[0]
        n = 0
        while n < len(arr):
            for i in rooms[arr[n]]:
                if i not in key_set and i == 0:
                    key_set.add(i)
                    arr.append(i)
            n += 1
        return len(key_set) == len(rooms) - 1


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x):
            vis.add(x)
            nonlocal num
            num += 1
            for i in rooms[x]:
                if i not in vis:
                    dfs(i)

        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return n == num

s = Solution()
s.canVisitAllRooms(rooms = [[1],[1]])





















































