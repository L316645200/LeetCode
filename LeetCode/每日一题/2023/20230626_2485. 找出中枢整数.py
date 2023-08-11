#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230626_2485. 找出中枢整数.py
# @Author: Lin
# @Date  : 2023/6/28 10:44

#
# 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：
# 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
# 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。
# 示例 1：
# 输入：n = 8
# 输出：6
# 解释：6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
# 示例 2：
# 输入：n = 1
# 输出：1
# 解释：1 是中枢整数，因为 1 = 1 。
# 示例 3：
# 输入：n = 4
# 输出：-1
# 解释：可以证明不存在满足题目要求的整数。
# 提示：
# 1 <= n <= 1000

class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1 + n) * n // 2
        prefix_sum = 0
        for i in range(1, n + 1):
            prefix_sum += i
            total -= i - 1
            if prefix_sum == total:
                return i
            elif prefix_sum > total:
                return -1

# 二分
class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            prefix_sum = (1 + mid) * mid // 2
            suffix_sum = (mid + n) * (n - mid + 1) // 2
            if prefix_sum == suffix_sum:
                return mid
            elif prefix_sum < suffix_sum:
                left = mid + 1
            else:
                right = mid - 1
        return -1



class Solution:
    def pivotInteger(self, n: int) -> int:
        t = (n ** 2 + n) // 2
        x = int(t ** 0.5)
        if t == x ** 2:
            return x
        return -1




s = Solution()
# r = s.pivotInteger(n = 8)
r = s.pivotInteger(1)
print(r)