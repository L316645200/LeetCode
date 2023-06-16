#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天.py
# @Author: Lin
# @Date  : 2023/5/19 16:38

# 875. 爱吃香蕉的珂珂
# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
# 珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。
# 示例 1：
# 输入：piles = [3,6,7,11], h = 8
# 输出：4
# 示例 2：
# 输入：piles = [30,11,23,4,20], h = 5
# 输出：30
# 示例 3：
# 输入：piles = [30,11,23,4,20], h = 6
# 输出：23
# 提示：
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
import bisect
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        # k 在1和最大堆根香蕉之间
        while left <= right:
            k = left + (right - left) // 2
            hour = 0
            # 遍历列表累加时间判断是否符合h小时之内
            for pile in piles:
                hour += (pile - 1) // k + 1
            # KEY = sum((pile - 1) // k + 1 for pile in piles)
            if hour <= h:
                right = k - 1
            else:
                left = k + 1
        return left


s = Solution()
s.minEatingSpeed(piles = [3,6,7,11], h = 8)

s.minEatingSpeed(piles = [30,11,23,4,20], h = 5)

s.minEatingSpeed(piles = [30,11,23,4,20], h = 6)



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        r = bisect.bisect_left(range(max(piles)), -h, 1, key=lambda x: -sum((pile - 1) // x + 1 for pile in piles))
        return r

#
#
# s = Solution()
#
# s.minEatingSpeed(piles = [3,6,7,11], h = 8)
#
# s.minEatingSpeed(piles = [30,11,23,4,20], h = 5)
#
# s.minEatingSpeed(piles = [30,11,23,4,20], h = 6)


# 1552. 两球之间的磁力
# 在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
# 已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
# 给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
# 示例 1：
# 输入：position = [1,2,3,4,7], m = 3
# 输出：3
# 解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
# 示例 2：
# 输入：position = [5,4,3,2,1,1000000000], m = 2
# 输出：999999999
# 解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
# 提示：
# n == position.length
# 2 <= n <= 10^5
# 1 <= position[i] <= 10^9
# 所有 position 中的整数 互不相同 。
# 2 <= m <= position.length


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 先排序
        position.sort()
        n = len(position)
        # 答案肯定在1和position[-1] - position[0]之间
        left, right = 1, position[-1] - position[0]
        res = 0
        while left <= right:
            # 二分查找可能的值
            mid = left + (right - left) // 2
            # current当前可能的球位置，num当前放球数目
            current, num = position[0], 1
            # print(left, right, mid)
            # 遍历列表克制当前磁力可以放多少个球
            for i in range(1, n):
                if position[i] - current >= mid:
                    num += 1
                    current = position[i]
            # 球数目大于m说明可能值可以更大，反之减小
            if num >= m:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        # print(res)
        return res


s = Solution()
s.maxDistance(position = [1,2,3,4,5,6,7,8,9,10], m = 4)

























































