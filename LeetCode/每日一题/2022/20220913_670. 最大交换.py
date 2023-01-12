#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220913_670. 最大交换.py
# @Author: Lin
# @Date  : 2022/9/13 16:27

# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
# 示例 1 :
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 示例 2 :
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
# 注意:
# 给定数字的范围是 [0, 10^8]


# 自我感觉写的挺棒的
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        i, n = 0, len(num)
        arr = [[i, num[n-1]] for i in range(n)]
        for i in range(n-2, -1, -1):
            if num[i] > arr[i+1][1]:
                arr[i] = [i, num[i]]
            else:
                arr[i] = [arr[i+1][0], arr[i+1][1]]

        for i in range(n):
            if arr[i][1] > num[i]:
                num[i], num[arr[i][0]] = num[arr[i][0]], num[i]
                break
        return int(''.join(num))


# 官解，列表最大值改为变量保存足矣，空间复杂度优化
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


if __name__ == '__main__':

    s = Solution()
    s.maximumSwap(2736)
    s.maximumSwap(9973)


