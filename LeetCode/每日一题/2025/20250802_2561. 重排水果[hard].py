#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 20:02
# @Author  : Lin
# @File    : 20250802_2561. 重排水果[hard].py
"""你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的交换成本。你想要让两个果篮相等。为此，可以根据需要多次执行下述操作：
选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
交换的成本是 min(basket1i,basket2j) 。
根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。
返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。
示例 1：
输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
输出：1
解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
示例 2：
输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
输出：-1
解释：可以证明无法使两个果篮相等。
提示：
basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1i,basket2i <= 109"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        diff1, diff2 = [], []
        mini = basket1[0]
        key_set = set()
        # 记录两个果篮每个成本的次数
        for x, y in zip(basket1, basket2):
            cnt1[x] += 1
            cnt2[y] += 1
            key_set.update({x, y})  # 所有可能的成本集合
            mini = min(mini, x, y)  # 最小的成本
        # 将不同成本的次数取出来
        for key in key_set:
            k = cnt1[key] - cnt2[key]
            # 果篮无法相等
            if k % 2 != 0:
                return -1
            if k > 0:
                diff1.extend([key] * (k // 2))
            else:
                diff2.extend([key] * (-k // 2))
        diff1.sort()
        diff2.sort()
        ans, m = 0, len(diff1)
        for i in range(m):
            # 取两次交换的较小值，或者用最小的成本去交换两次
            ans += min(diff1[i], diff2[m-1-i], mini * 2)
        return ans

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        diff1, diff2 = [], []
        mini = basket1[0]
        # 记录两个果篮每个成本的次数
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1
            mini = min(mini, x, y)  # 最小的成本
        # 将不同成本的次数取出来
        for k, v in cnt.items():
            # 果篮无法相等
            if v % 2 != 0:
                return -1
            if v > 0:
                diff1.extend([k] * (v // 2))
            else:
                diff2.extend([k] * (-v // 2))
        diff1.sort()
        diff2.sort(reverse=True)
        return sum(min(x, y, mini*2) for x, y in zip(diff1, diff2))


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        diff = []
        mini = basket1[0]
        # 记录两个果篮每个成本的次数
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1
            mini = min(mini, x, y)  # 最小的成本
        # 将不同成本的次数取出来
        for k, v in cnt.items():
            # 果篮无法相等
            if v % 2 != 0:
                return -1
            diff.extend([k] * (abs(v) // 2))
        diff.sort()
        return sum(min(x, mini*2) for x in diff[: len(diff) // 2])


s = Solution()
s.minCost(basket1=[183,259,304,201,128,68,289,346,257,259,300,167,167,289,33,304,382,21,183,252],
          basket2=[97,128,169,21,382,169,201,68,365,183,346,97,300,257,56,183,252,365,33,56])
