#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天 字符串.py
# @Author: Lin
# @Date  : 2021/10/22 9:29
# 387. 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 示例：
# s = "leetcode"
# 返回 0
# s = "loveleetcode"
# 返回 2
#
# 提示：你可以假定该字符串只包含小写字母。
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, v in enumerate(s):
            dic[v] = i if v not in dic else -1
        for k, v in dic.items():
            if v != -1:
                return v
        return -1



# s = Solution()
# r = s.firstUniqChar('leetcode')
# print(r)
# 383. 赎金信
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# 示例 1：
#
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 示例 2：
#
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 示例 3：
#
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 提示：
# 你可以假设两个字符串均只含有小写字母。



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for r in ransomNote:
            if r not in ransomNote or c[r] < 1:
                return False
            else:
                c[r] -= 1
        return True


s = Solution()
r = s.canConstruct('aa', 'aab')
print(r)

# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#  
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)



s = Solution()
r = s.isAnagram('anagram', 'nagaram')
print(r)







