#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210903_面试题 17.14. 最小K个数.py
# @Author: Lin
# @Date  : 2021/9/3 9:17


# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
# 示例：
#
# 输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
# 提示：
#
# 0 <= len(arr) <= 100000
# 0 <= k <= min(100000, len(arr))
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


arr = [3,4,2,1]

print(arr)