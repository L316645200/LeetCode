#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220903_646. 最长数对链.py
# @Author: Lin
# @Date  : 2022/9/3 10:56


# 646. 最长数对链
# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
# 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
# 给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
# 示例：
# 输入：[[1,2], [2,3], [3,4]]
# 输出：2
# 解释：最长的数对链是 [1,2] -> [3,4]
# 提示：
# 给出数对的个数在 [1, 1000] 范围内。
from typing import List


# 排序
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        arr = [pairs[0]]
        for i in range(1, len(pairs)):
            if pairs[i][0] > arr[-1][1]:
                arr.append(pairs[i])
            elif pairs[i][1] < arr[-1][1]:
                arr[-1] = pairs[i]
        return len(arr)


# 排序+原地修改
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = 0
        for i in range(1, len(pairs)):
            if pairs[i][0] > pairs[n][1]:
                pairs[n+1] = pairs[i]
                n += 1
            elif pairs[i][1] < pairs[n][1]:
                pairs[n] = pairs[i]
        return n + 1

s = Solution()
s.findLongestChain([[1,2], [2,3], [3,4]])




class Solution(object):
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res

