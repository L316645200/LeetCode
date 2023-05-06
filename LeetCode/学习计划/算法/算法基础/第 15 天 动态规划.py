#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 15 天 动态规划.py
# @Author: Lin
# @Date  : 2022/8/19 17:04

# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
# 提示：
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。

# 递归 超时
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         ans = [0]
#         n = len(s)
#         def dfs(index):
#             if index == n:
#                 ans[0] += 1
#                 return
#             for i in range(1, 3):
#                 if index < n and s[index] != '0' and 1 <= int(s[index: index+i]) <= 26:
#                     dfs(index+i)
#         dfs(0)
#         return ans[0]


# 动态规划
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [1] + [0] * (n-1)  # 可以用三个变量优化
        if s[0] == "0":
            return 0

        for i in range(1, n):
            if "10" <= s[i-1:i+1] <= "26":
                dp[i+1] += dp[i-1]
            if s[i] != "0":
                dp[i+1] += dp[i]
            # 可以提前判断没有有效映射，这两行可以注释掉
            if dp[i+1] == 0:
                return 0
        return dp[n]


s = Solution()
r = s.numDecodings(s = "08")
print(r)

# 139. 单词拆分
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 提示：
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        arr = [False] * (n+1)
        arr[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if arr[i] is True and s[i:j] in wordDict:
                    arr[j] = True
        return arr[n]




s = Solution()
s.wordBreak( s = "applepenapple", wordDict = ["apple", "pen"])