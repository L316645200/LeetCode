#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/12 10:43
# @Author  : Lin
# @File    : 2、矩形.py

"""84. 柱状图中最大的矩形[hard]
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：
输入： heights = [2,4]
输出： 4
提示：
1 <= heights.length <=105
0 <= heights[i] <= 104
"""
from typing import List


"""
思路：可以证明 矩形最大面积的高度一定是某个柱子的高度
则每个柱子去左右寻找第一个比自己低的柱子
可以求出以自己为高度的最大矩形面积
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        left, right = [-1] * n, [n] * n  # 坐标第一个比自己小的柱子下标，和右边第一个比自己小的柱子下标
        st = []
        for i in range(n-1, -1, -1):  # 单调栈
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            ans = max(ans, (right[i] - left[i] - 1) * heights[i])  # 求最大值
        return ans
# s = Solution()
# s.largestRectangleArea(heights = [2,1,5,6,2,3])
#
"""1793. 好子数组的最大分数 1946
给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
请你返回 好 子数组的最大可能 分数 。
示例 1：
输入：nums = [1,4,3,7,4,5], k = 3
输出：15
解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
示例 2：
输入：nums = [5,5,4,5,4,1,1,1], k = 0
输出：20
解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""
# 单调栈
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = [-1] * n, [n] * n
        st = []
        ans = 0
        for i in range(n-1, -1, -1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st.clear()
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            if left[i] < k < right[i]:
                ans = max(ans, (right[i] - left[i] - 1) * nums[i])
        return ans


# 双指针
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, cur = nums[k], nums[k]
        left, right = k - 1, k + 1
        while left >= 0 or right < n:
            if right == n or (left >= 0 and nums[left] >= nums[right]):  # 右指针超出 或者左指针大于右指针时
                cur = min(cur, nums[left])
                left -= 1
            else:
                cur = min(cur, nums[right])
                right += 1
            ans = max(ans, cur * (right - left - 1))
        return ans
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, cur = nums[k], nums[k]
        left, right = k - 1, k + 1
        for i in range(n-1):
            if right == n or (left >= 0 and nums[left] >= nums[right]):  # 右指针超出 或者左指针大于右指针时
                cur = min(cur, nums[left])
                left -= 1
            else:
                cur = min(cur, nums[right])
                right += 1
            ans = max(ans, cur * (right - left - 1))
        return ans
# s = Solution()
# s.maximumScore([6569,9667,3148,7698,1622,2194,793,9041,1670,1872], 5)

"""85. 最大矩形 
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：
输入：matrix = [["0"]]
输出：0
示例 3：
输入：matrix = [["1"]]
输出：1
提示：
rows == matrix.length
cols == matrix[0].length
1 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
"""

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [-1] * n, [n] * n
        st = []
        ans = 0
        for i in range(n-1, -1, -1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st.clear()
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            ans = max(ans, (right[i] - left[i] - 1) * nums[i])
        return ans


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i, cow in enumerate(matrix):
            for j, c in enumerate(cow):
                if c == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans, self.maximumScore(heights))
        return ans


# s = Solution()
# s.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
"""221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：
输入：matrix = [["0"]]
输出：0
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'"""

"""
# 单调栈
思路：求最大的矩阵边长，将边长改为求最大的正方形边长即可，即两矩阵两条边短的那条
"""
class Solution:
    def maxinum(self, nums: List[int]):  # 求边长
        n = len(nums)
        left, right = [-1] * n, [n] * n
        st = []
        ans = 0
        for i in range(n-1, -1, -1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st.clear()
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
            ans = max(ans, min((right[i]-left[i]-1), nums[i]))
        return ans

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * len(matrix[0])
        ans = 0
        for i, cow in enumerate(matrix):
            for j, c in enumerate(cow):
                if c == '0':
                    dp[j] = 0
                else:
                    dp[j] += 1
            ans = max(ans, self.maxinum(dp))
        return ans ** 2

# 动态规划

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])
        return ans ** 2

# s = Solution()
# s.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
"""42. 接雨水 做法不止一种
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
"""
思路：给每个柱子，找左边最大值和右边最大值，可以是自己，
然后减去自己的高度，这个数就是这个柱子能接的单位雨水（如果是负数取0）
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [i for i in range(n)], [i for i in range(n)]
        st = []
        ans = 0
        for i in range(n-1, -1, -1):
            while st and height[i] >= height[st[-1]]:
                st.pop()
            if st:
                right[i] = st[0]
            st.append(i)
        st.clear()
        for i in range(n):
            while st and height[i] >= height[st[-1]]:
                st.pop()
            if st:
                left[i] = st[0]
            st.append(i)
            ans += max(min(height[right[i]], height[left[i]]) - height[i], 0)
        return ans
# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        ans, n = 0, len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        while left <= right:
            if height[left] < height[right]:
                ans += min(left_max, right_max) - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                ans += min(left_max, right_max) - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return ans

s = Solution()
s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])




