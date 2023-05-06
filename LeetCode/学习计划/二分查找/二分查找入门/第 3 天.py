#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 3 天.py
# @Author: Lin
# @Date  : 2023/3/21 17:22

# 367. 有效的完全平方数
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
#
# 不能使用任何内置的库函数，如  sqrt 。
#
#  
#
# 示例 1：
#
# 输入：num = 16
# 输出：true
# 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
# 示例 2：
#
# 输入：num = 14
# 输出：false
# 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
#  
#
# 提示：
#
# 1 <= num <= 231 - 1
from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left <= right:
            mid = (right - left) // 2 + left
            square = mid ** 2
            if square > num:
                right = mid - 1
            elif square < num:
                left = mid + 1
            else:
                return True
        return False



s = Solution()
s.isPerfectSquare(num = 16)


# 1385. 两个数组间的距离值
# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
#
# 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
#
#  
#
# 示例 1：
#
# 输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# 输出：2
# 解释：
# 对于 arr1[0]=4 我们有：
# |4-10|=6 > d=2
# |4-9|=5 > d=2
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# 所以 arr1[0]=4 符合距离要求
#
# 对于 arr1[1]=5 我们有：
# |5-10|=5 > d=2
# |5-9|=4 > d=2
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# 所以 arr1[1]=5 也符合距离要求
#
# 对于 arr1[2]=8 我们有：
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
# 存在距离小于等于 2 的情况，不符合距离要求
#
# 故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
# 示例 2：
#
# 输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# 输出：2
# 示例 3：
#
# 输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# 输出：1
#  
#
# 提示：
#
# 1 <= arr1.length, arr2.length <= 500
# -10^3 <= arr1[i], arr2[j] <= 10^3
# 0 <= d <= 100

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans, n = 0, len(arr2)
        for v in arr1:
            left, right = 0, n - 1
            left_end_point, right_end_point = v - d, v + d
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] > right_end_point:
                    right = mid - 1
                elif arr2[mid] < left_end_point:
                    left = mid + 1
                else:
                    break
            ans += 1 if left > right else 0
        return ans



s = Solution()
s.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)























