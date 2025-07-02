#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 12:14
# @Author  : Lin
# @File    : 20250601_2929. 给小朋友们分糖果 II[mid].py

"""给你两个正整数 n 和 limit 。

请你将 n 颗糖果分给 3 位小朋友，确保没有任何小朋友得到超过 limit 颗糖果，请你返回满足此条件下的 总方案数 。



示例 1：

输入：n = 5, limit = 2
输出：3
解释：总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
示例 2：

输入：n = 3, limit = 3
输出：10
解释：总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。


提示：

1 <= n <= 106
1 <= limit <= 106"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit)+1):
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(n - i - limit, 0) + 1
        return ans
s = Solution()
s.distributeCandies(n = 3, limit = 3)


"""要计算合法方案数（每个小朋友分到的糖果都不超过 limit），
可以先计算所有方案数（没有 limit 限制），
再减去不合法的方案数（至少一个小朋友分到的糖果超过 limit）。
"""

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def c2(n: int):
            return (n - 1) * n // 2 if n > 1 else 0
        return c2(n+2) - 3 * c2(n - (limit + 1) + 2) + 3 * c2(n - 2 * (limit + 1) + 2) - c2(n - 3 * (limit + 1) + 2)
