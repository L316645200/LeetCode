#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240113_2182. 构造限制重复的字符串.py
# @Author  ：Lin
# @Date    ：2024/1/13 11:33

"""给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。



示例 1：

输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
示例 2：

输入：s = "aababab", repeatLimit = 2
输出："bbabaa"
解释：
使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。
字母 'a' 连续出现至多 2 次。
字母 'b' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。
注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。


提示：

1 <= repeatLimit <= s.length <= 105
s 由小写英文字母组成"""
import heapq
from collections import Counter

# 最大堆
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # 计数
        cnt = Counter(s)
        # 构造大根堆
        heap = [-ord(k) for k in cnt.keys()]
        heapq.heapify(heap)
        ans = ''
        #
        while heap:
            c = heapq.heappop(heap)
            letter = chr(-c)
            if cnt[letter] <= repeatLimit:
                ans += letter * cnt[letter]
                cnt.pop(letter)
            else:
                cnt[letter] -= repeatLimit
                ans += letter * repeatLimit
                if not heap:
                    break
                else:
                    c2 = heapq.heappop(heap)
                    letter2 = chr(-c2)
                    ans += letter2
                    if cnt[letter2] > 1:
                        heapq.heappush(heap, c2)
                        cnt[letter2] -= 1
                    else:
                        cnt.pop(letter2)
                heapq.heappush(heap, c)
        return ans



# class Solution:
#     def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
#         n = 26
#         count = [0] * n
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         i, j, m = n - 1, n - 2, 0
#         ret = []
#         while i >= 0 and j >= 0:
#             if count[i] == 0:
#                 i -= 1
#                 m = 0
#             elif m < repeatLimit:
#                 m += 1
#                 count[i] -= 1
#                 ret.append(chr(ord('a') + i))
#             elif j >= i or count[j] == 0:
#                 j -= 1
#             else:
#                 count[j] -= 1
#                 m = 0
#                 ret.append(chr(ord('a') + j))
#         return ''.join(ret)
#

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = 26
        count = [0] * N
        for c in s:
            count[ord(c) - ord('a')] += 1
        ret = []
        i, j, m = N - 1, N - 2, 0
        while i >= 0 and j >= 0:
            if count[i] == 0: # 当前字符已经填完，填入后面的字符，重置 m
                m, i = 0, i - 1
            elif m < repeatLimit: # 当前字符未超过限制
                count[i] -= 1
                ret.append(chr(ord('a') + i))
                m += 1
            elif j >= i or count[j] == 0: # 当前字符已经超过限制，查找可填入的其他字符
                j -= 1
            else: # 当前字符已经超过限制，填入其他字符，并且重置 m
                count[j] -= 1
                ret.append(chr(ord('a') + j))
                m = 0
        return ''.join(ret)




s = Solution()
s.repeatLimitedString(s = "cczazcc", repeatLimit = 3)