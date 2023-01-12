#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220707_648. 单词替换.py
# @Author: Lin
# @Date  : 2022/7/7 15:23

# 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
# 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
# 你需要输出替换之后的句子。
# 示例 1：
# 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# 输出："the cat was rat by the bat"
# 示例 2：
# 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# 输出："a a b c"
#  
# 提示：
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] 仅由小写字母组成。
# 1 <= sentence.length <= 10^6
# sentence 仅由小写字母和空格组成。
# sentence 中单词的总量在范围 [1, 1000] 内。
# sentence 中每个单词的长度在范围 [1, 1000] 内。
# sentence 中单词之间由一个空格隔开。
# sentence 没有前导或尾随空格。
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary_set = set(dictionary)
        words = sentence.split(' ')
        for i, v in enumerate(words):
            for j in range(1, len(v)+1):
                print(i,j,v[:j])
                if v[:j] in dictionary_set:
                    words[i] = v[:j]
                    break
        print(words)
        print(' '.join(words))
        return ' '.join(words)


# 字典树
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}  # #标记结尾
            print(trie)
        # 将dictionary的词根构建成字典树，并用#标记结尾，以上部分
        # 在搜索前缀时，在字典树上搜索除一条最短路劲即可，以下部分

        words = sentence.split(' ')
        for i, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if '#' in cur:  # 存在前缀结尾
                    words[i] = word[:j]
                    break
                if c not in cur:  # 不存在，说明没有以此开头的
                    break
                cur = cur[c]  # 进入字典树下级
        return ' '.join(words)


s = Solution()
s.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")



