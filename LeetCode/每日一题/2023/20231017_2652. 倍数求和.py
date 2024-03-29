#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231017_2652. 倍数求和.py
# @Author: Lin
# @Date  : 2023/10/17 9:58

"""给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。

返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。



示例 1：

输入：n = 7
输出：21
解释：在 [1, 7] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7 。数字之和为 21 。
示例 2：

输入：n = 10
输出：40
解释：在 [1, 10] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9、10 。数字之和为 40 。
示例 3：

输入：n = 9
输出：30
解释：在 [1, 9] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9 。数字之和为 30 。


提示：

1 <= n <= 103"""


# 枚举
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)


# 容斥原理

"""考虑在区间 [1,n][1, n][1,n] 内能被数 mmm 整除的整数，从小到大排序后成为一个等差数列，和为：

f(n,m) = (m + n // m * m) * (n // m) // 2
 
根据 容斥原理，在区间 [1,n][1, n][1,n] 内，能被 3 、5 和 7 整除的整数之和为：

f(3) + f(5) + f(7) - f(3*5) - f(3*7) - f(5*7) + f(3*5*7)"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            return (m + n // m * m) * (n // m) // 2
        return f(3) + f(5) + f(7) - f(3*5) - f(3*7) - f(5*7) + f(3*5*7)



s = Solution()
s.sumOfMultiples(10)