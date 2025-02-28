#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250125_2412. 完成所有交易的初始最少钱数[hard].py
# @Author  ：Lin
# @Date    ：2025/1/25 9:22
"""2412. 完成所有交易的初始最少钱数
给你一个下标从 0开始的二维整数数组transactions，其中transactions[i] = [costi, cashbacki]。
数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱money，为了完成交易i，money >= costi这个条件必须为真。执行交易后，你的钱数money 变成money - costi + cashbacki。
请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数money是多少。
示例 1：
输入：transactions = [[2,1],[5,0],[4,2]]
输出：10
解释：
刚开始 money = 10 ，交易可以以任意顺序进行。
可以证明如果 money < 10 ，那么某些交易无法进行。
示例 2：
输入：transactions = [[3,0],[0,3]]
输出：3
解释：
- 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
- 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
提示：
	1 <= transactions.length <= 10^5
	transactions[i].length == 2
	0 <= costi, cashbacki <= 10^9
https://leetcode.cn/problems/minimum-money-required-before-transactions/description/?envType=daily-question&envId=2025-01-25"""
from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = res = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            res = max(res, min(cost, cashback))
        return total_lose + res


s = Solution()
s.minimumMoney(transactions = [[3,9],[0,4],[7,10],[3,5],[0,9],[9,3],[7,4],[0,0],[3,3],[8,0]])
# s.minimumMoney(transactions = [[2,1],[5,0],[4,2]])
