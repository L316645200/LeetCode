#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2745. 构造最长的新字符串.py
# @Author  ：Lin
# @Date    ：2024/4/11 11:49


"""给你三个整数 x ，y 和 z 。

这三个整数表示你有 x 个 "AA" 字符串，y 个 "BB" 字符串，和 z 个 "AB" 字符串。你需要选择这些字符串中的部分字符串（可以全部选择也可以一个都不选择），将它们按顺序连接得到一个新的字符串。新字符串不能包含子字符串 "AAA" 或者 "BBB" 。

请你返回 新字符串的最大可能长度。

子字符串 是一个字符串中一段连续 非空 的字符序列。



示例 1：

输入：x = 2, y = 5, z = 1
输出：12
解释： 我们可以按顺序连接 "BB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AB" ，得到新字符串 "BBAABBAABBAB" 。
字符串长度为 12 ，无法得到一个更长的符合题目要求的字符串。
示例 2：

输入：x = 3, y = 2, z = 2
输出：14
解释：我们可以按顺序连接 "AB" ，"AB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AA" ，得到新字符串 "ABABAABBAABBAA" 。
字符串长度为 14 ，无法得到一个更长的符合题目要求的字符串。


提示：

1 <= x, y, z <= 50"""


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        m = 2 if x != y else 0
        return min(x, y) * 4 + z * 2 + m



s = Solution()
r = s.longestString(x = 2, y = 5, z = 1)
print(
    r
)