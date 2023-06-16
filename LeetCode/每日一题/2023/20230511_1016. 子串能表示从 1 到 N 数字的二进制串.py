#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230511_1016. 子串能表示从 1 到 N 数字的二进制串.py
# @Author: Lin
# @Date  : 2023/5/11 11:00

#
# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
#
# 子字符串 是字符串中连续的字符序列。
# 示例 1：
# 输入：s = "0110", n = 3
# 输出：true
# 示例 2：
# 输入：s = "0110", n = 4
# 输出：false
# 提示：
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 109

class Solution:
    def queryString(self, s: str, n: int) -> bool:

        return len(s)*(len(s)+1)//2>=n and all([bin(i)[2:] in s for i in range(1,n+1)])
s = Solution()
r = s.queryString(s = "0110", n = 4)
print(r)