#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231029_274. H 指数.py
# @Author  ：Lin
# @Date    ：2023/10/30 17:26
"""给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且每篇论文 至少 被引用 h 次。如果 h 有多种可能的值，h 指数 是其中最大的那个。



示例 1：

输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
示例 2：

输入：citations = [1,3,1]
输出：1


提示：

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        left, right = 0, n - 1
        res = n
        while left <= right:
            mid = (right - left) // 2 + left
            if citations[mid] >= n - mid:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return n - res


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n+1)
        print(counter)

        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        tot = 0
        for i in range(n-1, -1, -1):
            if tot >= i:
                return i
            tot += counter[i]
        return tot


s= Solution()
r = s.hIndex(citations = [3,0,6,1,5])
