#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230311_面试题 17.05.  字母与数字.py
# @Author: Lin
# @Date  : 2023/3/11 9:48

# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
# 示例 1:
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
# 示例 2:
# 输入: ["A","A"]
# 输出: []
# 提示：
# array.length <= 100000
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        nums = [0] * n
        for i, v in enumerate(array):
            val = 1 if v.isdigit() else -1
            if i == 0:
                nums[i] = val
            else:
                nums[i] = nums[i-1] + val
        min_dict, max_dict = {}, {}
        for i, v in enumerate(nums):
            if v not in min_dict:
                min_dict[v] = i
            max_dict[v] = i
        a, b = -1, -1
        print(min_dict)
        print(max_dict)
        for k, v in max_dict.items():
            print(v - min_dict[k],b - a, min_dict[k],a, b)

            if v - min_dict[k] > b - a or (v - min_dict[k] == b - a and min_dict[k] < a):
                a = min_dict[k]
                b = v
        print(111,max_dict.get(0) , max_dict.get(0), b - a)
        if max_dict.get(0) and max_dict.get(0) >= b - a-1:
            print(111)
            a = -1
            b = max_dict.get(0)
        print(a,b)
        print(array[a+1: b+1])
        return array[a+1: b+1]


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        nums = [0] * n
        min_dict, max_dict = {}, {}

        for i, v in enumerate(array):
            val = 1 if v.isdigit() else -1
            if i == 0:
                nums[i] = val
            else:
                nums[i] = nums[i-1] + val
            if nums[i] not in min_dict:
                min_dict[nums[i]] = i
            max_dict[nums[i]] = i

        a, b = -1, -1
        for k, v in max_dict.items():
            if v - min_dict[k] > b - a or (v - min_dict[k] == b - a and min_dict[k] < a):
                a = min_dict[k]
                b = v
        if max_dict.get(0) and max_dict.get(0) >= b - a-1:
            a = -1
            b = max_dict.get(0)
        return array[a+1: b+1]

s = Solution()
st = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
s.findLongestSubarray(["A","1"]
)

# s.findLongestSubarray(st)