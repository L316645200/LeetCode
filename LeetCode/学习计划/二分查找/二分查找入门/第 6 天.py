#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天.py
# @Author: Lin
# @Date  : 2023/4/13 11:18

# 441. 排列硬币
#
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
#
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
#
# 示例 1：
#
#
# 输入：n = 5
# 输出：2
# 解释：因为第三行不完整，所以返回 2 。
# 示例 2：
#
#
# 输入：n = 8
# 输出：3
# 解释：因为第四行不完整，所以返回 3 。
from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (right - left) // 2 + left

            pre = (1 + mid) * mid // 2
            if pre > n:
                right = mid - 1
            else:
                left = mid + 1
        return right

s = Solution()

#
# 1539. 第 k 个缺失的正整数
# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
#
# 请你找到这个数组里第 k 个缺失的正整数。
# 示例 1：
# 输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
# 示例 2：
#
# 输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
#  
#
# 提示：
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# 对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
#  
#
# 进阶：
#
# 你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？
#


#
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # if arr[-1] < n + k:
        #     return n + k
        # if arr[0] > k:
        #     return k
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # 设arr中的整数的下标为i，则arr[i]>i+k,必定arr[i]大于第k个缺失值，反之亦成立
            if mid + k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left + k


s = Solution()
r = s.findKthPositive(arr = [2,3,4,8,9], k = 5)
print(r)
print()

r = s.findKthPositive(arr = [3,4,5,6], k = 2)
print(r)

































