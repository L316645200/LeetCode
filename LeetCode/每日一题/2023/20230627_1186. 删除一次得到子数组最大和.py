#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230627_1186. 删除一次得到子数组最大和.py
# @Author: Lin
# @Date  : 2023/6/27 11:24

# 给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
# 注意，删除一个元素后，子数组 不能为空。
# 示例 1：
# 输入：arr = [1,-2,0,3]
# 输出：4
# 解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
# 示例 2：
# 输入：arr = [1,-2,-2,3]
# 输出：3
# 解释：我们直接选出 [3]，这就是最大和。
# 示例 3：
# 输入：arr = [-1,-1,-1,-1]
# 输出：-1
# 解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
#      我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
# 提示：
# 1 <= arr.length <= 105
# -104 <= arr[i] <= 104
from typing import List


# 暴力超时
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        res = -float('inf')
        for i in range(n):
            mi = 0
            s = arr[i]
            res = max(res, s)
            for j in range(i + 1, n):
                s += arr[j]
                mi = min(mi, arr[j])
                res = max(res, s - mi)
        return res


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp0, dp1, res = arr[0], 0, arr[0]
        for i in range(1, len(arr)):
            dp1 = max(dp1 + arr[i], dp0)
            dp0 = max(dp0, 0) + arr[i]
            res = max(res, dp0, dp1)
        return res


s = Solution()
s.maximumSum(arr = [1,-2,0,3])
s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6])
s.maximumSum(arr = [-1,-1,-1,-1])