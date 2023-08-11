#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230619_1262. 可被三整除的最大和.py
# @Author: Lin
# @Date  : 2023/6/21 10:18


# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
# 示例 1：
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 示例 2：
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 示例 3：
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
# 提示：
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        a, b, c = [], [], []
        nums_sum = 0
        # 分为余0(a) 余1(b) 余2(c)
        for num in nums:
            if num % 3 == 0:
                a.append(num)
            elif num % 3 == 1:
                b.append(num)
            else:
                c.append(num)
            nums_sum += num
        ans = 0
        lb, lc = len(b), len(c)
        # b被剩余的数不大于2，c同理
        for i in range(3):
            if lb - i >= 0:
                for j in range(3):
                    if lc - j >= 0:
                        if (lb - i - (lc - j)) % 3 == 0:
                            ans = max(ans, nums_sum - sum(b[:i]) - sum(c[:j]))
        return ans


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        a, b, c = [], [], []
        nums_sum = 0
        # 分为余0(a) 余1(b) 余2(c)
        for num in nums:
            if num % 3 == 0:
                a.append(num)
            elif num % 3 == 1:
                b.append(num)
            else:
                c.append(num)
            nums_sum += num
        lb, lc = len(b), len(c)
        remove = float('inf')
        if nums_sum % 3 == 0:
            remove = 0
        elif nums_sum % 3 == 1:
            if lb >= 1:
                remove = min(remove, b[0])
            if lc >= 2:
                remove = min(remove, c[0] + c[1])
        else:
            if lb >= 2:
                remove = min(remove, b[0] + b[1])
            if lc >= 1:
                remove = min(remove, c[0])
        return nums_sum - remove

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]

s = Solution()
# s.maxSumDivThree(nums = [1,2,3,4,4])

# s.maxSumDivThree(nums = [3,6,5,1,8])
s.maxSumDivThree([5,2,2,2])



