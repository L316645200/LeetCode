#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230519_1079. 活字印刷.py
# @Author: Lin
# @Date  : 2023/5/19 9:48
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 注意：本题中，每个活字字模只能使用一次。
# 示例 1：
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
# 输入："AAABBC"
# 输出：188
# 示例 3：
# 输入："V"
# 输出：1
# 提示：
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        tile = set(tiles)
        print(cnt)

        def dfs(i):
            if i == 0:
                return 1
            res = 0
            for t in tile:
                if cnt[t] > 0:
                    cnt[t] -= 1
                    res += dfs(i - 1)
                    cnt[t] += 1
            return res
        return sum([dfs(i) for i in range(1, len(tiles)+1)])


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        tile = set(tiles)

        def dfs(i):
            if i == 0:
                return 1
            res = 1
            for t in tile:
                if count[t] > 0:
                    count[t] -= 1
                    res += dfs(i - 1)
                    count[t] += 1
            return res

        return dfs(len(tiles)) - 1


s = Solution()
s.numTilePossibilities("AAB")