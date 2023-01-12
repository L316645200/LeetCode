#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220813_768. 最多能完成排序的块 II.py
# @Author: Lin
# @Date  : 2022/8/13 11:20

# 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。
# arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
# 我们最多能将数组分成多少块？
# 示例 1:
# 输入: arr = [5,4,3,2,1]
# 输出: 1
# 解释:
# 将数组分成2块或者更多块，都无法得到所需的结果。
# 例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
# 示例 2:
# 输入: arr = [2,1,3,4,4]
# 输出: 4
# 解释:
# 我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
# 然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
# 注意:
# arr的长度在[1, 2000]之间。
# arr[i]的大小在[0, 10**8]之间。
from collections import defaultdict
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        n = len(arr)
        cnt = defaultdict(int)
        ans = 0
        for i in range(n):
            cnt[arr[i]] += 1
            cnt[sorted_arr[i]] -= 1
            if cnt[arr[i]] == 0:
                del cnt[arr[i]]
            if cnt[sorted_arr[i]] == 0:
                del cnt[sorted_arr[i]]
            if not cnt:
                ans += 1
        return ans


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and a < stack[-1]:
                    stack.pop()
                stack.append(mx)
        return len(stack)
s = Solution()
s.maxChunksToSorted(arr = [2,1,3,4,4])