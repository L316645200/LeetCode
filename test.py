#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Lin
# @Date  : 2021/7/27 10:23


import bisect
from math import gcd
from typing import List


def bisect_left():
    a = [1, 4, 6, 8, 12, 15, 20]
    i = bisect.bisect_left(a, 21)
    print(i)
    print(a)


def bins():
    print(bin(111))


# 2.3 选择排序

nums = [6,1,4,8,0,10,9,7,2,3,5]


def select_sort(nums):
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1, l):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        arr = [heaters[0]-houses[0]]
        l = len(heaters)
        for i in range(1, l):
            arr.append((heaters[i] - heaters[i-1])//2)
        arr.append(houses[-1] - heaters[-1])
        print(arr)
        print(max(arr))
        return max(arr)




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def hastack(arr, index):
            if index == n:
                res.append(arr[:])
                return
            for i in range(index, n):
                print(i, index, arr)
                arr[i], arr[index] = arr[index], arr[i]

                hastack(arr, index+1)
                arr[index], arr[i] = arr[i], arr[index]
        res = []
        hastack(nums, 0)

        return res

class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            t = 0
            for i in str(num):
                t += int(i)
            num = t
        return num
s = Solution()
s.addDigits(10)