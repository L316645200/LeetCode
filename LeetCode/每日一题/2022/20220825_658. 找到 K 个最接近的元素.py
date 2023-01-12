#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220825_658. 找到 K 个最接近的元素.py
# @Author: Lin
# @Date  : 2022/8/25 9:55


# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
# 整数 a 比整数 b 更接近 x 需要满足：
# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b
# 示例 1：
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
# 示例 2：
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
# 提示：
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr 按 升序 排列
# -104 <= arr[i], x <= 104
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > x:
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1

            else:
                left = mid
                break

        right = left
        left = left - 1

        for i in range(k):
            if right == len(arr) or (left >= 0 and abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
        print(arr[left+1: right])
        return arr[left+1: right]


s = Solution()
s.findClosestElements(arr = [1,2,3,4,5,7,9], k = 4, x = 6)