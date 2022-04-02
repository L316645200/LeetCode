#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220307_504. 七进制数.py
# @Author: Lin
# @Date  : 2022/3/7 15:11
#
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
#
# 示例 1:
# 输入: num = 100
# 输出: "202"
# 示例 2:
# 输入: num = -7
# 输出: "-10"
#
# 提示：
# -107 <= num <= 107



class Solution:
    def convertToBase7(self, num: int) -> str:
        res, digit = '', 7
        abs_num = abs(num)

        while abs_num >= digit:
            abs_num, x = divmod(abs_num, digit)
            res = str(x) + res
        res = str(abs_num) + res if abs_num >= 0 else res
        return res if num >= 0 else '-' + res


s = Solution()
n = s.convertToBase7(0)
print(n)

