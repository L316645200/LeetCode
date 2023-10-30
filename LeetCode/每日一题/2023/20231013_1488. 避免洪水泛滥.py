#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231013_1488. 避免洪水泛滥.py
# @Author: Lin
# @Date  : 2023/10/13 10:07

"""你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨前是空的，那么它就会装满水。如果第 n 个湖泊下雨前是 满的 ，这个湖泊会发生 洪水 。你的目标是避免任意一个湖泊发生洪水。

给你一个整数数组 rains ，其中：

rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
请返回一个数组 ans ，满足：

ans.length == rains.length
如果 rains[i] > 0 ，那么ans[i] == -1 。
如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。

请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生。



示例 1：

输入：rains = [1,2,3,4]
输出：[-1,-1,-1,-1]
解释：第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，装满水的湖泊包括 [1,2,3]
第四天后，装满水的湖泊包括 [1,2,3,4]
没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。
示例 2：

输入：rains = [1,2,0,0,2,1]
输出：[-1,-1,2,1,-1,-1]
解释：第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，我们抽干湖泊 2 。所以剩下装满水的湖泊包括 [1]
第四天后，我们抽干湖泊 1 。所以暂时没有装满水的湖泊了。
第五天后，装满水的湖泊包括 [2]。
第六天后，装满水的湖泊包括 [1,2]。
可以看出，这个方案下不会有洪水发生。同时， [-1,-1,1,2,-1,-1] 也是另一个可行的没有洪水的方案。
示例 3：

输入：rains = [1,2,0,1,2]
输出：[]
解释：第二天后，装满水的湖泊包括 [1,2]。我们可以在第三天抽干一个湖泊的水。
但第三天后，湖泊 1 和 2 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。


提示：

1 <= rains.length <= 105
0 <= rains[i] <= 109"""
import bisect
from typing import List
from collections import deque



class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 装满水的湖泊 key:i 第i个湖泊 value:j 第i个湖泊出现的下标
        full = dict()
        # 待抽干湖泊的时间
        draned = []
        n = len(rains)
        ans = [1] * n
        for i, rain in enumerate(rains):
            # 如果没有下雨，可以将当前湖泊作为待抽干
            if rain == 0:
                draned.append(i)
            else:
                if rain in full:
                    # 最小的可 待抽干湖泊的时间
                    draned_idx = bisect.bisect(draned, full[rain])
                    if draned_idx >= len(draned):
                        return []
                    # 要被抽干的湖泊下标
                    idx = draned.pop(draned_idx)
                    ans[idx] = rain
                ans[i] = -1
                full[rain] = i
        return ans

from sortedcontainers import SortedList
# SortedList可以将输入的序列进行排序,并且可以保存有序的同时，
# 在O(log(n))的复杂度下完成后续的插入和删除的操作.
# 适合于需要保持序列的有序性同时需要不断修改的情形.
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 装满水的湖泊 key:i 第i个湖泊 value:j 第i个湖泊出现的下标
        full = dict()
        # 待抽干湖泊的时间
        draned = SortedList()
        ans = [1] * len(rains)
        for i, rain in enumerate(rains):
            # 如果没有下雨，可以将当前湖泊作为待抽干
            if rain == 0:
                draned.add(i)
            else:
                if rain in full:
                    # 最小的可 待抽干湖泊的时间
                    draned_idx = draned.bisect(full[rain])
                    if draned_idx == len(draned):
                        return []
                    # 要被抽干的湖泊下标
                    ans[draned[draned_idx]] = rain
                    draned.discard(draned[draned_idx])
                ans[i] = -1
                full[rain] = i
        return ans


s = Solution()
# s.avoidFlood(rains = [1,2,0,0,2,1])

r = s.avoidFlood(rains = [1,0,2,0,2,1])
print(r)