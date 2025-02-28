#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241224_1705. 吃苹果的最大数目[medium].py
# @Author  ：Lin
# @Date    ：2024/12/24 10:56

"""有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。



示例 1：

输入：apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出：7
解释：你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。
示例 2：

输入：apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出：5
解释：你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。


提示：

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
只有在 apples[i] = 0 时，days[i] = 0 才成立"""
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        计算最多可以吃多少个苹果。

        参数:
        apples: 每天新收获的苹果数量列表。
        days: 每天新收获苹果的保存天数列表。

        返回:
        最多吃到的苹果数量。
        """
        # 初始化一个最小堆，用于存储苹果的过期时间
        heap = []
        heapq.heapify(heap)
        # 获取苹果的总数
        n = len(apples)
        # 计算最后一天的天数，确保所有苹果都有足够的时间被食用
        m = n + max(days)
        # 初始化一个数组，用于记录每一天剩余的苹果数量
        wh = [0] * m
        # 初始化结果变量，用于记录总共吃到的苹果数量
        res = 0
        # 遍历每一天，尝试吃苹果
        for i in range(m):
            # 如果当天有新收获的苹果且数量不为零
            if i < n and apples[i] != 0:
                # 将苹果的最后食用期限加入到堆中
                heapq.heappush(heap, i + days[i] - 1)
                # 更新当天剩余的苹果数量
                wh[i + days[i] - 1] += apples[i]
            # 移除已经过期的苹果
            while heap and heap[0] < i:
                heapq.heappop(heap)
            # 如果堆中还有苹果，表示当天可以吃一个苹果
            if heap:
                # 减少当天剩余的苹果数量
                wh[heap[0]] -= 1
                # 如果当天的苹果已经吃完，从堆中移除
                if wh[heap[0]] == 0:
                    heapq.heappop(heap)
                # 更新总共吃到的苹果数量
                res += 1
        # 返回总共吃到的苹果数量
        return res

s = Solution()
# s.eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2])
# s.eatenApples(apples = [3,1,1,0,0,2], days = [3,1,1,0,0,2])
s.eatenApples(apples = [20000], days = [20000])
