#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240522_2225. 找出输掉零场或一场比赛的玩家.py
# @Author  ：Lin
# @Date    ：2024/5/22 10:10


"""给你一个整数数组 matches 其中 matches[i] = [winneri, loseri] 表示在一场比赛中 winneri 击败了 loseri 。

返回一个长度为 2 的列表 answer ：
answer[0] 是所有 没有 输掉任何比赛的玩家列表。
answer[1] 是所有恰好输掉 一场 比赛的玩家列表。
两个列表中的值都应该按 递增 顺序返回。
注意：
只考虑那些参与 至少一场 比赛的玩家。
生成的测试用例保证 不存在 两场比赛结果 相同 。
示例 1：
输入：matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
输出：[[1,2,10],[4,5,7,8]]
解释：
玩家 1、2 和 10 都没有输掉任何比赛。
玩家 4、5、7 和 8 每个都输掉一场比赛。
玩家 3、6 和 9 每个都输掉两场比赛。
因此，answer[0] = [1,2,10] 和 answer[1] = [4,5,7,8] 。
示例 2：
输入：matches = [[2,3],[1,3],[5,4],[6,4]]
输出：[[1,2,5,6],[]]
解释：
玩家 1、2、5 和 6 都没有输掉任何比赛。
玩家 3 和 4 每个都输掉两场比赛。
因此，answer[0] = [1,2,5,6] 和 answer[1] = [] 。
提示：
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
所有 matches[i] 互不相同"""
import bisect
from collections import defaultdict, Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]

        winner, loser = set(), defaultdict(int)
        for i, j in matches:
            winner.add(i)
            loser[j] += 1

        for w in winner:
            if w not in loser:
                bisect.insort_right(res[0], w)
        for k, v in loser.items():
            if v == 1:
                bisect.insort_right(res[1], k)
        return res


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]

        freq = Counter()

        for i, j in matches:
            if i not in freq:
                freq[i] = 0
            freq[j] += 1

        for k, v in freq.items():
            if v == 0:
                res[0].append(k)
            elif v == 1:
                res[1].append(k)
        res[0].sort()
        res[1].sort()
        return res


s = Solution()
s.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])