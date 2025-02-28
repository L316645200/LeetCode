#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241117_825. 适龄的朋友[medium].py
# @Author  ：Lin
# @Date    ：2024/11/18 10:24

"""在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

ages[y] <= 0.5 * ages[x] + 7
ages[y] > ages[x]
ages[y] > 100 && ages[x] < 100
否则，x 将会向 y 发送一条好友请求。

注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

返回在该社交媒体网站上产生的好友请求总数。



示例 1：

输入：ages = [16,16]
输出：2
解释：2 人互发好友请求。
示例 2：

输入：ages = [16,17,18]
输出：2
解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
示例 3：

输入：ages = [20,30,100,110,120]
输出：3
解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。


提示：

n == ages.length
1 <= n <= 2 * 104
1 <= ages[i] <= 120"""
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        res = left = right = 0
        for i in range(n):
            x, y = 0.5 * ages[i] + 7, ages[i]
            while left < n and ages[left] <= x:
                left += 1
            while right < n and ages[right] <= y:
                right += 1
            res += max(right - left - 1, 0)
        return res




s = Solution()
s.numFriendRequests(ages = [101,1,10,7,15,36,9,3,112,65])
