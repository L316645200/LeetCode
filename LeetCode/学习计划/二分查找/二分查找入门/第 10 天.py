#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 10 天.py
# @Author: Lin
# @Date  : 2023/4/17 17:17

# 350. 两个数组的交集 II
# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
# 提示：
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 进阶：
# 如果给定的数组已经排好序呢？你将如何优化你的算法？ 双指针 + 二分(数组长度小的遍历，大的二分)
# 如果 nums1 的大小比 nums2 小，哪种方法更优？  二分
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 分片读取，哈希存储
import math
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        if len(cnt1) > len(cnt2):
            cnt1, cnt2 = cnt2, cnt1

        for k, v in cnt1.items():
            if cnt2[k]:
                ans.extend([k] * min(v, cnt2[k]))
        return ans

s = Solution()
s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])


# 633. 平方数之和

# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
# 示例 1：
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：
# 输入：c = 3
# 输出：false
# 提示：
# 0 <= c <= 231 - 1
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.floor(math.sqrt(c))
        while a <= b:
            s = a ** 2 + b ** 2
            if s == c:
                return True
            elif s > c:
                b -= 1
            else:
                a += 1
        return False


s = Solution()
r = s.judgeSquareSum(c = 1)
print(r)
print(2**31-1)