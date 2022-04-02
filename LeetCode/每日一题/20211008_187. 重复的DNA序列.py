#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211008_187. 重复的DNA序列.py
# @Author: Lin
# @Date  : 2021/10/12 9:32
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
#
# 示例 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#  
# 提示：
#
# 0 <= s.length <= 105
# s[i] 为 'A'、'C'、'G' 或 'T'
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        arr = set()
        n = len(s)
        dic = {}
        for i in range(9, n):
            st = s[i-9: i+1]
            if st not in dic:
                dic[st] = 1
            else:
                arr.add(st)
        return list(arr)
