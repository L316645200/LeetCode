#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241107_3255. 长度为 K 的子数组的能量值 II[medium].py
# @Author  ：Lin
# @Date    ：2024/11/7 9:09

"""给你一个长度为 n 的整数数组 nums 和一个正整数 k 。

一个数组的 能量值 定义为：

如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
否则为 -1 。
你需要求出 nums 中所有长度为 k 的
子数组
 的能量值。

请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。
示例 1：

输入：nums = [1,2,3,4,3,2,5], k = 3

输出：[3,4,-1,-1,-1]

解释：

nums 中总共有 5 个长度为 3 的子数组：

[1, 2, 3] 中最大元素为 3 。
[2, 3, 4] 中最大元素为 4 。
[3, 4, 3] 中元素 不是 连续的。
[4, 3, 2] 中元素 不是 上升的。
[3, 2, 5] 中元素 不是 连续的。
示例 2：

输入：nums = [2,2,2,2,2], k = 4

输出：[-1,-1]

示例 3：

输入：nums = [3,2,3,2,3,2], k = 2

输出：[-1,3,-1,3,-1]
提示：

1 <= n == nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= n"""
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * (n - k + 1)
        cnt = 0
        for i in range(n):
            cnt = 1 if i == 0 or nums[i] - nums[i-1] != 1 else cnt + 1
            if cnt >= k:
                res[i-k+1] = nums[i]
        return res

s = Solution()
s.resultsArray(nums = [3,2,3,2,3,2], k = 2)
