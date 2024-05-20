#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240515_2589. 完成所有任务的最少时间.py
# @Author  ：Lin
# @Date    ：2024/5/15 11:45


"""你有一台电脑，它可以 同时 运行无数个任务。给你一个二维整数数组 tasks ，其中 tasks[i] = [starti, endi, durationi] 表示第 i 个任务需要在 闭区间 时间段 [starti, endi] 内运行 durationi 个整数时间点（但不需要连续）。

当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。

请你返回完成所有任务的情况下，电脑最少需要运行多少秒。
示例 1：
输入：tasks = [[2,3,1],[4,5,1],[1,5,2]]
输出：2
解释：
- 第一个任务在闭区间 [2, 2] 运行。
- 第二个任务在闭区间 [5, 5] 运行。
- 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
电脑总共运行 2 个整数时间点。
示例 2：
输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
输出：4
解释：
- 第一个任务在闭区间 [2, 3] 运行
- 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
- 第三个任务在闭区间 [5, 6] 运行。
电脑总共运行 4 个整数时间点。
提示：
1 <= tasks.length <= 2000
tasks[i].length == 3
1 <= starti, endi <= 2000
1 <= durationi <= endi - starti + 1 """
from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 按结束时间排序
        tasks.sort(key=lambda x: x[1])
        # 存储已执行任务的时间点
        mp = set()
        ans = 0
        for start, end, duration in tasks:
            # 遍历求出有多个时间段有任务在运行
            for i in range(start, end + 1):
                if i in mp:
                    duration -= 1
            # 尽量让任务运行在大的时间点
            for j in range(end, start - 1, -1):
                if duration <= 0:
                    break
                if j not in mp:
                    mp.add(j)
                    duration -= 1
                    ans += 1
        return ans

# 空间优化
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ans, m = 0, max(tasks, key=lambda x: x[1])[1]
        for i in range(1, m+1):
            run = False
            for start, end, duration in tasks:
                if duration > 0 and end - duration + 1 == i:
                    run = True
            if run:
                for j, task in enumerate(tasks):
                    if task[0] <= i <= task[1] and task[2] > 0:
                        tasks[j][2] -= 1
                ans += 1
        return ans


s = Solution()
# r = s.findMinimumTime(tasks = [[2,3,1],[4,5,1],[1,5,2]])
r = s.findMinimumTime(tasks = [[8,19,1],[3,20,1],[1,20,2],[6,13,3]])
print(r)


# a = [1,2,3,4,5]
# for i in a:
#     match i:
#         case 1:
#             print(999)
#         case 2:
#             print(222)
#         case 3:
#             print(333)
#         case 4:
#             print(444)

