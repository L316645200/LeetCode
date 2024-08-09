#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240627_2734. 执行子串操作后的字典序最小字符串[mid].py
# @Author  ：Lin
# @Date    ：2024/6/27 9:43

"""给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以完成以下行为：

选择 s 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。

子字符串 是字符串中的一个连续字符序列。

现有长度相同的两个字符串 x 和 字符串 y ，在满足 x[i] != y[i] 的第一个位置 i 上，如果  x[i] 在字母表中先于 y[i] 出现，则认为字符串 x 比字符串 y 字典序更小 。


示例 1：

输入：s = "cbabc"
输出："baabc"
解释：我们选择从下标 0 开始、到下标 1 结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
示例 2：

输入：s = "acbbc"
输出："abaab"
解释：我们选择从下标 1 开始、到下标 4 结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
示例 3：

输入：s = "leetcode"
输出："kddsbncd"
解释：我们选择整个字符串执行操作。
可以证明最终得到的字符串是字典序最小的。


提示：

1 <= s.length <= 3 * 105
s 仅由小写英文字母组成"""


class Solution:
    def smallestString(self, s: str) -> str:
        arr = list(s)
        mark = 0
        for i in range(len(s)):
            if arr[i] != 'a':
                mark = 1
                arr[i] = chr(max(ord(s[i]) - 1, ord('a')))

            elif mark == 1:
                break
        if mark == 0:
            arr[-1] = 'z'
        return ''.join(arr)


# class Solution:
#     def smallestString(self, s: str) -> str:
#         indexOfFirstNonA = self.findFirstNonA(s)
#         if indexOfFirstNonA == len(s):
#             return s[:-1] + 'z'
#         indexOfFirstA_AfterFirstNonA = self.findFirstA_AfterFirstNonA(s, indexOfFirstNonA)
#         res = []
#         for i, c in enumerate(s):
#             if indexOfFirstNonA <= i < indexOfFirstA_AfterFirstNonA:
#                 res.append(chr(ord(c)-1))
#             else:
#                 res.append(c)
#         return ''.join(res)
#
#     def findFirstNonA(self, s: str) -> int:
#         for i, c in enumerate(s):
#             if c != 'a':
#                 return i
#         return len(s)
#
#     def findFirstA_AfterFirstNonA(self, s:str, firstNonA: int) -> int:
#         for i in range(firstNonA, len(s)):
#             if s[i] == 'a':
#                 return i
#         return len(s)



s = Solution()
s.smallestString(s = "leetcode")