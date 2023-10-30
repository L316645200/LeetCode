#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231019_ 1726. 同积元组.py
# @Author: Lin
# @Date  : 2023/10/19 11:10

"""给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。



示例 1：

输入：nums = [2,3,4,6]
输出：8
解释：存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
示例 2：

输入：nums = [1,2,4,5,10]
输出：16
解释：存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)


提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums 中的所有元素 互不相同"""
from typing import List
from collections import defaultdict, Counter

"""# 当 a*b=c*d时，由于由于数组中不存在相同的数，所以a<>b<>c<>d,
# 此时回满足 a * b = c * d 的元组 (a, b, c, d) 的数量为4*1*2*1=8,
即任意选 2个两不同的数对一定可以满构成8个不同的同积元组
"""
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                cnt[nums[i]*nums[j]] += 1
        return sum([8 * ((v-1) * v) // 2 for c, v in cnt.items()])


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([8 * ((v - 1) * v) // 2 for c, v in Counter([nums[i]*nums[j] for i in range(n) for j in range(i+1, n)]).items()])


s = Solution()
r = s.tupleSameProduct(nums = [2,3,4,6,8,12])
print(r)