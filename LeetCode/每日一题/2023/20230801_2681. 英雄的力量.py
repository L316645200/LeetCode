#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230801_2681. 英雄的力量.py
# @Author: Lin
# @Date  : 2023/8/1 15:16

#
# 给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。
# 如果我们选出一部分英雄，这组英雄的 力量 定义为：
#
# i0 ，i1 ，... ik 表示这组英雄在数组中的下标。
# 那么这组英雄的力量为 max(nums[i0],nums[i1] ... nums[ik])2 * min(nums[i0],nums[i1] ... nums[ik]) 。
# 请你返回所有可能的 非空 英雄组的 力量 之和。
# 由于答案可能非常大，请你将结果对 109 + 7 取余。
#
# 示例 1：
# 输入：nums = [2,1,4]
# 输出：141
# 解释：
# 第 1 组：[2] 的力量为 22 * 2 = 8 。
# 第 2 组：[1] 的力量为 12 * 1 = 1 。
# 第 3 组：[4] 的力量为 42 * 4 = 64 。
# 第 4 组：[2,1] 的力量为 22 * 1 = 4 。
# 第 5 组：[2,4] 的力量为 42 * 2 = 32 。
# 第 6 组：[1,4] 的力量为 42 * 1 = 16 。
# 第​ ​​​​​​7 组：[2,1,4] 的力量为 42​​​​​​​ * 1 = 16 。
# 所有英雄组的力量之和为 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141 。
# 示例 2：
# 输入：nums = [1,1,1]
# 输出：7
# 解释：总共有 7 个英雄组，每一组的力量都是 1 。所以所有英雄组的力量之和为 7 。
# 输入：nums = [1,1,1]
# 输出：7
# 解释：总共有 7 个英雄组，每一组的力量都是 1 。所以所有英雄组的力量之和为 7 。
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dp = [0] * n
        pre_sum = [0] * (n + 1)
        res, mod = 0, 10 ** 9 + 7
        for i in range(n):
            dp[i] = (nums[i] + pre_sum[i]) % mod
            pre_sum[i + 1] = (pre_sum[i] + dp[i]) % mod

            res = (res + nums[i] ** 2 * dp[i]) % mod
            print(dp, pre_sum)
        return res


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        dp, pre_sum = 0, 0
        res, mod = 0, 10 ** 9 + 7
        for i in range(len(nums)):
            dp = (nums[i] + pre_sum) % mod
            pre_sum = (pre_sum + dp) % mod
            res = (res + nums[i] * nums[i] * dp) % mod
        return res


s = Solution()
s.sumOfPower(nums = [1,2,4,8,16])
# print(2**3+2**2*2+2*4+8+16)
# s.sumOfPower(nums = [1,1,1,1])