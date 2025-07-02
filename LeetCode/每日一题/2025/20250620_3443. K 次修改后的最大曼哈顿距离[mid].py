#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/20 9:58
# @Author  : Lin
# @File    : 20250620_3443. K 次修改后的最大曼哈顿距离[mid].py
"""给你一个由字符 'N'、'S'、'E' 和 'W' 组成的字符串 s，其中 s[i] 表示在无限网格中的移动操作：
'N'：向北移动 1 个单位。
'S'：向南移动 1 个单位。
'E'：向东移动 1 个单位。
'W'：向西移动 1 个单位。
初始时，你位于原点 (0, 0)。你 最多 可以修改 k 个字符为任意四个方向之一。
请找出在 按顺序 执行所有移动操作过程中的 任意时刻 ，所能达到的离原点的 最大曼哈顿距离 。
曼哈顿距离 定义为两个坐标点 (xi, yi) 和 (xj, yj) 的横向距离绝对值与纵向距离绝对值之和，即 |xi - xj| + |yi - yj|。
示例 1：
输入：s = "NWSE", k = 1
输出：3
解释：
将 s[2] 从 'S' 改为 'N' ，字符串 s 变为 "NWNE" 。
移动操作	位置 (x, y)	曼哈顿距离	最大值
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。
示例 2：
输入：s = "NSWWEW", k = 3
输出：6
解释：
将 s[1] 从 'S' 改为 'N' ，将 s[4] 从 'E' 改为 'W' 。字符串 s 变为 "NNWWWW" 。
执行移动操作过程中，距离原点的最大曼哈顿距离是 6 。
提示：
1 <= s.length <= 105
0 <= k <= s.length
s 仅由 'N'、'S'、'E' 和 'W' 。"""
from collections import defaultdict


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        cnt = defaultdict(int)  # 字符数
        for c in s:
            cnt[c] += 1
            left = k  # 修改字符的次数
            def f(a: int, b: int):
                nonlocal left
                d = min(a, b, left)  # 最多能修改字符的次数
                left -= d
                return abs(a - b) + d * 2
            ans = max(ans, f(cnt['N'], cnt['S']) + f(cnt['W'], cnt['E']))
        return ans

"""方法二
设当前位置为 (x,y)，当前位置到原点的曼哈顿距离为 ∣x∣+∣y∣。
再看看方法一的这个式子
∣a−b∣+2d
其中 ∣a−b∣ 就是 ∣x∣，d 可以理解为操作次数。所以每操作一次，曼哈顿距离都会增大 2。但这不会超过移动的次数，即 i+1。
所以执行完 s[i] 后的答案为
min(∣x∣+∣y∣+2k,i+1)
"""
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = x = y = 0
        for i, c in enumerate(s):
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'W':
                x += 1
            else:
                x -= 1
            ans = max(ans, min(abs(x) + abs(y) + k * 2, i + 1))
        return ans
