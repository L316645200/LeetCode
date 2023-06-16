#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230510_1015. 可被 K 整除的最小整数.py
# @Author: Lin
# @Date  : 2023/5/11 11:38

# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
# 返回 n 的长度。如果不存在这样的 n ，就返回-1。
# 注意： n 不符合 64 位带符号整数。
# 示例 1：
# 输入：k = 1
# 输出：1
# 解释：最小的答案是 n = 1，其长度为 1。
# 示例 2：
#
# 输入：k = 2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 n 。
# 示例 3：
#
# 输入：k = 3
# 输出：3
# 解释：最小的答案是 n = 111，其长度为 3。
# 提示：
#
# 1 <= k <= 105

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 in [0, 2, 4, 5, 6, 8]:
            return -1

        ans, resid = 1, 1  # ans 表示长度，resid 表示余数
        while resid % k != 0:  # 当余数不为 0 时
            resid = (resid % k) * (10 % k) + 1  # 模拟除法运算，计算下一次的余数
            ans += 1  # 长度加 1

        return ans  # 返回最小整数的长度


s = Solution()
r = s.smallestRepunitDivByK(23)
print(r)