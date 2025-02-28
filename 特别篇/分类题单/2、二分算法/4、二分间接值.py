#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：4、二分间接值.py
# @Author  ：Lin
# @Date    ：2025/1/23 10:33

"""二分的不是答案，而是一个和答案有关的值（间接值）。
"""
import heapq
from collections import defaultdict
from typing import List

"""3143. 正方形中的最多点数 1697
给你一个二维数组points和一个字符串s，其中points[i]表示第 i个点的坐标，s[i]表示第 i个点的 标签。
如果一个正方形的中心在(0, 0)，所有边都平行于坐标轴，且正方形内不存在标签相同的两个点，那么我们称这个正方形是合法的。
请你返回 合法正方形中可以包含的 最多点数。
注意：
	如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
	正方形的边长可以为零。
示例 1：
输入：points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"
输出：2
解释：
边长为 4 的正方形包含两个点points[0] 和points[1]。
示例 2：
输入：points = [[1,1],[-2,-2],[-2,2]], s = "abb"
输出：1
解释：
边长为 2 的正方形包含 1 个点points[0]。
示例 3：
输入：points = [[1,1],[-1,-1],[2,-2]], s = "ccd"
输出：0
解释：
任何正方形都无法只包含points[0] 和points[1]中的一个点，所以合法正方形中都不包含任何点。
提示：
	1 <= s.length, points.length <= 10^5
	points[i].length == 2
	-10^9 <= points[i][0], points[i][1] <= 10^9
	s.length == points.length
	points中的点坐标互不相同。
	s只包含小写英文字母。
https://leetcode.cn/problems/maximum-points-inside-the-square/description/"""
# 二分
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        left, right = 0, 10 ** 9
        res = 0
        while left <= right:
            mp = set()
            mid = (left + right) // 2
            cnt = 0
            for i, (p, q) in enumerate(points):
                if abs(p) <= mid and abs(q) <= mid:
                    if s[i] not in mp:
                        mp.add(s[i])
                        cnt += 1
                    else:
                        cnt = -1
                        break
            if cnt == -1:
                right = mid - 1
            else:
                res = max(res, cnt)
                left = mid + 1
        return res

# 贪心(维护次小半径)
import math
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min2, mind = float('inf'), defaultdict(lambda: float('inf'))

        for c, (x, y) in zip(s, points):
            d = max(abs(x), abs(y))
            if d < mind[c]:
                min2 = min(min2, mind[c])
                mind[c] = d
            else:
                min2 = min(min2, d)
        return sum(v < min2 for v in mind.values())


s = Solution()
s.maxPointsInsideSquare(points = [[-2,4],[9,3],[-9,3]], s='cca')

"""1648. 销售价值减少的颜色球 2050
你有一些球的库存inventory，里面包含着不同颜色的球。
一个顾客想要任意颜色 总数为orders的球。
这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的同色球的数目。比方说还剩下6个黄球，那么顾客买第一个黄球的时候该黄球的价值为6。这笔交易以后，只剩下5个黄球了，所以下一个黄球的价值为5（也就是球的价值随着顾客购买同色球是递减的）
给你整数数组inventory，其中inventory[i]表示第i种颜色球一开始的数目。同时给你整数orders，表示顾客总共想买的球数目。你可以按照 任意顺序卖球。
请你返回卖了 orders个球以后 最大总价值之和。由于答案可能会很大，请你返回答案对 10^9+ 7取余数的结果。
示例 1：
输入：inventory = [2,5], orders = 4
输出：14
解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
最大总和为 2 + 5 + 4 + 3 = 14 。
示例 2：
输入：inventory = [3,5], orders = 6
输出：19
解释：卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。
最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。
示例 3：
输入：inventory = [2,8,4,10,6], orders = 20
输出：110
示例 4：
输入：inventory = [1000000000], orders = 1000000000
输出：21
解释：卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 10^9 + 7 取余为 21 。
提示：
	1 <= inventory.length <= 10^5
	1 <= inventory[i] <= 10^9
	1 <= orders <= min(sum(inventory[i]), 10^9)
https://leetcode.cn/problems/sell-diminishing-valued-colored-balls/description/"""


# 堆超时
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = [-num for num in inventory]
        heapq.heapify(inventory)
        res, mod = 0, 10 ** 9 + 7
        for i in range(orders):
            k = heapq.heappop(inventory)
            res = (res - k) % mod
            k += 1
            heapq.heappush(inventory, k)
        return res
"""思路：二分
以取完球后剩余的球数目为二分条件
遍历inventory,"""
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 1, max(inventory)
        mod = 10 ** 9 + 7
        while left <= right:
            mid = (left + right) // 2
            cnt1 = cnt2 = 0
            s = 0
            for num in inventory:
                cnt1 += max(num - mid, 0)
                cnt2 += max(num - mid + 1, 0)
                s = (s + (num + mid + 1) * max(num - mid, 0) // 2) % mod
            if cnt1 <= orders <= cnt2:
                return s + (orders - cnt1) * mid
            elif cnt1 > orders:
                left = mid + 1
            else:
                right = mid - 1

s = Solution()
# r = s.maxProfit(inventory = [2,5], orders = 4)
r = s.maxProfit([497978859,167261111,483575207,591815159], orders = 836556809)
print(r)
