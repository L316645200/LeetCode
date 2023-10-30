#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231025_2698. 求一个整数的惩罚数.py
# @Author: Lin
# @Date  : 2023/10/25 11:58

"""给你一个正整数 n ，请你返回 n 的 惩罚数 。

n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：

1 <= i <= n
i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。


示例 1：

输入：n = 10
输出：182
解释：总共有 3 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
因此，10 的惩罚数为 1 + 81 + 100 = 182
示例 2：

输入：n = 37
输出：1478
解释：总共有 4 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
- 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478


提示：

1 <= n <= 1000"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, index: int, star: int, target: int) -> bool:
            if index == len(s):
                return star == target

            _sum = 0
            for i in range(index, len(s)):
                _sum = _sum * 10 + int(s[i])
                if _sum + star > target:
                    break
                if dfs(s, i+1, _sum + star, target):
                    return True
            return False

        res = 0
        for i in range(1, n+1):
            if dfs(str(i*i), 0, 0, i):
                print(i)
                res += i * i
        print(res)
        return res


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, pos: int, tot: int, target: int) -> bool:
            if pos == len(s):
                return tot == target
            sum = 0
            for i in range(pos, len(s)):
                sum = sum * 10 + int(s[i])
                if sum + tot > target:
                    break
                if dfs(s, i + 1, sum + tot, target):
                    return True
            return False
        res = 0
        for i in range(1, n + 1):
            if dfs(str(i * i), 0, 0, i):
                res += i * i
        return res



s = Solution()
s.punishmentNumber(n = 37)