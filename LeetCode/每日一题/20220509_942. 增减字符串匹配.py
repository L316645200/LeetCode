#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220509_942. 增减字符串匹配.py
# @Author: Lin
# @Date  : 2022/5/12 15:44

# 由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
# 如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
# 如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
# 给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。
# 示例 1：
# 输入：s = "IDID"
# 输出：[0,4,1,3,2]
# 示例 2：
# 输入：s = "III"
# 输出：[0,1,2,3]
# 示例 3：
# 输入：s = "DDI"
# 输出：[3,2,0,1]
# 提示：
# 1 <= s.length <= 105
# s 只包含字符 "I" 或 "D"
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        left, right = 0, len(s)
        arr = []
        for i in s:
            if i == 'I':
               arr.append(left)
               left += 1
            else:
                arr.append(right)
                right -= 1
        arr.append(left)
        return arr



s = Solution()
s.diStringMatch("IDID")