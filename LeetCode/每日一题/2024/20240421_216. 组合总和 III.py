#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240421_216. 组合总和 III.py
# @Author  ：Lin
# @Date    ：2024/4/24 10:12


"""找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。



示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
示例 3:

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。


提示:

2 <= k <= 9
1 <= n <= 60"""

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         m = 10 ** 4 + 1
#         @cache
#         def dfs(i, c):
#             if i < 0:
#                 return 0 if c == 0 else m
#             elif c < coins[i]:
#                 return dfs(i-1, c)
#             return min(dfs(i-1, c), dfs(i, c - coins[i]) + 1)
#
#         r = dfs(n -1, amount)
#         return r if r != m else -1
from functools import cache
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(arr, c, target, index, size):
            if c == k and target == 0:  # 判断是否符合条件
                ans.append(arr)
                return
            elif c >= k or target < 0: # 如果使用数字大于等于k或者目标值小于0跳过
                return
            for i in range(index, size): # 递归
                dfs(arr + [i], c + 1, target - i, i + 1, size)
        ans = []
        dfs([], 0, n, 1, 10)
        return ans


s = Solution()
s.combinationSum3(k = 3, n = 9)