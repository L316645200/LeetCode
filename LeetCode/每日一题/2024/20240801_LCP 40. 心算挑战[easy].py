#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240801_LCP 40. 心算挑战[easy].py
# @Author  ：Lin
# @Date    ：2024/8/1 10:08


"""「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

示例 1：

输入：cards = [1,2,8,9], cnt = 3

输出：18

解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

示例 2：

输入：cards = [3,3,1], cnt = 1

输出：0

解释：不存在获取有效得分的卡牌方案。

提示：

1 <= cnt <= cards.length <= 10^5
1 <= cards[i] <= 1000"""
from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])
        if s % 2 == 0:
            return s

        def replace_sum(x: int) -> int:
            for y in cards[cnt:]:
                if y % 2 != x % 2:
                    return s - x + y
            return 0

        x = cards[cnt-1]
        res = replace_sum(x)

        for i in range(cnt-1, -1, -1):
            if cards[i] % 2 != x % 2:
                res = max(res, replace_sum(cards[i]))
                break
        return res



s = Solution()
# s.maxmiumScore(cards = [7,4,1], cnt = 1)
s.maxmiumScore(cards =
[9,5,9,1,6,10,3,4,5,1], cnt = 2)
