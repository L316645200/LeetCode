#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 9 天.py
# @Author: Lin
# @Date  : 2023/4/17 17:17
# 1337. 矩阵中战斗力最弱的 K 行
# 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
# 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。
# 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。
# 示例 1：
# 输入：mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# 输出：[2,0,3]
# 解释：
# 每行中的军人数目：
# 行 0 -> 2
# 行 1 -> 4
# 行 2 -> 1
# 行 3 -> 2
# 行 4 -> 5
# 从最弱到最强对这些行排序后得到 [2,0,3,1,4]
# 示例 2：
# 输入：mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# 输出：[0,2]
# 解释：
# 每行中的军人数目：
# 行 0 -> 1
# 行 1 -> 4
# 行 2 -> 1
# 行 3 -> 1
# 从最弱到最强对这些行排序后得到 [0,2,3,1]
# 提示：
# m == mat.length
# n == mat[i].length
# 2 <= n, m <= 100
# 1 <= k <= m
# matrix[i][j] 不是 0 就是 1
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        nums = []
        for i, m in enumerate(mat):
            left, right = 0, len(m) - 1
            while left <= right:
                mid = (left + right) // 2
                if m[mid] == 0:
                    right = mid - 1
                else:
                    left = mid + 1
            nums.append([left, i])
        nums.sort()
        return [nums[i][0] for i in range(k)]


s = Solution()
s.kWeakestRows(mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2)

# 1346. 检查整数及其两倍数是否存在
# 给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。
# 更正式地，检查是否存在两个下标 i 和 j 满足：
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
# 示例 1：
# 输入：arr = [10,2,5,3]
# 输出：true
# 解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。
# 示例 2：
# 输入：arr = [7,1,14,11]
# 输出：true
# 解释：N = 14 是 M = 7 的两倍，即 14 = 2 * 7 。
# 示例 3：
# 输入：arr = [3,1,7,11]
# 输出：false
# 解释：在该情况下不存在 N 和 M 满足 N = 2 * M 。
# 提示：
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        for n in arr:
            if n != 0 and counter[2 * n] >= 1:
                return True
            if n == 0 and counter[2 * n] >= 2:
                return True
        return False



s = Solution()
s.checkIfExist(arr = [7,1,14,11])