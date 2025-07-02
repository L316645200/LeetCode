#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/8 14:26
# @Author  : Lin
# @File    : 20250608_386. 字典序排数[mid].py

"""给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
示例 1：
输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
示例 2：
输入：n = 2
输出：[1,2]
提示：
1 <= n <= 5 * 104"""
from typing import List

# 递归
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(i):
            for j in range(10):
                x = i * 10 + j
                if 1 <= x <= n:
                    ans.append(x)
                    dfs(x)
        dfs(0)
        return ans
s = Solution()
s.lexicalOrder(13)
