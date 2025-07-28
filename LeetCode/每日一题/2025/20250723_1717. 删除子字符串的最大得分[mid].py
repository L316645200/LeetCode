#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/7/23 21:08
# @Author  : Lin
# @File    : 20250723_1717. 删除子字符串的最大得分[mid].py

"""给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
删除子字符串 "ab" 并得到 x 分。
比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
删除子字符串"ba" 并得到 y 分。
比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
请返回对 s 字符串执行上面操作若干次能得到的最大得分。
示例 1：
输入：s = "cdbcbbaaabab", x = 4, y = 5
输出：19
解释：
- 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
- 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
- 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
- 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
总得分为 5 + 4 + 5 + 5 = 19 。
示例 2：
输入：s = "aabbaaxybbaabb", x = 5, y = 4
输出：20
提示：
1 <= s.length <= 105
1 <= x, y <= 104
s 只包含小写英文字母。"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            x, y = y, x
            s = ''.join(['b' if c == 'a' else 'a' if c == 'b' else c for c in s])
        ans = i = 0
        n = len(s)
        while i < n:
            cntA = cntB = 0
            while i < n and s[i] in 'ab':
                if s[i] == 'a':
                    cntA += 1
                else:
                    if cntA > 0:
                        cntA -= 1
                        ans += x
                    else:
                        cntB += 1
                i += 1
            i += 1
            ans += min(cntA, cntB) * y
        return ans


s = Solution()
s.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5)