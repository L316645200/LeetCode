#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：背包问题.py
# @Author  ：Lin
# @Date    ：2024/7/2 19:15


"""
0-1背包
"""
from typing import List

# 动态规划
# def zero_one_backpack(d, w, v):
#     n = len(w)
#     dp = [[0] * (d + 1) for _ in range(n + 1)]
#     for i, x in enumerate(w):
#         for j in range(d+1):
#             if x > j:
#                 dp[i+1][j] = dp[i][j]
#             else:
#                 print(i, x, j)
#                 dp[i+1][j] = max(dp[i][j], dp[i][j-x] + v[i])
#     return dp[-1][-1]
#
#
# zero_one_knapsack(8, [3,5,1,2,2], [4, 5, 2, 1, 3])

# 空间优化
# def zero_one_backpack(d, w, v):
#     n = len(w)
#     dp = [[0] * (d + 1) for _ in range(2)]
#     for i, x in enumerate(w):
#         for j in range(d+1):
#             if x > j:
#                 dp[(i+1) % 2][j] = dp[i % 2][j]
#             else:
#                 print(i, x, j)
#                 dp[(i+1) % 2][j] = max(dp[i % 2][j], dp[i % 2][j-x] + v[i])
#     return dp[n % 2][-1]
# 空间再优化
# def zero_one_backpack(d, w, v):
#     dp = [0] * (d + 1)
#     for i, x in enumerate(w):
#         for j in range(d, x - 1, -1):
#             dp[j] = max(dp[j], dp[j-x] + v[i])
#     return dp[-1]

# zero_one_knapsack(8, [3,5,1,2,2], [4, 5, 2, 1, 3])

"""
多重背包
w: List[int]:每件物品的重量
c: List[int]:每件物品的价值
s: List[int]:每件物品的数量
v: 背包容量
"""


# def multiple_backpack(v: int, w: List[int], c: List[int]):
#     dp = [0] * (v + 1)
#     for i, x in enumerate(w):
#         for j in range(v, x - 1, -1):
#             dp[j] = max(dp[j], dp[j-x] + c[i])
#     print(dp)
class Solution:
    def multiple_backpack(self,v: int, w: List[int], c: List[int]):
        print(w)
        n = len(w)

        dp = [[0] * (v + 1) for _ in range(n + 1)]
        for i, x in enumerate(w):
            for j in range(v+1):
                if x > j:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-x] + c[i])
        print(dp)

        def flash_back(v, n):
            i, j = n, v
            ans = []
            while i != 0:
                print(i,j)
                if dp[i][j] == dp[i-1][j]:
                    i -= 1
                else:
                    i -= 1
                    ans.append(i)
                    j -= w[i]
            return ans
        ans = flash_back(v, n)
        print(ans)

    def binary_optimization(self, temp_w: List[int], temp_c: List[int], s: List[int]):
        # k = 0
        n = len(temp_w)
        w, c = [], []
        for i in range(n):
            j = 1
            while j <= s[i]:
                # k += 1
                w.append(temp_w[i] * j)
                c.append(temp_c[i] * j)
                s[i] -= j
                j <<= 1
            if s[i] != 0:
                # k += 1
                w.append(temp_w[i] * s[i])
                c.append(temp_c[i] * s[i])
        return w, c


    # w = [3,4,2,5]
    # c = [2,3,2,3]
    # s = [2,2,1,4]
    # w, c = binary_optimization(w, c, s)
    # print(w, c)
    # multiple_backpack(10, w, c)

# sol = Solution()
#
# w = [50, 40, 60]
# c = [50, 40, 60]
# s = [20, 15, 10]
#
# w, c = sol.binary_optimization(w, c, s)
# print(w, c)
# sol.multiple_backpack(310, w, c)


"""
完全背包
"""

# 动态规划


def complete_backpack(d, w, v):
    n = len(w)
    dp = [[0] * (d + 1) for _ in range(n + 1)]
    for i, x in enumerate(w):
        for j in range(d+1):
            if x > j:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-x] + v[i])
    return dp[-1][-1]


# 空间优化
def complete_backpack(d, w, v):
    dp = [0] * (d + 1)

    for i, x in enumerate(w):
        for j in range(x, d+1):
            dp[j] = max(dp[j], dp[j-x] + v[i])
    return dp[-1]


complete_backpack(8, [3,5,1,2,2], [4, 5, 2, 1, 3])

























