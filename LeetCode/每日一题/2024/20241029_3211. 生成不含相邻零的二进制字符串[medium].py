#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241029_3211. 生成不含相邻零的二进制字符串[medium].py
# @Author  ：Lin
# @Date    ：2024/10/29 9:32


"""给你一个正整数 n。
如果一个二进制字符串 x 的所有长度为 2 的
子字符串
中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。
返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。
示例 1：
输入： n = 3
输出： ["010","011","101","110","111"]
解释：
长度为 3 的有效字符串有："010"、"011"、"101"、"110" 和 "111"。
示例 2：
输入： n = 1
输出： ["0","1"]
解释：
长度为 1 的有效字符串有："0" 和 "1"。
提示：
1 <= n <= 18"""
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(arr: List[str]) -> None:
            if len(arr) == n:
                ans.append(''.join(arr))
            else:
                if not arr or arr[-1] == '1':
                    dfs(arr + ['0'])
                dfs(arr + ['1'])
        dfs([])
        return ans

s = Solution()
s.validStrings(5)
