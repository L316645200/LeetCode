#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210925_583. 两个字符串的删除操作.py
# @Author: Lin
# @Date  : 2021/9/25 16:34
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
#
# 示例：
#
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
#  
#
# 提示：
#
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。

# 006动态规划 最长公共子序列
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1)+1, len(word2)+1
        dp = [[0]*n2 for _ in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n1 + n2 - dp[-1][-1] * 2 - 2
s = Solution()
s.minDistance('sea', 'eat')
# 006动态规划 直接求删除
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1)+1, len(word2)+1
        dp = [[i + j for i in range(n2)] for j in range(n1)] # 只要构造第0行和第0列的数据即可
        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
s = Solution()
s.minDistance('sea', 'eat')