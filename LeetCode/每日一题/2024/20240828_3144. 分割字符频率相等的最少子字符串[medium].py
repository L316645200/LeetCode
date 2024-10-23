#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240828_3144. 分割字符频率相等的最少子字符串[medium].py
# @Author  ：Lin
# @Date    ：2024/8/28 16:00

"""给你一个字符串 s ，你需要将它分割成一个或者更多的 平衡 子字符串。比方说，s == "ababcc" 那么 ("abab", "c", "c") ，("ab", "abc", "c") 和 ("ababcc") 都是合法分割，但是 ("a", "bab", "cc") ，("aba", "bc", "c") 和 ("ab", "abcc") 不是，不平衡的子字符串用粗体表示。
请你返回 s 最少 能分割成多少个平衡子字符串。
注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。
示例 1：
输入：s = "fabccddg"
输出：3
解释：
我们可以将 s 分割成 3 个子字符串：("fab, "ccdd", "g") 或者 ("fabc", "cd", "dg") 。
示例 2：
输入：s = "abababaccddb"
输出：2
解释：
我们可以将 s 分割成 2 个子字符串：("abab", "abaccddb") 。
提示：
1 <= s.length <= 1000
s 只包含小写英文字母。"""
from cmath import inf
from collections import defaultdict
from functools import cache


"""首先说明，分割方案是一定存在的，因为单个字母是平衡的，
我们一定可以把 s 划分成 n 个平衡子串。

一、寻找子问题
示例 1 的 s=fabccddg，枚举最后一段的长度：

最后一段分割出一个长为 1 的子串，即 g，这是平衡的，
问题变成剩余字符串 fabccdd 最少能分割出多少个平衡子串。
最后一段分割出一个长为 2 的子串，即 dg，这是平衡的，
问题变成剩余字符串 fabccd 最少能分割出多少个平衡子串。
……
在这个过程中，我们只需要知道剩余字符串的长度，因为剩余字符串一定是 s 的一个前缀。

这些问题都是和原问题相似的、规模更小的子问题，可以用递归解决。

注 1：从右往左思考，主要是为了方便把递归翻译成递推。从左往右思考也是可以的。

注 2：动态规划有「选或不选」和「枚举选哪个」两种基本思考方式。在做题时，可根据题目要求，
选择适合题目的一种来思考。本题用到的是「枚举选哪个」。

二、状态定义与状态转移方程
根据上面的讨论，我们只需要在递归过程中跟踪以下信息：

i：剩余字符串是 s[0] 到 s[i]。
因此，定义状态为 dfs(i)，表示当剩余字符串是 s[0] 到 s[i] 时，
最少能分割出多少个平衡子串。

枚举最后一段从 s[j] 到 s[i]，如果这个子串是平衡的，那么接下来要解决的问题是：
当剩余字符串是 s[0] 到 s[j−1] 时，最少能分割出多少个平衡子串，即 dfs(j−1)。

枚举所有小于等于 i 的 j，取 dfs(j−1) 的最小值，即

dfs(i)= 
j=0
min
i
​
 dfs(j−1)+1
其中 s[j] 到 s[i] 是平衡子串。

如何快速判断子串是平衡的呢？

我们可以在倒序枚举 j 的同时，用一个哈希表（或者数组）统计每个字符的出现次数。
如果子串中每个字母的出现次数都相等，那么子串是平衡的。

优化：设子串中有 k 种字母，字母出现次数的最大值为 maxCnt。子串是平衡的，
当且仅当子串长度 i−j+1 等于 k⋅maxCnt。

递归边界：dfs(−1)=0。

递归入口：dfs(n−1)，也就是答案。
"""
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i == -1:
                return 0
            cnt = defaultdict(int)
            max_cnt = 0
            res = i
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                if max_cnt * len(cnt) == i - j + 1:
                    res = min(res, dfs(j - 1))
            return res + 1
        return dfs(n - 1)


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(n):
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                if max_cnt * len(cnt) == i - j + 1:
                    f[i+1] = min(f[i+1], f[j] + 1)
        return f[n]

s = Solution()
s.minimumSubstringsInPartition(s = "fabccddg")