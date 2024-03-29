#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231110_2300. 咒语和药水的成功对数.py
# @Author  ：Lin
# @Date    ：2023/11/10 14:40


"""给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。

同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。

请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。



示例 1：

输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
输出：[4,0,3]
解释：
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
示例 2：

输入：spells = [3,1,2], potions = [8,5,8], success = 16
输出：[2,0,2]
解释：
- 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
- 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
- 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
所以返回 [2,0,2] 。


提示：

n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010"""
from typing import List

# 二分
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        for i, spell in enumerate(spells):
            t = success / spell
            left, right = 0, n - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if potions[mid] >= t:
                    right = mid - 1
                else:
                    left = mid + 1
            spells[i] = n - left
        return spells


# 双指针
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spells_sort = sorted(spells)

        potions.sort()
        d = {}
        m, n = len(spells), len(potions)
        j = n - 1
        for i in range(m):
            t = success / spells_sort[i]
            while j >= 0 and potions[j] >= t:
                j -= 1
            d[spells_sort[i]] = n - j - 1
        return [d[spells[i]] for i in range(m)]


# 双指针代码改进
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m, n = len(spells), len(potions)
        res = [0] * m
        idx = [i for i in range(m)]
        idx.sort(key=lambda x: spells[x])
        potions.sort()

        j = n - 1
        for i in range(m):
            t = success / spells[idx[i]]
            while j >= 0 and potions[j] >= t:
                j -= 1
            res[idx[i]] = n - j - 1
        return res


s = Solution()
s.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7)