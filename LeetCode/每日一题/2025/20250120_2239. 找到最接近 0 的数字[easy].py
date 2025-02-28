#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250120_2239. 找到最接近 0 的数字[easy].py
# @Author  ：Lin
# @Date    ：2025/1/20 9:44
"""2239. 找到最接近 0 的数字

给你一个长度为 n的整数数组nums，请你返回 nums中最 接近0的数字。
如果有多个答案，请你返回它们中的 最大值。

示例 1：
输入：nums = [-4,-2,1,4,8]
输出：1
解释：
-4 到 0 的距离为 |-4| = 4 。
-2 到 0 的距离为 |-2| = 2 。
1 到 0 的距离为 |1| = 1 。
4 到 0 的距离为 |4| = 4 。
8 到 0 的距离为 |8| = 8 。
所以，数组中距离 0 最近的数字为 1 。

示例 2：
输入：nums = [2,-1,1]
输出：1
解释：1 和 -1 都是距离 0 最近的数字，所以返回较大值 1 。

提示：
	1 <= n <= 1000
	-10^5 <= nums[i] <= 10^5


https://leetcode.cn/problems/find-closest-number-to-zero/description/?envType=daily-question&envId=2025-01-20"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = -10**5
        for num in nums:
            if abs(num) < abs(res) or (abs(num) == abs(res) and num > res):
                res = num
        return res