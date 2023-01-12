#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220926_面试题 17.19. 消失的两个数字.py
# @Author: Lin
# @Date  : 2022/9/26 9:23

# 给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？
# 以任意顺序返回这两个数字均可。
# 示例 1:
# 输入: [1]
# 输出: [2,3]
# 示例 2:
# 输入: [2,3]
# 输出: [1,4]
# 提示：
# nums.length <= 30000
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        su = sum([i for i in range(1, n + 1)]) - sum(nums)
        square = sum([i ** 2 for i in range(1, n + 1)]) - sum([num ** 2 for num in nums])


        su ** 2 - 2 * x * (su - x) = square

        x = su / 2 - square / (su * 2)

        print(x)







s = Solution()
s.missingTwo([2,3])