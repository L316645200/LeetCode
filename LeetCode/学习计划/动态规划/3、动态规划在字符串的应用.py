#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 3、动态规划在字符串的应用.py
# @Author: Lin
# @Date  : 2023/8/12 16:17

"""5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成"""
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mal = 0
        ans = ''

        def is_palindrome(x, is_odd):
            if is_odd:
                l = 1
                p = s[x]
                x, y = x - 1, x + 1
            else:
                l = 0
                p = ''
                x, y = x, x + 1
            while x >= 0 and y < n and s[x] == s[y]:
                p = s[x] + p + s[y]
                l += 2
                x -= 1
                y += 1
            return l, p

        for i in range(n):
            l1, p1 = is_palindrome(i, False)
            if l1 > mal:
                mal = l1
                ans = p1
            l2, p2 = is_palindrome(i, True)
            if l2 > mal:
                mal = l2
                ans = p2
        return ans



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        begin, end = 0, 0

        def is_palindrome(x, y):
            while x >= 0 and y < n and s[x] == s[y]:
                x -= 1
                y += 1
            return x, y

        for i in range(n):
            left, right = is_palindrome(i, i)
            if end - begin < right - left:
                begin, end = left, right
            left, right = is_palindrome(i, i + 1)
            if end - begin < right - left:
                begin, end = left, right
        return s[begin + 1: end]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s[0]
        dp = [[False] * n for _ in range(n)]
        begin = 0
        max_len = 1
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            for i in range(n):
                # 左端点i 右端点j
                # 长度 L = j - i + 1
                j = i + L - 1

                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if L < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and max_len < L:
                    max_len = L
                    begin = i
        return s[begin:begin+max_len]


# sol = Solution()
# sol.longestPalindrome(s = "ac")

"""139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
 

提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        words = set(wordDict)

        for j in range(n):
            for i in range(j, -1, -1):
                if dp[i] and s[i: j+1] in words:
                    dp[j + 1] = True
                print(j, i, dp)
        return dp[n]



# sol = Solution()
# sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"])

# sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])

"""516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
 

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[''] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = s[i]
        max_len = 1

        for L in range(2, n+1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    if L < 3:
                        dp[i][j] = s[i] + s[j]
                    else:
                        dp[i][j] = s[i] + dp[i+1][j-1] + s[j]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], key=lambda x: len(x))
                if len(dp[i][j]) > max_len:
                    max_len = len(dp[i][j])
        return max_len


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        max_len = 1

        for L in range(2, n+1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
sol = Solution()
sol.longestPalindromeSubseq(s = "baaaaabbab")


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
# 动态规划


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1),  len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m+1):
            for j in range(n+1):
                # i=0或j=0的时候,向另一个单词插入j或i个字符即可
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    # dp[i][j]
                    """D[i][j-1] 为 A 的前 i 个字符和 B 的前 j - 1 个字符编辑距离的子问题。
                    即对于 B 的第 j 个字符，我们在 A 的末尾添加了一个相同的字符，
                    那么 D[i][j] 最小可以为 D[i][j-1] + 1；
                    D[i-1][j] 为 A 的前 i - 1 个字符和 B 的前 j 个字符编辑距离的子问题。
                    即对于 A 的第 i 个字符，我们在 B 的末尾添加了一个相同的字符，
                    那么 D[i][j] 最小可以为 D[i-1][j] + 1；
                    D[i-1][j-1] 为 A 前 i - 1 个字符和 B 的前 j - 1 个字符编辑距离的子问题。
                    即对于 B 的第 j 个字符，我们修改 A 的第 i 个字符使它们相同，
                    那么 D[i][j] 最小可以为 D[i-1][j-1] + 1。
                    特别地，如果 A 的第 i 个字符和 B 的第 j 个字符原本就相同，
                    那么我们实际上不需要进行修改操作。在这种情况下，D[i][j] 最小可以为 D[i-1][j-1]。"""

                    cnt = 0 if word1[i-1] == word2[j-1] else 1
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cnt)
        return dp[-1][-1]


# s = Solution()
# s.minDistance(word1 = "intention", word2 = "execution")


"""712. 两个字符串的最小ASCII删除和
给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。
示例 1:
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
示例 2:
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
提示:
0 <= s1.length, s2.length <= 1000
s1 和 s2 由小写英文字母组成"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]


s = Solution()
s.minimumDeleteSum(s1 = "a", s2 = "at")


"""115. 不同的子序列
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 109 + 7 取模。
示例 1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
babgbag
babgbag
babgbag
babgbag
babgbag
提示：
1 <= s.length, t.length <= 1000
s 和 t 由英文字母组成"""

# TODO
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):

                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i-1][j]
        return dp[m][n]
s = Solution()
# s.numDistinct(s = "rabbbit", t = "rabbit")

s.numDistinct(s = "babgbag", t = "bag")















































































































