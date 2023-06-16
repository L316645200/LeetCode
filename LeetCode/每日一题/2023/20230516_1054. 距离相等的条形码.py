#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230516_1054. 距离相等的条形码.py
# @Author: Lin
# @Date  : 2023/5/16 11:04


# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
# 示例 1：
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 示例 2：
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
# 提示：
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
import heapq
from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        q = []
        for x, cx in count.items():
            heapq.heappush(q, (-cx, x))
        ans = []
        while q:
            cx, x = heapq.heappop(q)
            if ans and ans[-1] == x:
                cy, y = heapq.heappop(q)
                ans.append(y)
                if cy < -1:
                    heapq.heappush(q, (cy + 1, y))
                heapq.heappush(q, (cx, x))
            else:
                ans.append(x)
                if cx < -1:
                    heapq.heappush(q, (cx + 1, x))
        return ans


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        odd_index, even_index = 1, 0
        ans = [0] * n
        cnt = Counter(barcodes)

        for c, cx in cnt.items():
            for i in range(cx):
                if odd_index < n and not (n % 2 == 1 and cx == (n + 1) // 2):
                    ans[odd_index] = c
                    odd_index += 2
                else:
                    ans[even_index] = c
                    even_index += 2
        return ans


s = Solution()
s.rearrangeBarcodes(barcodes = [1,1,1,1,2,2,3,3,3])