#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250109_3297. 统计重新排列后包含另一个字符串的子字符串数目 I[medium].py
# @Author  ：Lin
# @Date    ：2025/1/9 9:33
"""给你两个字符串 word1 和 word2 。
如果一个字符串 x 重新排列后，word2 是重排字符串的
前缀
 ，那么我们称字符串 x 是 合法的 。
请你返回 word1 中 合法
子字符串
 的数目。
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
1 <= word1.length <= 105
1 <= word2.length <= 104
word1 和 word2 都只包含小写英文字母。"""
from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        cnt1 = Counter()
        diff = len(cnt2)
        res = j = 0
        n = len(word1)
        for i, c in enumerate(word1):
            cnt1[c] += 1
            if cnt1[c] == cnt2[c]:
                diff -= 1
            while diff == 0:
                res += n - i
                cnt1[word1[j]] -= 1
                if cnt1[word1[j]] < cnt2[word1[j]]:
                    diff += 1
                j += 1
        return res

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        """
        计算 word1 中包含 word2 前缀的子串个数

        参数:
            word1: 主字符串
            word2: 目标前缀字符串

        返回:
            int: 包含目标前缀的子串个数
        """
        # 初始化计数器，用于记录 word2 中每个字符的出现次数
        cnt = Counter(word2)
        # 初始化差异计数器，用于记录 word2 中尚未在当前窗口中出现的字符个数
        diff = len(cnt)
        # 初始化结果计数器和窗口起始位置
        res = j = 0
        # 获取 word1 的长度
        n = len(word1)

        # 遍历 word1 中的每个字符
        for i, c in enumerate(word1):
            # 减少当前字符在计数器中的出现次数
            cnt[c] -= 1
            # 如果当前字符的出现次数为 0，则表示该字符已经在当前窗口中出现
            if cnt[c] == 0:
                # 更新差异计数器，表示已经找到一个字符
                diff -= 1
            # 当差异计数器为 0 时，表示当前窗口中的子串包含了 word2 中的所有字符
            while diff == 0:
                # 增加结果计数器，计算当前窗口后面的字符个数
                res += n - i
                # 如果窗口起始位置的字符在计数器中的出现次数为 0，则表示该字符是 word2 中的最后一个字符
                if cnt[word1[j]] == 0:
                    # 更新差异计数器，表示需要找到下一个字符
                    diff += 1
                # 增加窗口起始位置字符的出现次数
                cnt[word1[j]] += 1
                # 移动窗口起始位置
                j += 1

        # 返回包含目标前缀的子串个数
        return res

s = Solution()
s.validSubstringCount(word1 = "abcabc", word2 = "abc")