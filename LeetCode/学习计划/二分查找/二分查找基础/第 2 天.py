#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 2 天.py
# @Author: Lin
# @Date  : 2023/5/13 11:26

# 658. 找到 K 个最接近的元素
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
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 104找到 K 个最接近的元素
# arr 按 升序 排列
# -104 <= arr[i], x <= 104
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid - 1
            else:
                left = mid + 1

        left, right = left - 1, left
        for i in range(k):
            if right == n or (left >= 0 and abs(x - arr[left]) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - k
        while left < right:
            mid = (left + right) // 2
            # print(left, right, abs(x - arr[mid]), abs(arr[mid + k] - x))
            if (x - arr[mid]) <= (arr[mid + k] - x):  # (arr[mid + k] - x)负数时x在右端点的右边
                right = mid
            else:
                left = mid + 1
        # print(arr[left: left+k])
        return arr[left: left + k]
# from typing import List
#
#
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         size = len(arr)
#         left = 0
#         right = size - k
#
#         while left < right:
#             # mid = left + (right - left) // 2
#             mid = (left + right) // 2
#             # 尝试从长度为 k + 1 的连续子区间删除一个元素
#             # 从而定位左区间端点的边界值
#             if x - arr[mid] > arr[mid + k] - x:
#                 # 下一轮搜索区间是 [mid + 1..right]
#                 left = mid + 1
#             else:
#                 # 下一轮搜索区间是 [left..mid]
#                 right = mid
#         return arr[left:left + k]


s = Solution()
s.findClosestElements(arr = [1,1,2,2,2,2,2,3,3], k = 3, x = 3)

# s.findClosestElements(arr = [1], k = 1, x = 1)

# 1894. 找到需要补充粉笔的学生编号
# 一个班级里有 n 个学生，编号为 0 到 n - 1 。每个学生会依次回答问题，编号为 0 的学生先回答，然后是编号为 1 的学生，以此类推，直到编号为 n - 1 的学生，然后老师会重复这个过程，重新从编号为 0 的学生开始回答问题。
# 给你一个长度为 n 且下标从 0 开始的整数数组 chalk 和一个整数 k 。一开始粉笔盒里总共有 k 支粉笔。当编号为 i 的学生回答问题时，他会消耗 chalk[i] 支粉笔。如果剩余粉笔数量 严格小于 chalk[i] ，那么学生 i 需要 补充 粉笔。
# 请你返回需要 补充 粉笔的学生 编号 。
# 示例 1：
# 输入：chalk = [5,1,5], k = 22
# 输出：0
# 解释：学生消耗粉笔情况如下：
# - 编号为 0 的学生使用 5 支粉笔，然后 k = 17 。
# - 编号为 1 的学生使用 1 支粉笔，然后 k = 16 。
# - 编号为 2 的学生使用 5 支粉笔，然后 k = 11 。
# - 编号为 0 的学生使用 5 支粉笔，然后 k = 6 。
# - 编号为 1 的学生使用 1 支粉笔，然后 k = 5 。
# - 编号为 2 的学生使用 5 支粉笔，然后 k = 0 。
# 编号为 0 的学生没有足够的粉笔，所以他需要补充粉笔。
# 示例 2：
# 输入：chalk = [3,4,1,2], k = 25
# 输出：1
# 解释：学生消耗粉笔情况如下：
# - 编号为 0 的学生使用 3 支粉笔，然后 k = 22 。
# - 编号为 1 的学生使用 4 支粉笔，然后 k = 18 。
# - 编号为 2 的学生使用 1 支粉笔，然后 k = 17 。
# - 编号为 3 的学生使用 2 支粉笔，然后 k = 15 。
# - 编号为 0 的学生使用 3 支粉笔，然后 k = 12 。
# - 编号为 1 的学生使用 4 支粉笔，然后 k = 8 。
# - 编号为 2 的学生使用 1 支粉笔，然后 k = 7 。
# - 编号为 3 的学生使用 2 支粉笔，然后 k = 5 。
# - 编号为 0 的学生使用 3 支粉笔，然后 k = 2 。
# 编号为 1 的学生没有足够的粉笔，所以他需要补充粉笔。
# 提示：
# chalk.length == n
# 1 <= n <= 105
# 1 <= chalk[i] <= 105
# 1 <= k <= 109

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        for i in range(1, n):
            chalk[i] = chalk[i] + chalk[i-1]
        k = k % chalk[n-1]
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if chalk[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i


s = Solution()
s.chalkReplacer(chalk = [3,4,1,2], k = 25)


r = s.chalkReplacer(chalk = [5,1,5], k = 27)
print(r)





















