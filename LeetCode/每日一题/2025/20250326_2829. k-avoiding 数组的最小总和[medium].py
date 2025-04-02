#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/26 13:27
# @Author  : Lin
# @File    : 20250326_2829. k-avoiding 数组的最小总和[medium].py
"""给你两个整数 n 和 k 。

对于一个由 不同 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 k-avoiding 数组。

返回长度为 n 的 k-avoiding 数组的可能的最小总和。



示例 1：

输入：n = 5, k = 4
输出：18
解释：设若 k-avoiding 数组为 [1,2,4,5,6] ，其元素总和为 18 。
可以证明不存在总和小于 18 的 k-avoiding 数组。
示例 2：

输入：n = 2, k = 6
输出：3
解释：可以构造数组 [1,2] ，其元素总和为 3 。
可以证明不存在总和小于 3 的 k-avoiding 数组。


提示：

1 <= n, k <= 50"""

"""分两部分求加
第一部分，小于k的时候
1和k-1只能选一个，选小的1
2和k-2只能选一个，选小的2...
如果k是偶数，k/2也选
求和: (1+k/2)*k/2/2
第二部分，
设m=k/2,则剩余n-m个数
求和: (k+k+n-m-1)*(n-m)/2
"""

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        m = min(k//2, n)
        return (1+m)*m//2 + (k+k+n-m-1)*(n-m)//2


