#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 21:22
# @Author  : Lin
# @File    : 20250810_869. 重新排序得到 2 的幂[mid].py
"""给定正整数 n ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
示例 1：
输入：n = 1
输出：true
示例 2：
输入：n = 10
输出：false
提示：
1 <= n <= 109"""
from collections import Counter

mp = [Counter(str(2 ** i)) for i in range(30)]

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return Counter(str(n)) in mp


pow_two_sorted_str_set = {''.join(sorted(str(1 << i))) for i in range(30)}

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = ''.join(sorted(str(n)))
        return s in pow_two_sorted_str_set

s = Solution()
s.reorderedPowerOf2(n = 10)