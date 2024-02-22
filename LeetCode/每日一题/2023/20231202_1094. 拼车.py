#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231202_1094. 拼车.py
# @Author  ：Lin
# @Date    ：2023/12/5 17:59

"""车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。



示例 1：

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false
示例 2：

输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true


提示：

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105"""
import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = [(trip[2], trip[0]) for trip in trips]
        heapq.heapify(heap)
        print(heap)
        trips.sort(key=lambda x: (x[1], x[2]))
        p = 0
        point, num = heapq.heappop(heap)
        for trip in trips:
            p += trip[0]
            while trip[0] > point:
                p -= num
                point, num = heapq.heappop(heap)
            if p > capacity:
                return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        to_max = max(trip[2] for trip in trips)
        diff = [0] * (to_max + 1)
        for trip in trips:
            diff[trip[1]] += trip[0]
            diff[trip[2]] -= trip[0]
        p = 0
        for d in diff:
            p += d
            if p > capacity:
                return False
        return True


s = Solution()
s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)