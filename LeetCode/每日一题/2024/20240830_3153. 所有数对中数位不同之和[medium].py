#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240830_3153. 所有数对中数位不同之和[medium].py
# @Author  ：Lin
# @Date    ：2024/8/30 11:10


"""你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。

两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。

请你返回 nums 中 所有 整数对里，数位不同之和。



示例 1：

输入：nums = [13,23,12]

输出：4

解释：
计算过程如下：
- 13 和 23 的数位不同为 1 。
- 13 和 12 的数位不同为 1 。
- 23 和 12 的数位不同为 2 。
所以所有整数数对的数位不同之和为 1 + 1 + 2 = 4 。

示例 2：

输入：nums = [10,10,10,10]

输出：0

解释：
数组中所有整数都相同，所以所有整数数对的数位不同之和为 0 。



提示：

2 <= nums.length <= 105
1 <= nums[i] < 109
nums 中的整数都有相同的数位长度。"""
from typing import List


# class Solution:
#     def sumDigitDifferences(self, nums: List[int]) -> int:
#         res = 0
#         pos = [defaultdict(int) for _ in range(10)]
#         for num in nums:
#             i = 0
#             while num:
#                 remainder = num % 10
#                 res += pos[i][-1] - pos[i][remainder]
#                 pos[i][remainder] += 1
#                 pos[i][-1] += 1
#                 i += 1
#                 num //= 10
#         return res

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        res = 0
        pos = [[0] * 11 for _ in range(9)]
        for num in nums:
            i = 0
            while num:
                remainder = num % 10
                res += pos[i][10] - pos[i][remainder]
                pos[i][remainder] += 1
                pos[i][10] += 1
                i += 1
                num //= 10
        return res

s = Solution()
s.sumDigitDifferences(nums = [13,23,12])