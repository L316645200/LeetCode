#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230928_2251. 花期内花的数目.py
# @Author: Lin
# @Date  : 2023/9/28 15:16

"""给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。

请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。



示例 1：



输入：flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
输出：[1,2,2,2]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
示例 2：



输入：flowers = [[1,10],[3,3]], people = [3,3,2]
输出：[2,2,1]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。


提示：

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109"""
import bisect
from typing import List
import collections


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = collections.defaultdict(int)
        # 构造差分数组
        for start, end in flowers:
            cnt[start] += 1
            cnt[end+1] -= 1
        arr = sorted(cnt.items())
        people = sorted([[p, i] for i, p in enumerate(people)])
        m = len(people)
        ans = [0] * m
        j, curr = 0, 0
        curr = 0
        for p, i in zip(people, range(m)):
            """在时间点starti上开花的数量增加了1，在时间点endi+1开花的数量减少了1"""

            while j < len(arr) and p[0] >= arr[j][0]:
                curr += arr[j][1]
                j += 1
            ans[p[1]] = curr
        return ans

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = collections.defaultdict(int)
        for start, end in flowers:
            cnt[start] += 1
            cnt[end + 1] -= 1
        arr = sorted(cnt.items())
        m = len(people)
        ans = [0] * m
        j, curr = 0, 0
        for p, i in sorted(zip(people, range(m))):
            while j < len(arr) and p >= arr[j][0]:
                curr += arr[j][1]
                j += 1
            ans[i] += curr
        return ans


# 二分查找
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []
        for i, j in flowers:
            starts.append(i)
            ends.append(j)
        starts.sort()
        ends.sort()
        ans = []
        for p in people:
            x = bisect.bisect_right(starts, p)
            y = bisect.bisect_left(ends, p)
            ans.append(x - y)
        return ans


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect.bisect_right(starts, p) - bisect.bisect_left(ends, p) for p in people]


s = Solution()
s.fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11])
s.fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2])
