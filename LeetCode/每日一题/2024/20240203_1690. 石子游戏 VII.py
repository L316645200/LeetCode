#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240203_1690. 石子游戏 VII.py
# @Author  ：Lin
# @Date    ：2024/2/3 16:03


"""石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。

有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。当没有石头可移除时，得分较高者获胜。

鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。

给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分的差值 。



示例 1：

输入：stones = [5,3,1,4,2]
输出：6
解释：
- 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
- 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
- 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
- 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
- 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
得分的差值 18 - 12 = 6 。
示例 2：

输入：stones = [7,90,5,1,100,10,10,2]
输出：122


提示：

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000"""
from functools import cache
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre = [0]
        for s in stones:
            pre.append(pre[-1] + s)

        @cache
        def dfs(i, j):
            if i > j:
                return 0
            return max(pre[j+1] - pre[i+1] - dfs(i+1, j), pre[j] - pre[i] - dfs(i, j-1))

        res = dfs(0, len(stones) - 1)
        dfs.cache_clear()
        print(res)
        return res


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        sum_arr = [0] * (n + 1)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            sum_arr[i + 1] = sum_arr[i] + stones[i]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(sum_arr[j+1] - sum_arr[i+1] - dp[i+1][j], sum_arr[j] - sum_arr[i] - dp[i][j-1])
            print(dp)
        print(sum_arr)
        return dp[0][n - 1]
s = Solution()
s.stoneGameVII(stones = [7,90,5,1,100,10,10,2])