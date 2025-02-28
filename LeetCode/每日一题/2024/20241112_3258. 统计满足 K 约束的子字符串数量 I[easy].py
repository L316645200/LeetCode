#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241112_3258. 统计满足 K 约束的子字符串数量 I[easy].py
# @Author  ：Lin
# @Date    ：2024/11/13 10:12

"""给你一个 二进制 字符串 s 和一个整数 k。

如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：

字符串中 0 的数量最多为 k。
字符串中 1 的数量最多为 k。
返回一个整数，表示 s 的所有满足 k 约束 的
子字符串
的数量。



示例 1：

输入：s = "10101", k = 1

输出：12

解释：

s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。

示例 2：

输入：s = "1010101", k = 2

输出：25

解释：

s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。

示例 3：

输入：s = "11111", k = 1

输出：15

解释：

s 的所有子字符串都满足 k 约束。



提示：

1 <= s.length <= 50
1 <= k <= s.length
s[i] 是 '0' 或 '1'。"""

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int, {'0': 0, '1': 0})
        res = left = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            while min(cnt.values()) > k:
                cnt[s[left]] -= 1
                left += 1
            res += right - left + 1
        return res

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = [0, 0]
        res = left = 0
        for right in range(len(s)):
            cnt[ord(s[right]) & 1] += 1
            while min(cnt[0], cnt[1]) > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            res += right - left + 1
        return res
s = Solution()
s.countKConstraintSubstrings(s = "10101", k = 1)