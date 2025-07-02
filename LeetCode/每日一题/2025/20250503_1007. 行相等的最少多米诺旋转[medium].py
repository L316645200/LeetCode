#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/4 18:23
# @Author  : Lin
# @File    : 20250503_1007. 行相等的最少多米诺旋转[medium].py

"""在一排多米诺骨牌中，tops[i] 和 bottoms[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）

我们可以旋转第 i 张多米诺，使得 tops[i] 和 bottoms[i] 的值交换。

返回能使 tops 中所有值或者 bottoms 中所有值都相同的最小旋转次数。

如果无法做到，返回 -1.



示例 1：


输入：tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
输出：2
解释：
图一表示：在我们旋转之前， tops 和 bottoms 给出的多米诺牌。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
示例 2：

输入：tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
输出：-1
解释： 在这种情况下，不可能旋转多米诺牌使一行的值相等。


提示：

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6"""
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        ans, n, mx, num, mark = 0, len(tops), -1, -1, -1
        for x, y in zip(tops, bottoms):
            cnt1[x] += 1
            cnt2[y] += 1
            if cnt1[x] > mx:
                mx = cnt1[x]
                num = x
                mark = 1
            if cnt2[y] > mx:
                mx = cnt2[y]
                num = y
                mark = - 1
        if mx < n / 2:
            return -1
        if mark == -1:
            tops, bottoms = bottoms, tops
        for i in range(n):
            if num != tops[i]:
                tops[i], bottoms[i] = bottoms[i], tops[i]
        return n - mx if len(set(tops)) == 1 or len(set(bottoms)) == 1 else -1



class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def min_rot(target):
            to_top = to_bottom = 0
            for x, y in zip(tops, bottoms):
                if x != target and y != target:
                    return inf
                if x != target:
                    to_top += 1
                if y != target:
                    to_bottom += 1
            return min(to_top, to_bottom)
        ans = min(min_rot(tops[0]), min_rot(bottoms[0]))
        return -1 if ans == inf else ans



s = Solution()
s.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2])



