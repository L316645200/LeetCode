#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250220_2595. 奇偶位数[easy].py
# @Author  ：Lin
# @Date    ：2025/2/20 9:11

"""2595. 奇偶位数

给你一个 正 整数 n 。
用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。
用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。
返回整数数组 answer ，其中 answer = [even, odd] 。

示例 1：
输入：n = 17
输出：[2,0]
解释：17 的二进制形式是 10001 。
下标 0 和 下标 4 对应的值为 1 。
共有 2 个偶数下标，0 个奇数下标。

示例 2：
输入：n = 2
输出：[0,1]
解释：2 的二进制形式是 10 。
下标 1 对应的值为 1 。
共有 0 个偶数下标，1 个奇数下标。

提示：
	1 <= n <= 1000


https://leetcode.cn/problems/number-of-even-and-odd-bits/description/?envType=daily-question&envId=2025-02-20"""
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        i = 0
        while n:
            if i % 2 == 0:
                even += n & 1
            else:
                odd += n & 1
            i += 1
            n //= 2
        return [even, odd]

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1  # 切换奇偶
        return ans


s = Solution()
s.evenOddBit(50)
