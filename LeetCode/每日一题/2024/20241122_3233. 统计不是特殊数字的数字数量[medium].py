#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241122_3233. 统计不是特殊数字的数字数量[medium].py
# @Author  ：Lin
# @Date    ：2024/11/22 10:07

"""给你两个 正整数 l 和 r。对于任何数字 x，x 的所有正因数（除了 x 本身）被称为 x 的 真因数。

如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：

数字 4 是 特殊数字，因为它的真因数为 1 和 2。
数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
返回区间 [l, r] 内 不是 特殊数字 的数字数量。



示例 1：

输入： l = 5, r = 7

输出： 3

解释：

区间 [5, 7] 内不存在特殊数字。

示例 2：

输入： l = 4, r = 16

输出： 11

解释：

区间 [4, 16] 内的特殊数字为 4 和 9。



提示：

1 <= l <= r <= 109"""
from math import isqrt


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = isqrt(r)
        res = r - l + 1
        v = [0] * (n + 1)
        for i in range(2, n + 1):
            if v[i] == 0:
                if l <= i * i <= r:
                    res -= 1
                for j in range(i * 2, n + 1, i):
                    v[j] = 1
        return res


s = Solution()
s.nonSpecialCount(4, 100)