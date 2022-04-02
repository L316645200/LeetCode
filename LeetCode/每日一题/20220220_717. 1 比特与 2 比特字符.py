#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220220_717. 1 比特与 2 比特字符.py
# @Author: Lin
# @Date  : 2022/2/21 11:16

# 有两种特殊字符：
# 第一种字符可以用一比特 0 表示
# 第二种字符可以用两比特（10 或 11）表示
# 给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。
#
# 示例 1:
# 输入: bits = [1, 0, 0]
# 输出: true
# 解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
# 所以最后一个字符是一比特字符。
# 示例 2:
# 输入：bits = [1,1,1,0]
# 输出：false
# 解释：唯一的解码方式是将其解析为两比特字符和两比特字符。
# 所以最后一个字符不是一比特字符。
#  
# 提示:
# 1 <= bits.length <= 1000
# bits[i] 为 0 或 1
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = 0
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == 1:
                n += 1
            else:
                break
        return n % 2 == 0
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = n - 2
        while i >= 0 and bits[i]:
            i -= 1
        return (n - i) % 2 == 0


s = Solution()
s.isOneBitCharacter([1,1,1,0])