#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230214_1124. 表现良好的最长时间段.py
# @Author: Lin
# @Date  : 2023/2/15 10:25

# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 请你返回「表现良好时间段」的最大长度。
# 示例 1：
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
# 输入：hours = [6,6,6]
# 输出：0
# 提示：
# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        h_map = dict()
        res = s = 0
        for i, h in enumerate(hours):
            s += 1 if h > 8 else - 1
            if s > 0:
                res = max(res, i + 1)
            else:
                if s-1 in h_map:
                    res = max(res, i - h_map[s-1])
            if s not in h_map:
                h_map[s] = i

        return res


s = Solution()
s.longestWPI(hours = [6,9,6])