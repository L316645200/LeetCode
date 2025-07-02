#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/14 12:08
# @Author  : Lin
# @File    : 20250513_3335. 字符串转换后的长度 I[medium].py
"""给你一个字符串 s 和一个整数 t，表示要执行的 转换 次数。每次 转换 需要根据以下规则替换字符串 s 中的每个字符：

如果字符是 'z'，则将其替换为字符串 "ab"。
否则，将其替换为字母表中的下一个字符。例如，'a' 替换为 'b'，'b' 替换为 'c'，依此类推。
返回 恰好 执行 t 次转换后得到的字符串的 长度。

由于答案可能非常大，返回其对 109 + 7 取余的结果。



示例 1：

输入： s = "abcyy", t = 2

输出： 7

解释：

第一次转换 (t = 1)
'a' 变为 'b'
'b' 变为 'c'
'c' 变为 'd'
'y' 变为 'z'
'y' 变为 'z'
第一次转换后的字符串为："bcdzz"
第二次转换 (t = 2)
'b' 变为 'c'
'c' 变为 'd'
'd' 变为 'e'
'z' 变为 "ab"
'z' 变为 "ab"
第二次转换后的字符串为："cdeabab"
最终字符串长度：字符串为 "cdeabab"，长度为 7 个字符。
示例 2：

输入： s = "azbk", t = 1

输出： 5

解释：

第一次转换 (t = 1)
'a' 变为 'b'
'z' 变为 "ab"
'b' 变为 'c'
'k' 变为 'l'
第一次转换后的字符串为："babcl"
最终字符串长度：字符串为 "babcl"，长度为 5 个字符。


提示：

1 <= s.length <= 105
s 仅由小写英文字母组成。
1 <= t <= 105"""
from collections import Counter, defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = defaultdict(int)
        mod = 10 ** 9 + 7
        for x in s:
            cnt[ord(x) - ord('a')] += 1
        for i in range(t):
            cnt_t = defaultdict(int)
            for j in range(26):
                cnt_t[(j+1) % 26] = cnt[j] % mod
            cnt_t[1] += (cnt[25] % mod)
            cnt = cnt_t
        return sum(cnt.values())

s = Solution()
s.lengthAfterTransformations( s = "azbk", t = 1)










