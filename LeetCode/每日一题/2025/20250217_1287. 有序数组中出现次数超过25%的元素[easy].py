#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250217_1287. 有序数组中出现次数超过25%的元素[easy].py
# @Author  ：Lin
# @Date    ：2025/2/17 9:17
"""1287. 有序数组中出现次数超过25%的元素

给你一个非递减的有序整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
请你找到并返回这个整数

示例：
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6

提示：
	1 <= arr.length <= 10^4
	0 <= arr[i] <= 10^5


https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2025-02-17"""
import bisect
from collections import defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = defaultdict(int)
        for i, num in enumerate(arr):
            cnt[num] += 1
            if cnt[num] > n // 4:
                return num

"""
思路：因为数组是有序的，且要求的是超过数组总长度1/4的元素
则在数组的每1/4点位上必定会出现该元素，
用二分查询该元素的起始位置，大于1/4*n的即为答案
总时间复杂度为4logn
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = max(n // 4, 1)
        for i in range(m, n, m):
            left = bisect.bisect_left(arr, arr[i])
            right = bisect.bisect_right(arr, arr[i])
            if right - left > m:
                return arr[i]
        return arr[0]
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 4
        for i in (m, m * 2 + 1):
            x = arr[i]
            j = bisect.bisect_left(arr, x)
            if arr[j] == arr[j+m]:
                return arr[j]
        return arr[m * 3 + 2]

s = Solution()
s.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10])
