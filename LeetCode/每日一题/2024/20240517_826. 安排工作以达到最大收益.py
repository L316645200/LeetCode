#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240517_826. 安排工作以达到最大收益.py
# @Author  ：Lin
# @Date    ：2024/5/17 11:34


"""你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:

difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。

举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。



示例 1：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
示例 2:

输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0


提示:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105"""
import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, res = len(difficulty), 0
        idx = sorted((zip(difficulty, profit)))
        deq = []
        # 如果难度小的工作的收益大于难度大的，那么该难度大的工作可以直接排除掉
        for i in range(n):
            if not deq or deq[-1][1] < idx[i][1]:
                deq.append(idx[i])
        for work in worker:
            k = bisect.bisect_right(deq, work, key=lambda x: x[0])
            if k == 0:
                continue
            res += deq[k-1][1]
        return res


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = i = best = 0
        idx = sorted(zip(difficulty, profit))
        print(idx)
        for w in worker:
            while i < len(difficulty) and w >= idx[i][0]:
                best = max(best, idx[i][1])
                i += 1
            res += best
        print(res)
        return res


s = Solution()
s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])

s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])

