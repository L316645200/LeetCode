#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220908_667. 优美的排列 II.py
# @Author: Lin
# @Date  : 2022/9/8 15:50

# 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：
# 假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。
# 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。
# 示例 1：
# 输入：n = 3, k = 1
# 输出：[1, 2, 3]
# 解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1
# 示例 2：
# 输入：n = 3, k = 2
# 输出：[1, 3, 2]
# 解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2
# 提示：
# 1 <= k < n <= 104
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return [i + 1 for i in range(n)]
        elif k == 2:
            return [2, 1] + [i + 1 for i in range(2, n)]

        arr = [1, n] + [0] * (n - 2)
        i = 2
        while i < k:
            if i % 2 == 0:
                arr[i] = arr[i-2] + 1
            else:
                arr[i] = n - arr[i-1] + 1
            i += 1
        t = 1 if i % 2 != 0 else -1
        for j in range(i, n):
            arr[j] = arr[j-1] + t
        return arr

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        print(answer)
        return answer

s = Solution()
s.constructArray(n = 10, k = 4)