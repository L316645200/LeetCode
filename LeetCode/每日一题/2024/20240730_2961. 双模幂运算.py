#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240730_2961. 双模幂运算.py
# @Author  ：Lin
# @Date    ：2024/7/30 9:28


"""给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [ai, bi, ci, mi]，以及一个整数 target 。

如果满足以下公式，则下标 i 是 好下标：

0 <= i < variables.length
((aibi % 10)ci) % mi == target
返回一个由 好下标 组成的数组，顺序不限 。



示例 1：

输入：variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
输出：[0,2]
解释：对于 variables 数组中的每个下标 i ：
1) 对于下标 0 ，variables[0] = [2,3,3,10] ，(23 % 10)3 % 10 = 2 。
2) 对于下标 1 ，variables[1] = [3,3,3,1] ，(33 % 10)3 % 1 = 0 。
3) 对于下标 2 ，variables[2] = [6,1,1,4] ，(61 % 10)1 % 4 = 2 。
因此，返回 [0,2] 作为答案。
示例 2：

输入：variables = [[39,3,1000,1000]], target = 17
输出：[]
解释：对于 variables 数组中的每个下标 i ：
1) 对于下标 0 ，variables[0] = [39,3,1000,1000] ，(393 % 10)1000 % 1000 = 1 。
因此，返回 [] 作为答案。


提示：

1 <= variables.length <= 100
variables[i] == [ai, bi, ci, mi]
1 <= ai, bi, ci, mi <= 103
0 <= target <= 103"""
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, d) in enumerate(variables):
            if pow(pow(a, b, 10), c, d) == target:
                ans.append(i)
        return ans


# 两次快速幂(pow内置方法即可)
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            x, y = 1, 1
            while b:
                if b & 1:
                    x *= a
                a *= a
                b >>= 1
            t = x % 10

            while c:
                if c & 1:
                    y *= t
                t *= t
                c >>= 1
            if y % m == target:
                ans.append(i)
        return ans


s = Solution()
s.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2)