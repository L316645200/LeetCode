#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 17 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/22 11:08

# 1143. 最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
# 提示：
#
# 1 <= text1.length, text2.length <= 1000
# text1 和 text2 仅由小写英文字符组成。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1)+1, len(text2)+1
        dp = [[0] * l2 for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

s = Solution()
s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )


# 583. 两个字符串的删除操作
# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
# 每步 可以删除任意一个字符串中的一个字符。
# 示例 1：
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
# 示例  2:
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
# 提示：
# 1 <= word1.length, word2.length <= 500
# word1 和 word2 只包含小写英文字母

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return l1 + l2 - dp[-1][-1] * 2 - 2


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[i + j for i in range(l2)] for j in range(l1)]
        print(dp)
        print()

        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
s = Solution()
s.minDistance(word1 = "leetcode", word2 = "etco")












