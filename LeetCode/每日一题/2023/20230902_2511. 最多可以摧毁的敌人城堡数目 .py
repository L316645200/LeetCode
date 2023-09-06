#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230902_2511. 最多可以摧毁的敌人城堡数目 .py
# @Author: Lin
# @Date  : 2023/9/4 18:40

"""给你一个长度为 n ，下标从 0 开始的整数数组 forts ，表示一些城堡。forts[i] 可以是 -1 ，0 或者 1 ，其中：

-1 表示第 i 个位置 没有 城堡。
0 表示第 i 个位置有一个 敌人 的城堡。
1 表示第 i 个位置有一个你控制的城堡。
现在，你需要决定，将你的军队从某个你控制的城堡位置 i 移动到一个空的位置 j ，满足：

0 <= i, j <= n - 1
军队经过的位置 只有 敌人的城堡。正式的，对于所有 min(i,j) < k < max(i,j) 的 k ，都满足 forts[k] == 0 。
当军队移动时，所有途中经过的敌人城堡都会被 摧毁 。

请你返回 最多 可以摧毁的敌人城堡数目。如果 无法 移动你的军队，或者没有你控制的城堡，请返回 0 。

 

示例 1：

输入：forts = [1,0,0,-1,0,0,0,0,1]
输出：4
解释：
- 将军队从位置 0 移动到位置 3 ，摧毁 2 个敌人城堡，位置分别在 1 和 2 。
- 将军队从位置 8 移动到位置 3 ，摧毁 4 个敌人城堡。
4 是最多可以摧毁的敌人城堡数目，所以我们返回 4 。
示例 2：

输入：forts = [0,0,1,-1]
输出：0
解释：由于无法摧毁敌人的城堡，所以返回 0 。
 

提示：

1 <= forts.length <= 1000
-1 <= forts[i] <= 1"""""
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        res = 0
        for i in range(n):
            if forts[i] == -1:
                j = i - 1
                k = i + 1
                while j >= 0:
                    if forts[j] == 0:
                        j -= 1
                    elif forts[j] == 1:
                        res = max(res, i - j - 1)
                        break
                    else:
                        break
                while k < n:
                    if forts[k] == 0:
                        k += 1
                    elif forts[k] == 1:
                        res = max(res, k - i - 1)
                        break
                    else:
                        break
        return res


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = 0
        n = len(forts)
        pre, record_val = 0, 0
        for i in range(n):
            if forts[i] == 1 or forts[i] == -1:
                if record_val == -forts[i]:
                    res = max(res, i - pre - 1)
                record_val = forts[i]
                pre = i
        return res


# 精简再精简
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        pre, ans = -1, 0
        for i, fort in enumerate(forts):
            if forts[i] == 1 or forts[i] == -1:
                if pre >= 0 and forts[i] != forts[pre]:
                    ans = max(ans, i - pre - 1)
                pre = i
        return ans


s = Solution()
s.captureForts(forts = [1,0,0,-1,0,0,0,0,1])
