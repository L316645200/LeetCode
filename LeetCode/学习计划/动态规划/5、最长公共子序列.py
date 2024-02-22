#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：5、最长公共子序列.py
# @Author  ：Lin
# @Date    ：2024/2/17 16:01


"""1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
提示：
1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。"""

# 动态规划
from functools import cache
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1), len(text2)
#
#         @cache
#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return 0
#             if text1[i] == text2[j]:
#                 return dfs(i-1, j-1) + 1
#             return max(dfs(i-1, j), dfs(i, j-1))
#         return dfs(n-1, m-1)
#
# 空间优化
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            pre = dp[0]
            for j in range(1, m + 1):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
                pre = tmp

        return dp[m]


s = Solution()
s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )


"""72. 编辑距离
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for i in range(n+1)]
        dp[0] = list(range(m+1))

        for i in range(1, n+1):
            dp[i][0] = i

            for j in range(1, m+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]


s = Solution()
# s.minDistance(word1 = "horse", word2 = "ros")


s.minDistance(word1 = "", word2 = "a")


"""1035. 不相交的线
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

 

示例 1：


输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
示例 2：

输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3
示例 3：

输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
 

提示：

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
 """


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

# 空间优化
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)
        dp = [0] * (m+1)
        for i in range(n):
            pre = dp[0]
            for j in range(m):
                tmp = dp[j+1]
                if nums1[i] == nums2[j]:
                    dp[j+1] = pre + 1
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                pre = tmp
        return dp[-1]


s = Solution()
s.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1])


























