#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221020_779. 第K个语法符号.py
# @Author: Lin
# @Date  : 2022/10/20 10:49

# 我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
# 给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）
# 示例 1:
# 输入: n = 1, k = 1
# 输出: 0
# 解释: 第一行：0
# 示例 2:
# 输入: n = 2, k = 1
# 输出: 0
# 解释:
# 第一行: 0
# 第二行: 01
# 示例 3:
# 输入: n = 2, k = 2
# 输出: 1
# 解释:
# 第一行: 0
# 第二行: 01
# 提示:
# 1 <= n <= 30
# 1 <= k <= 2n - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/k-th-symbol-in-grammar
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (1 - k % 2) ^ self.kthGrammar(n - 1, (k + 1) // 2)


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (k & 1) ^ 1 ^ self.kthGrammar(n - 1, (k + 1) // 2)


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k > (1 << (n - 2)):
            return 1 ^ self.kthGrammar(n - 1, k - (1 << (n - 2)))
        return self.kthGrammar(n - 1, k)


s = Solution()
r = s.kthGrammar(n = 2, k = 2)
print(r)