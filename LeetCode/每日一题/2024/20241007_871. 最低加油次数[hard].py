#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241007_871. 最低加油次数[hard].py
# @Author  ：Lin
# @Date    ：2024/10/9 17:48


"""汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
沿途有加油站，用数组 stations 表示。其中 stations[i] = [positioni, fueli] 表示第 i 个加油站位于出发位置东面 positioni 英里处，并且有 fueli 升汽油。
假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
示例 1：
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：可以在不加油的情况下到达目的地。
示例 2：
输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：无法抵达目的地，甚至无法到达第一个加油站。
示例 3：
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
出发时有 10 升燃料。
开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后开车抵达目的地。
沿途在两个加油站停靠，所以返回 2 。
提示：

1 <= target, startFuel <= 109
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 109"""
import heapq
from typing import List


"""思路
可以将加油站看做路过时就可以捡起来且可以随时使用的加油包，因为是要求加油的次数最少，那么我们每次加油加汽油最多的，那么可以用最大堆存储这些加油包。
用end表示当前汽车能达到的英里处，则开始时end=startFuel。此时可以将position在0-end中的加油包捡起来，然后分两种情况讨论：
①end<target时，且有捡起的加油包没用时，使用最大的加油包以达到更远处,然后捡起来这 过程经过的加油包，如粗循环，以end>=target为止。
②end<target 且没有未使用的加油包时，无法达到target处，则返回-1。
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        end = startFuel  # 能到达的英里处
        i, n = 0, len(stations)
        ans = 0
        # 加的油不到终点就一直加油
        while end < target:
            # 将目前能加油的加油站全部添加到堆中
            while i < n and stations[i][0] <= end:
                heapq.heappush(heap, -stations[i][1])
                i += 1
            # 加油先加汽油最多的
            if heap:
                end -= heapq.heappop(heap)
                ans += 1
            else:
                return -1
        return ans


s = Solution()
# s.minRefuelStops(target = 100, statFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]])

s.minRefuelStops(target = 100, startFuel = 50, stations = [[25,25],[50,50]])
