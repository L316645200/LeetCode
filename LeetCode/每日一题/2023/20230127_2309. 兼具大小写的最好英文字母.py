#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230127_2309. 兼具大小写的最好英文字母.py
# @Author: Lin
# @Date  : 2023/2/4 16:37
from string import ascii_lowercase, ascii_uppercase

# 给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
# 最好 英文字母的大写和小写形式必须 都 在 s 中出现。
# 英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。
# 示例 1：
# 输入：s = "lEeTcOdE"
# 输出："E"
# 解释：
# 字母 'E' 是唯一一个大写和小写形式都出现的字母。
# 示例 2：
# 输入：s = "arRAzFif"
# 输出："R"
# 解释：
# 字母 'R' 是大写和小写形式都出现的最好英文字母。
# 注意 'A' 和 'F' 的大写和小写形式也都出现了，但是 'R' 比 'F' 和 'A' 更好。
# 示例 3：
# 输入：s = "AbCdEfGhIjK"
# 输出：""
# 解释：
# 不存在大写和小写形式都出现的字母。
# 提示：
# 1 <= s.length <= 1000
# s 由小写和大写英文字母组成


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for lower, upper in zip(reversed(ascii_lowercase), reversed(ascii_uppercase)):
            if lower in s and upper in s:
                return upper
        return ""
