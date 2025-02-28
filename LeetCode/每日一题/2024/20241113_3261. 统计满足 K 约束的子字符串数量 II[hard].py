#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241113_3261. 统计满足 K 约束的子字符串数量 II[hard].py
# @Author  ：Lin
# @Date    ：2024/11/13 10:11

"""3261. 统计满足 K 约束的子字符串数量 II 2659 子串的子串
给你一个 二进制 字符串 s 和一个整数 k。
另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。
如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
字符串中 0 的数量最多为 k。
字符串中 1 的数量最多为 k。
返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的
子字符串
 的数量。
示例 1：
输入：s = "0001111", k = 2, queries = [[0,6]]
输出：[26]
解释：
对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。
示例 2：
输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]
输出：[15,9,3]
解释：
s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。
提示：
1 <= s.length <= 105
s[i] 是 '0' 或 '1'
1 <= k <= s.length
1 <= queries.length <= 105
queries[i] == [li, ri]
0 <= li <= ri < s.length
所有查询互不相同
"""
import bisect
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = 0
        left_arr = [0] * n
        pre = [0] * (n + 1)
        cnt = [0, 0]
        for right in range(n):
            cnt[ord(s[right]) & 1] += 1
            while min(cnt[0], cnt[1]) > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            left_arr[right] = left
            pre[right+1] += pre[right] + right - left + 1
        res = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            j = bisect.bisect_left(left_arr, left, left, right+1)
            res[i] = pre[right+1] - pre[j] + (j-left+1) * (j - left) // 2
        return res


s = Solution()
s.countKConstraintSubstrings(s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]])
