#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231127_907. 子数组的最小值之和.py
# @Author  ：Lin
# @Date    ：2023/11/27 10:30


"""给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。



示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：

输入：arr = [11,81,94,43,3]
输出：444


提示：

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
 """
from typing import List

# dp[i][j]表示arr[i],arr[i+1],...,arr[j]的最小值
# 则dp[i][j] = min(dp[i][j-1], arr[j])

# 动态规划,内存溢出
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        dp = [[arr[i] for i in range(n)] for j in range(n)]
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = arr[j]
                else:
                    dp[i][j] = min(dp[i][j-1], arr[j])
                res += dp[i][j]
        return res % mod

# 内存优化，超时
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            dp = [0 for i in range(n)]
            for j in range(i, n):
                if i == j:
                    dp[j] = arr[j]
                else:
                    dp[j] = min(dp[j-1], arr[j])

                res += dp[j]
            res = res % mod
        return res


"""若0-i,i是最小值,则dp[i] = arr[i] * (i+1)

若不是最小值, 设j是最小值, 0<j<i，
则 dp[i] = arr[i] * (i-j) + dp[j]
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        mod = 10 ** 9 + 7
        momo_stack = []
        dp = [0] * n
        for i, k in enumerate(arr):
            # 存在单调栈且比当前值大，则往后走
            while momo_stack and arr[momo_stack[-1]] > k:
                momo_stack.pop()

            k = momo_stack[-1] if momo_stack else i + 1
            dp[i] = dp[k] + (i-k) * arr[i] if momo_stack else k * arr[i]
            res = (res + dp[i]) % mod
            momo_stack.append(i)

        return res



s =Solution()
s.sumSubarrayMins([11,81,94,43,3])