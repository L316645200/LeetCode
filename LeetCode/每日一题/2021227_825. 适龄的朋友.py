#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2021227_825. 适龄的朋友.py
# @Author: Lin
# @Date  : 2021/12/27 11:29
# 在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。
#
# 如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# 否则，x 将会向 y 发送一条好友请求。
# 注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。
# 返回在该社交媒体网站上产生的好友请求总数。

# 示例 1：
# 输入：ages = [16,16]
# 输出：2
# 解释：2 人互发好友请求。
# 示例 2：
# 输入：ages = [16,17,18]
# 输出：2
# 解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
# 示例 3：
# 输入：ages = [20,30,100,110,120]
# 输出：3
# 解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。
#
# 提示：
# n == ages.length
# 1 <= n <= 2 * 104
# 1 <= ages[i] <= 120
from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        print(ages)
        l = len(ages) - 1
        left, right = 0, 0
        r = 0
        while left < l and right <= l:
            print(left, right, r)
            if left == right:
                right += 1
                if not self.check(ages[left], ages[right]):
                    left += 1
            else:
                if right < l and self.check(ages[left], ages[right+1]):
                    right += 1
                else:
                    r += right - left
                    left += 1
        return r + sum([v*(v-1)//2 for k, v in Counter(ages).items() if k > 14])

    @staticmethod
    def check(y, x):
        return not ((y <= (0.5 * x + 7)) or (y > x) or ((y > 100) & (x < 100)))


s = Solution()
# s.numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])
s.numFriendRequests([16,16])




