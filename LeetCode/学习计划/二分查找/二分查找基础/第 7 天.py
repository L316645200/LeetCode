#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 7 天.py
# @Author: Lin
# @Date  : 2023/6/14 15:04

# 1482. 制作 m 束花所需的最少天数
# 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
# 现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
# 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
# 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。
# 示例 1：
# 输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
# 输出：3
# 解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
# 现在需要制作 3 束花，每束只需要 1 朵。
# 1 天后：[x, _, _, _, _]   // 只能制作 1 束花
# 2 天后：[x, _, _, _, x]   // 只能制作 2 束花
# 3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
# 示例 2：
# 输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
# 输出：-1
# 解释：要制作 3 束花，每束需要 2 朵花，也就是一共需要 6 朵花。而花园中只有 5 朵花，无法满足制作要求，返回 -1 。
# 示例 3：
# 输入：bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# 输出：12
# 解释：要制作 2 束花，每束需要 3 朵。
# 花园在 7 天后和 12 天后的情况如下：
# 7 天后：[x, x, x, x, _, x, x]
# 可以用前 3 朵盛开的花制作第一束花。但不能使用后 3 朵盛开的花，因为它们不相邻。
# 12 天后：[x, x, x, x, x, x, x]
# 显然，我们可以用不同的方式制作两束花。
# 示例 4：
# 输入：bloomDay = [1000000000,1000000000], m = 1, k = 1
# 输出：1000000000
# 解释：需要等 1000000000 天才能采到花来制作花束
# 示例 5：
# 输入：bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
# 输出：9
# 提示：
# bloomDay.length == n
# 1 <= n <= 10^5
# 1 <= bloomDay[i] <= 10^9
# 1 <= m <= 10^6
# 1 <= k <= n
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        left, right = 1, max(bloomDay)
        ans = 0
        while left <= right:
            day = left + (right - left) // 2
            t = 0
            f = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    t += 1
                else:
                    t = 0
                if t >= k:
                    f += 1
                    t -= k
            if f >= m:
                ans = day
                right = day - 1
            else:
                left = day + 1
        return ans


s = Solution()
s.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)


# 1818. 绝对差值和
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
# |x| 定义为：
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x
# 示例 1：
# 输入：nums1 = [1,7,5], nums2 = [2,3,5]
# 输出：3
# 解释：有两种可能的最优方案：
# - 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
# - 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
# 两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
# 示例 2：
# 输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
# 输出：0
# 解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
# 示例 3：
# 输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
# 输出：20
# 解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
# 绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
# 提示：
# n == nums1.length
# n == nums2.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 105


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums_sort = sorted(nums1)
        n = len(nums1)
        total = 0
        mi = 0
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums_sort[mid] <= nums2[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            b = min(abs(nums_sort[left - 1] - nums2[i]) if 0 <= left - 1 < n else float('inf'),
                    abs(nums_sort[left] - nums2[i]) if 0 <= left < n else float('inf'))
            if b < diff:
                mi = min(mi, b - diff)
        return (total + mi) % (10 ** 9 + 7)

s = Solution()
s.minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4])


































