#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240913_2398. 预算内的最多机器人数目[hard].py
# @Author  ：Lin
# @Date    ：2024/9/13 11:35

"""你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。
运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes) 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。
请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。
示例 1：
输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
输出：3
解释：
可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 25 。
可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
示例 2：
输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
输出：0
解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
提示：
chargeTimes.length == runningCosts.length == n
1 <= n <= 5 * 104
1 <= chargeTimes[i], runningCosts[i] <= 105
1 <= budget <= 1015"""
from collections import deque
from typing import List

# 二分答案，超时O(nlogn)
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + runningCosts[i]
        left, right = 0, n
        res = 0
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            mark = False
            stack = deque()

            for i in range(n):
                while stack and chargeTimes[stack[-1]] <= chargeTimes[i]:
                    stack.pop()
                while stack and stack[0] <= i - mid:
                    stack.popleft()
                stack.append(i)
                if i + 1 >= mid:
                    total = chargeTimes[stack[0]] + mid * (pre[i+1] - pre[i+1-mid])
                    if total <= budget:
                        print(total, mid, i, stack, pre)
                        mark = True
                        break
            if mark:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        print(res)
        return res


# 单调队列
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        runningCostsSum = 0
        res, stack = 0, deque()
        j = 0
        for i in range(len(chargeTimes)):
            runningCostsSum += runningCosts[i]
            while stack and chargeTimes[stack[-1]] <= chargeTimes[i]:
                stack.pop()
            stack.append(i)

            while j <= i and chargeTimes[stack[0]] + (i - j + 1) * runningCostsSum > budget:
                runningCostsSum -= runningCosts[j]
                j += 1
                while stack and stack[0] <= j - 1:
                    stack.popleft()

            res = max(res, i - j + 1)
        return res


s = Solution()
# s.maximumRobots(chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25)
# s.maximumRobots(chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19)
s.maximumRobots([74,46,19,34,7,87,7,40,28,81,53,39,3,46,21,40,76,44,88,93,44,50,22,59,46,60,36,24,50,40,56,5,39,9,24,74,7,14,95,45,36,17,22,12,53,41,2,33,100,73,20,70,81,91,28,98,47,88,79,100,78,38,44,74,48,76,73,92,28,30,95,87],
                [11,33,15,40,8,28,97,89,51,42,17,57,45,5,63,53,23,43,76,64,86,86,89,53,94,91,78,12,90,29,79,48,35,6,88,79,82,76,44,93,83,55,65,96,86,24,54,65,94,4,26,73,51,85,47,99,17,14,76,2,39,52,58,5,15,35,79,16,94,16,59,50],
                447)