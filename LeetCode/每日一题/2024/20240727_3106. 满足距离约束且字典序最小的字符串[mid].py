#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240727_3106. 满足距离约束且字典序最小的字符串[mid].py
# @Author  ：Lin
# @Date    ：2024/7/27 9:59


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        i, arr = 0, list(s)
        for i in range(len(arr)):
            diff = ord(arr[i]) - ord('a')
            diff = min(26-diff, diff)
            if k >= diff:
                arr[i] = 'a'
                k -= diff
            else:
                arr[i] = chr(ord(arr[i]) - k)
                break
        return ''.join(arr)



s = Solution()
s.getSmallestString(s = "xaxcd", k = 4)