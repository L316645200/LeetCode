#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    :2025/3/10 15:19
# @Author  : Lin
# @File    :20250309_2070. 每一个查询的最大美丽值[medium].py
"""给你一个二维整数数组 items ，其中 items[i] = [pricei, beautyi] 分别表示每一个物品的 价格 和 美丽值 。

同时给你一个下标从 0 开始的整数数组 queries 。对于每个查询 queries[j] ，你想求出价格小于等于 queries[j] 的物品中，最大的美丽值 是多少。如果不存在符合条件的物品，那么查询的结果为 0 。

请你返回一个长度与 queries 相同的数组 answer，其中 answer[j]是第 j 个查询的答案。



示例 1：

输入：items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
输出：[2,4,5,5,6,6]
解释：
- queries[0]=1 ，[1,2] 是唯一价格 <= 1 的物品。所以这个查询的答案为 2 。
- queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。
  它们中的最大美丽值为 4 。
- queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。
  它们中的最大美丽值为 5 。
- queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。
  所以，答案为所有物品中的最大美丽值，为 6 。
示例 2：

输入：items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
输出：[4]
解释：
每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。
注意，多个物品可能有相同的价格和美丽值。
示例 3：

输入：items = [[10,1000]], queries = [5]
输出：[0]
解释：
没有物品的价格小于等于 5 ，所以没有物品可以选择。
因此，查询的结果为 0 。


提示：

1 <= items.length, queries.length <= 105
items[i].length == 2
1 <= pricei, beautyi, queries[j] <= 109"""
import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.append([0, 0])
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i-1][1], items[i][1])
        n = len(queries)
        ans = [0] * n

        for j, price in enumerate(queries):
            k = bisect.bisect_right(items, price, key=lambda x: x[0])
            ans[j] = items[k-1][1]
        return ans


s = Solution()
s.maximumBeauty(items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]],
                queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584])
