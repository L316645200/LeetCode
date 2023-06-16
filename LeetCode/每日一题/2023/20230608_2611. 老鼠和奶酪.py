#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230608_2611. 老鼠和奶酪.py
# @Author: Lin
# @Date  : 2023/6/8 10:14

#
# 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
# 下标为 i 处的奶酪被吃掉的得分为：
# 如果第一只老鼠吃掉，则得分为 reward1[i] 。
# 如果第二只老鼠吃掉，则得分为 reward2[i] 。
# 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
# 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。
# 示例 1：
# 输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
# 输出：15
# 解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
# 总得分为 4 + 4 + 3 + 4 = 15 。
# 15 是最高得分。
# 示例 2：
# 输入：reward1 = [1,1], reward2 = [1,1], k = 2
# 输出：2
# 解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
# 总得分为 1 + 1 = 2 。
# 2 是最高得分。
# 提示：
# 1 <= n == reward1.length == reward2.length <= 105
# 1 <= reward1[i], reward2[i] <= 1000
# 0 <= k <= n
from heapq import heappush, heappop
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        reward3 = [[reward1[i] - reward2[i], i] for i in range(n)]
        reward3.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        for i in range(k):
            ans += reward1[reward3[i][1]]
        for j in range(k, n):
            ans += reward2[reward3[j][1]]
        return ans


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diffs = [reward1[i] - reward2[i] for i in range(n)]
        diffs.sort(reverse=True)
        ans = sum(reward2)
        for i in range(k):
            ans += diffs[i]
        return ans


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        pq = []
        ans = sum(reward2)
        for i in range(n):
            heappush(pq, reward1[i] - reward2[i])
            if len(pq) > k:
                heappop(pq)
        while pq:
            ans += heappop(pq)
        return ans
s = Solution()
s.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2)