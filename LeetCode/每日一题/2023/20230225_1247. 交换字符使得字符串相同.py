#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230225_1247. 交换字符使得字符串相同.py
# @Author: Lin
# @Date  : 2023/2/25 9:34
#
# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。
# 示例 1：
# 输入：s1 = "xx", s2 = "yy"
# 输出：1
# 解释：
# 交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。
# 示例 2：
# 输入：s1 = "xy", s2 = "yx"
# 输出：2
# 解释：
# 交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
# 交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
# 注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
# 示例 3：
# 输入：s1 = "xx", s2 = "xy"
# 输出：-1
# 示例 4：
# 输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# 输出：4
# 提示：
# 1 <= s1.length, s2.length <= 1000
# s1, s2 只包含 'x' 或 'y'。
from collections import Counter, defaultdict


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        n = len(s1)
        cnt, mark = defaultdict(int), 0
        for i in range(n):
            cnt1[s1[i]] += 1
            cnt2[s2[i]] += 1
            if s1[i] != s2[i]:
                cnt[s1[i]] += 1
        x, y = cnt1['x'] + cnt2['x'], cnt1['y'] + cnt2['y']
        if x % 2 == 1 or y % 2 == 1:
            return -1
        if cnt['x'] % 2 == 1:
            mark = 1
        print(cnt['x'])
        return (cnt['x'] + cnt['y']) // 2 + mark


s = Solution()
s.minimumSwap(s1 = "xx", s2 = "yy")

# 官解
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        n = len(s1)
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            if a == 'y' and b == 'x':
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        return xy // 2 + yx // 2 + xy % 2 + yx % 2

