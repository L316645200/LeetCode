#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250221_2209. 用地毯覆盖后的最少白色砖块[hard].py
# @Author  ：Lin
# @Date    ：2025/2/21 17:25
"""2209. 用地毯覆盖后的最少白色砖块

给你一个下标从0开始的 二进制字符串floor，它表示地板上砖块的颜色。
	floor[i] = '0'表示地板上第i块砖块的颜色是 黑色。
	floor[i] = '1'表示地板上第i块砖块的颜色是 白色。
同时给你numCarpets 和carpetLen。你有numCarpets条黑色的地毯，每一条黑色的地毯长度都为carpetLen块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色砖块的数目 最小。地毯相互之间可以覆盖。
请你返回没被覆盖的白色砖块的 最少数目。

示例 1：
输入：floor = "10^110101", numCarpets = 2, carpetLen = 2
输出：2
解释：
上图展示了剩余 2 块白色砖块的方案。
没有其他方案可以使未被覆盖的白色砖块少于 2 块。

示例 2：
输入：floor = "11111", numCarpets = 2, carpetLen = 3
输出：0
解释：
上图展示了所有白色砖块都被覆盖的一种方案。
注意，地毯相互之间可以覆盖。

提示：
	1 <= carpetLen <= floor.length <= 1000
	floor[i] 要么是'0'，要么是'1'。
	1 <= numCarpets <= 1000


https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/description/?envType=daily-question&envId=2025-02-21
"""


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[float('inf')] * (numCarpets+1) for _ in range(n+1)]
        for j in range(numCarpets+1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + (1 if floor[i-1] == '1' else 0)

        for i in range(1, n + 1):
            for j in range(1, numCarpets+1):
                dp[i][j] = dp[i-1][j] + (1 if floor[i-1] == '1' else 0)
                dp[i][j] = min(dp[i][j], dp[max(i-carpetLen, 0)][j-1])
        return dp[n][numCarpets]

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[float('inf')] * (numCarpets+1) for _ in range(n+1)]

        for i in range(numCarpets+1):
            dp[0][i] = 0

        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] + (1 if floor[i-1] == '1' else 0)

        for i in range(1, n+1):
            for j in range(1, numCarpets+1):
                dp[i][j] = dp[i-1][j] + (1 if floor[i-1] == '1' else 0)
                dp[i][j] = min(dp[i][j], dp[max(i-carpetLen, 0)][j-1])
        return dp[n][numCarpets]




s = Solution()
s.minimumWhiteTiles(floor = "10110101", numCarpets = 2, carpetLen = 2)