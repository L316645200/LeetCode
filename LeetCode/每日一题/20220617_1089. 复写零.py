#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220617_1089. 复写零.py
# @Author: Lin
# @Date  : 2022/6/17 10:43

# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
# 注意：请不要在超过该数组长度的位置写入元素。
# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
#
# 示例 1：
# 输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
# 示例 2：
# 输入：[1,2,3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,2,3]
# 提示：
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
from typing import List
from collections import deque

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans = []
        count, l = 0, len(arr)
        for i in arr:
            if i != 0:
                ans.append(i)
                count += 1
            else:
                ans.extend([0, 0])
                count += 2
            if count == l:
                break
            elif count > l:
                ans.pop()
                break
        arr = ans
        print(arr)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        top = 0
        i = -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        print(i, top)
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            i -= 1

s = Solution()
s.duplicateZeros([1,0,2,3,0,4,5,0])