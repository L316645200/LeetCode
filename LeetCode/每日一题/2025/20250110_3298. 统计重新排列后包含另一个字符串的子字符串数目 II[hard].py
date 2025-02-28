#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250110_3298. 统计重新排列后包含另一个字符串的子字符串数目 II[hard].py
# @Author  ：Lin
# @Date    ：2025/1/10 9:25
"""给你两个字符串 word1 和 word2 。

如果一个字符串 x 重新排列后，word2 是重排字符串的
前缀
 ，那么我们称字符串 x 是 合法的 。

请你返回 word1 中 合法
子字符串
 的数目。

注意 ，这个问题中的内存限制比其他题目要 小 ，所以你 必须 实现一个线性复杂度的解法。



示例 1：

输入：word1 = "bcca", word2 = "abc"

输出：1

解释：

唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。

示例 2：

输入：word1 = "abcabc", word2 = "abc"

输出：10

解释：

除了长度为 1 和 2 的所有子字符串都是合法的。

示例 3：

输入：word1 = "abcabc", word2 = "aaabc"

输出：0



解释：

1 <= word1.length <= 106
1 <= word2.length <= 104
word1 和 word2 都只包含小写英文字母。"""
from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        """
        计算 word1 中包含 word2 前缀的子串个数

        参数:
            word1 (str): 主字符串
            word2 (str): 目标前缀字符串

        返回:
            int: 包含目标前缀的子串个数
        """
        # 初始化计数器，用于记录 word2 中每个字符的出现次数
        cnt = Counter(word2)
        # 记录 word2 中不同字符的数量
        diff = len(cnt)
        # 初始化结果变量，用于存储符合条件的子串个数
        res = j = 0
        n = len(word1)
        for i, c in enumerate(word1):
            # 减少当前字符在计数器中的出现次数
            cnt[c] -= 1
            # 如果当前字符的出现次数变为 0，则不同字符的数量减 1
            if cnt[c] == 0:
                diff -= 1
            # 如果不同字符的数量变为 0，表示当前子串包含 word2 作为前缀
            while diff == 0:
                # 累加结果，计算当前位置到字符串末尾的所有子串个数
                res += n - i
                # 如果 word1 中当前位置的字符在计数器中的出现次数变为 0，则不同字符的数量加 1
                if cnt[word1[j]] == 0:
                    diff += 1
                # 移动窗口的起始位置
                cnt[word1[j]] += 1
                j += 1
        return res