#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240918_2332. 坐上公交的最晚时间[medium].py
# @Author  ：Lin
# @Date    ：2024/9/18 10:01


"""给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。
每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。
返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。
注意：数组 buses 和 passengers 不一定是有序的。
示例 1：
输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2
输出：16
解释：
第 1 辆公交车载着第 1 位乘客。
第 2 辆公交车载着你和第 2 位乘客。
注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。
示例 2：
输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
输出：20
解释：
第 1 辆公交车载着第 4 位乘客。
第 2 辆公交车载着第 6 位和第 2 位乘客。
第 3 辆公交车载着第 1 位乘客和你。
提示：
n == buses.length
m == passengers.length
1 <= n, m, capacity <= 105
2 <= buses[i], passengers[i] <= 109
buses 中的元素 互不相同 。
passengers 中的元素 互不相同 。"""
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        m = len(passengers)
        start = left = 0
        print(buses, passengers)
        for bus in buses:
            start = left
            right = min(left + capacity, m) - 1
            while left <= right:
                mid = left + (right - left) // 2
                print(left, right, mid)

                if passengers[mid] <= bus:
                    left = mid + 1
                else:
                    right = mid - 1
        left -= 1
        if start + capacity - 1 > left and passengers[left] < buses[-1]:
            return min(passengers[left+1] - 1, buses[-1]) if left < len(passengers) - 1 else buses[-1]
        while left > 0 and passengers[left - 1] == passengers[left] - 1:
            left -= 1
        return min(passengers[left] - 1, buses[-1])

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n, m = len(buses), len(passengers)
        i = 0
        for bus in buses:
            c = capacity
            while c and i < m and bus >= passengers[i]:
                i += 1
                c -= 1
        i -= 1
        ans = buses[-1] if c else passengers[i]
        while i >= 0 and ans == passengers[i]:
            ans -= 1
            i -= 1
        return ans

s = Solution()
# r = s.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2)
# s.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2)
# r = s.latestTimeCatchTheBus(buses = [3], passengers = [2,4], capacity = 2)
r = s.latestTimeCatchTheBus(buses = [5], passengers = [7,8], capacity = 1)
print(r)
