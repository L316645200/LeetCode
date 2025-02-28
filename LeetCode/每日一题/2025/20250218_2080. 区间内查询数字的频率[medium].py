#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250218_2080. 区间内查询数字的频率[medium].py
# @Author  ：Lin
# @Date    ：2025/2/18 15:02

"""2080. 区间内查询数字的频率

请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率。
子数组中一个值的 频率指的是这个子数组中这个值的出现次数。
请你实现RangeFreqQuery类：
	RangeFreqQuery(int[] arr)用下标从 0开始的整数数组arr构造一个类的实例。
	int query(int left, int right, int value)返回子数组arr[left...right]中value的频率。
一个 子数组 指的是数组中一段连续的元素。arr[left...right]指的是 nums中包含下标 left和 right在内的中间一段连续元素。

示例 1：
输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：
[null, 1, 2]
解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。

提示：
	1 <= arr.length <= 10^5
	1 <= arr[i], value <= 10^4
	0 <= left <= right < arr.length
	调用query不超过10^5次。


https://leetcode.cn/problems/range-frequency-queries/?envType=daily-question&envId=2025-02-18"""
import bisect
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = defaultdict(list)
        for i, v in enumerate(arr):
            self.mp[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        arr = self.mp[value]
        start = bisect.bisect_left(arr, left)
        end = bisect.bisect_right(arr, right)
        return end - start

