#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 3 天 数组.py
# @Author: Lin
# @Date  : 2021/10/21 10:29
# 350. 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。
#  
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 进阶：
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
#
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        res = []
        for n in nums1:
            dic[n] += 1
        for n in nums2:
            if n in dic and dic[n] > 0:
                dic[n] -= 1
                res.append(n)
        return res


s = Solution()
res = s.intersect([1, 2, 2,1], [2,2,2])

# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
# 示例 1：
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
# 提示：
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mininum = prices[0]
        for i in prices:
            res = max(res, i - mininum)
            mininum = min(mininum, i)
        return res
