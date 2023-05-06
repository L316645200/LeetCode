#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230506_1419. 数青蛙.py
# @Author: Lin
# @Date  : 2023/5/6 9:57

#
# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。
# 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
# 要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。
# 示例 1：
# 输入：croakOfFrogs = "croakcroak"
# 输出：1
# 解释：一只青蛙 “呱呱” 两次
# 示例 2：
# 输入：croakOfFrogs = "crcoakroak"
# 输出：2
# 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
# 第一只青蛙 "crcoakroak"
# 第二只青蛙 "crcoakroak"
# 示例 3：
# 输入：croakOfFrogs = "croakcrook"
# 输出：-1
# 解释：给出的字符串不是 "croak" 的有效组合。
# 提示：
#
# 1 <= croakOfFrogs.length <= 105
# 字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'
from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = defaultdict(int)
        prec = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        ans, n = 0, 0
        for croak in croakOfFrogs:
            print(croak, n)
            cnt[croak] += 1
            if croak == 'c':
                n += 1
                ans = max(ans, n)
            else:
                if cnt[prec[croak]] == 0:
                    return -1
                if croak == 'k':
                    n -= 1
                cnt[prec[croak]] -= 1
        if n > 0:
            return -1
        return ans


s = Solution()
s.minNumberOfFrogs(croakOfFrogs = "croakcrook")