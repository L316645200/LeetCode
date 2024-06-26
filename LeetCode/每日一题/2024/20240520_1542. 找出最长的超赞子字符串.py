#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240520_1542. 找出最长的超赞子字符串.py
# @Author  ：Lin
# @Date    ：2024/5/20 11:01

"""给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
「超赞子字符串」需满足满足下述两个条件：
该字符串是 s 的一个非空子字符串
进行任意次数的字符交换后，该字符串可以变成一个回文字符串
示例 1：
输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
示例 2：
输入：s = "12345678"
输出：1
示例 3：
输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
示例 4：
输入：s = "00"
输出：2
提示：
1 <= s.length <= 10^5
s 仅由数字组成"""


# TODO 官解，有点复杂，看不懂
class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        prefix = {0: -1}
        ans, sequence = 0, 0

        for j in range(n):
            digit = ord(s[j]) - ord("0")  # <> int(s[j])

            sequence ^= (1 << digit)
            if sequence in prefix:
                ans = max(ans, j - prefix[sequence])
            else:
                prefix[sequence] = j
            for k in range(10):
                if sequence ^ (1 << k) in prefix:
                    ans = max(ans, j - prefix[sequence ^ (1 << k)])
        return ans


s = Solution()
s.longestAwesome(s = "3242415")