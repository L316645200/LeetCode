#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 13 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/16 18:45
# 45. 跳跃游戏 II
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。
# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2
# 提示:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        times = 0
        while l < n-1:
            times += 1
            for i in range(l, r+1):
                if nums[i] + i > r:
                    l = i + 1
                    r = nums[i] + i
                    if r >= n - 1:
                        return times
        return times


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

s = Solution()
s.jump(nums = [2,3,1,1,4])

# 62. 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
# 示例 1：
# 输入：m = 3, n = 7
# 输出：28
# 示例 2：
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 示例 3：
# 输入：m = 7, n = 3
# 输出：28
# 示例 4：
# 输入：m = 3, n = 3
# 输出：6
# 提示：
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 109


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * (n + 1) for _ in range(m+1)]
        arr[1][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[-1][-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[-1][-1]

s = Solution()
s.uniquePaths(m = 7, n = 3)
























