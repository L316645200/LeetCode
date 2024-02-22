#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240122_670. 最大交换.py
# @Author  ：Lin
# @Date    ：2024/1/22 10:50


"""给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 10^8]"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        prefix = [[num_list[n-1], n-1]] * n
        for i in range(n-2, -1, -1):
            if prefix[i+1][0] >= num_list[i]:
                prefix[i] = prefix[i+1]
            else:
                prefix[i] = [num_list[i], i]

        for i in range(n):
            if num_list[i] < prefix[i][0]:
                num_list[i], num_list[prefix[i][1]] = prefix[i][0], num_list[i]
                break
        return int(''.join(num_list))


s = Solution()
s.maximumSwap(2736)

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))

