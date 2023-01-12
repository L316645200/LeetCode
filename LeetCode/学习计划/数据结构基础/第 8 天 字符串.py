#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 8 天 字符串.py
# @Author: Lin
# @Date  : 2022/10/27 16:09.
# 49. 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
# 提示：
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsdict = defaultdict(list)
        [strsdict[''.join(sorted(str))].append(str) for str in strs]
        return list(strsdict.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


s = Solution()
s.groupAnagrams(strs = [""])


# 43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 提示：
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1), len(num2)
        arr = [0] * (n1 + n2)

        for i in range(n1):
            x = int(num1[i])
            for j in range(n2):
                arr[i+j+1] += x * int(num2[j])
        for i in range(n1+n2-1, 0, -1):
            x, y = divmod(arr[i], 10)
            arr[i-1], arr[i] = arr[i-1] + x, y
        index = 1 if arr[0] == 0 else 0
        return ''.join([str(i) for i in arr[index:]])


s = Solution()
s.multiply(num1 = "123", num2 = "456")