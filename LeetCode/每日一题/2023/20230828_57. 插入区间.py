#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230828_57. 插入区间.py
# @Author: Lin
# @Date  : 2023/8/28 11:28

"""给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。



示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]


提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        points = 2
        n = len(intervals)
        for i in range(n):
            if points == 0 or newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                points = 0
                ans.append(newInterval)
                ans.append(intervals[i])
            elif newInterval[1] > intervals[i][1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
            else:
                points = 0
                ans.append([min(newInterval[0], intervals[i][0]), intervals[i][1]])
        if points > 0:
            ans.append(newInterval)
        return ans


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        points = 2
        left, right = newInterval
        for li, ri in intervals:
            if points == 0 or left > ri:
                ans.append([li, ri])
            elif right < li:
                points = 0
                ans.append([left, right])
                ans.append([li, ri])
            elif right > ri:
                left = min(left, li)
            else:
                points = 0
                ans.append([min(left, li), ri])
        if points > 0:
            ans.append([left, right])
        return ans


s = Solution()
s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])