#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250119_2266. 统计打字方案数[medium].py
# @Author  ：Lin
# @Date    ：2025/1/20 9:43
"""2266. 统计打字方案数

Alice 在给 Bob 用手机打字。
数字到字母的 对应如下图所示。
为了 打出一个字母，Alice 需要 按对应字母 i次，i是该字母在这个按键上所处的位置。
	比方说，为了按出字母's'，Alice 需要按'7'四次。类似的， Alice 需要按'5'两次得到字母'k'。
	注意，数字'0' 和'1'不映射到任何字母，所以Alice 不使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息。
	比方说，Alice 发出的信息为"bob"，Bob 将收到字符串"2266622"。
给你一个字符串pressedKeys，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息。
由于答案可能很大，将它对10^9 + 7取余 后返回。

示例 1：
输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。

示例 2：
输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 208287610^3 种 Alice 可能发出的文字信息。
由于我们需要将答案对 10^9 + 7 取余，所以我们返回 208287610^3 % (10^9 + 7) = 82876089 。

提示：
	1 <= pressedKeys.length <= 10^5
	pressedKeys 只包含数字'2'到'9'。


https://leetcode.cn/problems/count-number-of-texts/description/?envType=daily-question&envId=2025-01-19"""
from itertools import groupby


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        res = 1
        mod = 10 ** 9 + 7
        for c, g in groupby(pressedKeys):
            m = len(list(g))
            k = 3 if c not in "79" else 4
            if m <= k:
                res *= 2**(m-1)
            else:
                dp = [0] * m
                for i in range(k):
                    dp[i] = 2**i
                for i in range(k, m):
                    for j in range(k):
                        dp[i] += dp[i-1-j]
                res *= dp[-1]
        return res % mod

mod = 10 ** 9 + 7
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]
for _ in range(10 ** 5 - 3):
    f.append((f[-1] + f[-2] + f[-3]) % mod)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % mod)

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        res = 1
        # print(list(groupby(pressedKeys)))

        for c, gs in groupby(pressedKeys):
            m = len(list(gs))
            res = (g[m] if c in "79" else f[m]) * res % mod
        return res
s = Solution()
s.countTexts(pressedKeys = "2222222")
s.countTexts(pressedKeys = "227777777")
