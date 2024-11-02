#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241102_3226. 使两个整数相等的位更改次数[easy].py
# @Author  ：Lin
# @Date    ：2024/11/2 10:29


"""给你两个正整数 n 和 k。

你可以选择 n 的 二进制表示 中任意一个值为 1 的位，并将其改为 0。

返回使得 n 等于 k 所需要的更改次数。如果无法实现，返回 -1。



示例 1：

输入： n = 13, k = 4

输出： 2

解释：
最初，n 和 k 的二进制表示分别为 n = (1101)2 和 k = (0100)2，

我们可以改变 n 的第一位和第四位。结果整数为 n = (0100)2 = k。

示例 2：

输入： n = 21, k = 21

输出： 0

解释：
n 和 k 已经相等，因此不需要更改。

示例 3：

输入： n = 14, k = 13

输出： -1

解释：
无法使 n 等于 k。



提示：

1 <= n, k <= 106"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return (n ^ k).bit_count() if n & k == k else -1


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        res = 0
        while n > 0 or k > 0:
            if n & 1 == 0 and k & 1 == 1:
                return -1
            if n & 1 == 1 and k & 1 == 0:
                res += 1
            n >>= 1
            k >>= 1
        return res


s = Solution()
s.minChanges(n = 13, k = 4)
