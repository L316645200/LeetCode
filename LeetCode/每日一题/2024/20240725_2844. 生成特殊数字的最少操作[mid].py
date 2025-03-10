#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240725_2844. 生成特殊数字的最少操作[mid].py
# @Author  ：Lin
# @Date    ：2024/7/25 9:22


"""给你一个下标从 0 开始的字符串 num ，表示一个非负整数。

在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。

返回最少需要多少次操作可以使 num 变成特殊数字。

如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字。





示例 1：

输入：num = "2245047"
输出：2
解释：删除数字 num[5] 和 num[6] ，得到数字 "22450" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 2 位数字。
示例 2：

输入：num = "2908305"
输出：3
解释：删除 num[3]、num[4] 和 num[6] ，得到数字 "2900" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 3 位数字。
示例 3：

输入：num = "10"
输出：1
解释：删除 num[0] ，得到数字 "0" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 1 位数字。


提示

1 <= num.length <= 100
num 仅由数字 '0' 到 '9' 组成
num 不含任何前导零"""


class Solution:
    def minimumOperations(self, num: str) -> int:
        res = len(num)
        n = len(num)
        i, c, k = n - 1, 0, 0
        while i >= 0:
            if c == 0 and num[i] == '0':
                c += 1
            elif c == 1 and num[i] in ('0', '5'):
                return n - i - 2

            if k == 0 and num[i] == '5':
                k += 1
            elif k == 1 and num[i] in ('2', '7'):
                return n - i - 2
            i -= 1
        return n-1 if c == 1 else res



s = Solution()
s.minimumOperations(num = "2245047")