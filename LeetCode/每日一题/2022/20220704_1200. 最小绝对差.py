#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220704_1200. 最小绝对差.py
# @Author: Lin
# @Date  : 2022/7/4 10:39

# 给你个整数数组 arr，其中每个元素都 不相同。
#
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
# 示例 1：
# 输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
# 示例 2：
# 输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
# 示例 3：
# 输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
# 提示：
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        ans = []
        t = float('inf')
        for i in range(len(arr)-1):
            m = arr[i+1]-arr[i]
            if t == m:
                ans.append([arr[i], arr[i+1]])
            elif m < t:
                ans = [[arr[i], arr[i+1]]]
                t = m
        return ans


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        best, ans = float('inf'), list()
        for i in range(n - 1):
            if (delta := arr[i + 1] - arr[i]) < best:
                best = delta
                ans = [[arr[i], arr[i + 1]]]
            elif delta == best:
                ans.append([arr[i], arr[i + 1]])

        return ans



s = Solution()
s.minimumAbsDifference(arr = [4,2,1,3])