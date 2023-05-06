#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230427_.py
# @Author: Lin
# @Date  : 2023/4/27 10:33

# 给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
# 如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
# 例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
# 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。
# 从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。
# 示例 1：
# 输入：words = ["a","b","ba","bca","bda","bdca"]
# 输出：4
# 解释：最长单词链之一为 ["a","ba","bda","bdca"]
# 示例 2:
# 输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# 输出：5
# 解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# 示例 3:
# 输入：words = ["abcd","dbqca"]
# 输出：1
# 解释：字链["abcd"]是最长的字链之一。
# ["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。
# 提示：
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] 仅由小写英文字母组成。
#
from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        word_chain = defaultdict(dict)
        ans = 1
        for i, word in enumerate(words):
            word_chain[len(word)][word] = 1
            for word1, v in word_chain[len(word)-1].items():
                if self.is_predecessor(word1, word):
                    word_chain[len(word)][word] = max(word_chain[len(word)][word], v + 1)
                    ans = max(ans, v + 1)
        return ans

    def is_predecessor(self, word1, word2):
        i, j = 0, 0
        n = len(word1)
        while i < n and j < n + 1:
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if j - 1 <= i == n else False
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        words.sort(key=len)
        res = 0
        for word in words:
            cnt[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in cnt:
                    cnt[word] = max(cnt[word], cnt[prev] + 1)
            res = max(res, cnt[word])
        return res

s = Solution()
# s.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])

{1: {"a": 0, "b": 0}, 2: {"ba": 2}, }
s.longestStrChain(words =  ["a","ab","ac","bd","abc","abd","abdd"])


