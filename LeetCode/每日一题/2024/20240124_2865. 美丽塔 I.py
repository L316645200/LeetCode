#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240124_2865. 美丽塔 I.py
# @Author  ：Lin
# @Date    ：2024/1/24 17:09


"""给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。

你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。

如果以下条件满足，我们称这些塔是 美丽 的：

1 <= heights[i] <= maxHeights[i]
heights 是一个 山脉 数组。
如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：

对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。



示例 1：

输入：maxHeights = [5,3,4,1,1]
输出：13
解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山脉数组，峰值在 i = 0 处。
13 是所有美丽塔方案中的最大高度和。
示例 2：

输入：maxHeights = [6,5,3,9,2,7]
输出：22
解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山脉数组，峰值在 i = 3 处。
22 是所有美丽塔方案中的最大高度和。
示例 3：

输入：maxHeights = [3,2,5,5,2,3]
输出：18
解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山脉数组，最大值在 i = 2 处。
注意，在这个方案中，i = 3 也是一个峰值。
18 是所有美丽塔方案中的最大高度和。


提示：

1 <= n == maxHeights <= 103
1 <= maxHeights[i] <= 109"""
from typing import List


# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)
#         ans = 0
#         for i in range(n):
#             left, right = i - 1, i + 1
#             s = maxHeights[i]
#             left_height, right_height = s, s
#             while left >= 0:
#                 if maxHeights[left] > left_height:
#                     s += left_height
#                 else:
#                     s += maxHeights[left]
#                     left_height = maxHeights[left]
#                 left -= 1
#             while right < n:
#                 if maxHeights[right] > right_height:
#                     s += right_height
#                 else:
#                     s += maxHeights[right]
#                     right_height = maxHeights[right]
#                 right += 1
#             ans = max(ans, s)
#         return ans
# 方法一：枚举
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            left, right = i - 1, i + 1
            s = maxHeights[i]
            left_height, right_height = s, s
            while left >= 0:
                left_height = min(maxHeights[left], left_height)
                s += left_height
                left -= 1
            while right < n:
                right_height = min(maxHeights[right], right_height)
                s += right_height
                right += 1
            ans = max(ans, s)
        return ans

# 方法二：单调栈
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        res = 0
        prefix, suffix = [0] * n, [0] * n
        stack1, stack2 = [], []
        """对于左侧的非递减：将 maxHeights依次入栈，对于第 i 个元素来说，不断从栈顶弹出元素，
        直到栈顶元素小于等于 maxHeights[i]。假设此时栈顶元素为 maxHeights[j]，
        则区间 [j+1,i−1]中的元素最多只能取到 maxHeights[i]，
        则 prefix[i]=prefix[j]+(i−j)×maxHeights[i]；"""
        for i in range(n):
            while stack1 and maxHeights[stack1[-1]] >= maxHeights[i]:
                stack1.pop()
            if stack1:
                prefix[i] = prefix[stack1[-1]] + maxHeights[i] * (i - stack1[-1])
            else:
                prefix[i] = maxHeights[i] * (i + 1)

            stack1.append(i)
        """对于右侧的非递减：将 maxHeights依次入栈，对于第 i个元素来说，不断从栈顶弹出元素，
        直到栈顶元素小于等于 maxHeights[i]。假设此时栈顶元素为 maxHeights[j]，
        则区间 [i+1,j−1]中的元素最多只能取到 maxHeights[i]，
        则 suffix[i]=suffix[j]+(j−i)×maxHeights[i]；"""
        for i in range(n-1, -1, -1):
            while stack2 and maxHeights[stack2[-1]] >= maxHeights[i]:
                stack2.pop()
            if stack2:
                suffix[i] = suffix[stack2[-1]] + maxHeights[i] * (stack2[-1] - i)
            else:
                suffix[i] = maxHeights[i] * (n - i)
            stack2.append(i)

            res = max(res, prefix[i] + suffix[i] - maxHeights[i])
        return res


s = Solution()
# s.maximumSumOfHeights(maxHeights = [3,2,5,5,2,3])
s.maximumSumOfHeights(maxHeights = [2,4,1,3,5])

































