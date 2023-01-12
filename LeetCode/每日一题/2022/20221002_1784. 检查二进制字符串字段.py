#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221002_1784. 检查二进制字符串字段.py
# @Author: Lin
# @Date  : 2022/10/10 15:40

# 给你一个二进制字符串 s ，该字符串 不含前导零 。
# 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
# 如果 s 中 由连续若干个 '1' 组成的字段 数量不超过 1，返回 true​​​ 。否则，返回 false 。
# 示例 1：
# 输入：s = "1001"
# 输出：false
# 解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
# 示例 2：
# 输入：s = "110"
# 输出：true
# 提示：
# 1 <= s.length <= 100
# s[i]​​​​ 为 '0' 或 '1'
# s[0] 为 '1'



class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        num, c = 0, ''

        for i in s:
            if i == '1' and i != c:
                num += 1
            c = i
        return num <= 1

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s



s = Solution()
s.checkOnesSegment(s = "110")