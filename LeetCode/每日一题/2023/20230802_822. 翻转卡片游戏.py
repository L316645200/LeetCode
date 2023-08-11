#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230802_822. 翻转卡片游戏.py
# @Author: Lin
# @Date  : 2023/8/2 18:19
#
# 在桌子上有
# N
# 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。
# 我们可以先翻转任意张卡片，然后选择其中一张卡片。
# 如果选中的那张卡片背面的数字
# X
# 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。
# 哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出
# 0。
# 其中, fronts[i]
# 和
# backs[i]
# 分别代表第
# i
# 张卡片的正面和背面的数字。
# 如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。
# 示例：
# 输入：fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]
# 输出：2
# 解释：假设我们翻转第二张卡片，那么在正面的数变成了[1, 3, 4, 4, 7] ， 背面的数变成了[1, 2, 4, 1, 3]。
# 接着我们选择第二张卡片，因为现在该卡片的背面的数是
# 2，2
# 与任意卡片上正面的数都不同，所以
# 2
# 就是我们想要的数字。
# 提示：
# 1 <= fronts.length == backs.length <= 1000
# 1 <= fronts[i] <= 2000
# 1 <= backs[i] <= 2000
from typing import List
from collections import defaultdict

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res = min(self.core(fronts, backs), self.core(backs, fronts))
        return res if res < 3000 else 0

    @staticmethod
    def core(fronts, backs):
        d = defaultdict(list)
        for i, f in enumerate(fronts):
            d[f].append(i)
        res = 3000
        for i, v in enumerate(backs):
            arr = d[v]
            mark = 0
            if arr:
                for j in arr:
                    if backs[j] != v:
                        continue
                    mark = 1
                    break
            res = min(res, v) if mark == 0 else res
        return res


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        same = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        res = 3000
        for a in fronts:
            if a < res and a not in same:
                res = a
        for a in backs:
            if a < res and a not in same:
                res = a
        return res if res < 3000 else 0


s = Solution()
s.flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3])