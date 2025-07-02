#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/7 11:29
# @Author  : Lin
# @File    : 20250607_3170. 删除星号以后字典序最小的字符串[mid].py
"""给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。
当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：
删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
请你返回删除所有 '*' 字符以后，剩余字符连接而成的 字典序最小 的字符串。
示例 1：
输入：s = "aaba*"
输出："aab"
解释：
删除 '*' 号和它左边的其中一个 'a' 字符。如果我们选择删除 s[3] ，s 字典序最小。
示例 2：
输入：s = "abc"
输出："abc"
解释：
字符串中没有 '*' 字符。
提示：
1 <= s.length <= 105
s 只含有小写英文字母和 '*' 字符。
输入保证操作可以删除所有的 '*' 字符。"""
from itertools import chain

"""
思路：
从左到右遍历 s，用 26 个栈记录遍历过的每种字母的下标。
遇到*，弹出最小字母栈（第一个非空栈）的栈顶。
最后把剩余下标对应的字母按顺序串起来，即为答案。
"""
class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    st.pop()
                    break
        # chain.from_iterable()展平可迭代对象
        return ''.join(s[i] for i in sorted(chain.from_iterable(stacks)))


# 把要弹出的字母改为*,最后把不是*的字母连接起来就可以，省去排序
class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    s[st.pop()] = '*'
                    break
        return ''.join(c for c in s if c != '*')
