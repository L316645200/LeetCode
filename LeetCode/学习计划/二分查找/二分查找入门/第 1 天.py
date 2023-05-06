#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天.py
# @Author: Lin
# @Date  : 2023/3/10 18:17

# 704. 二分查找
#
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#  
#
# 提示：
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
from bisect import bisect_left
from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1



# 374. 猜数字大小
# 猜数字游戏的规则如下：
#
# 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
#
# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。
#
#  
#
# 示例 1：
#
# 输入：n = 10, pick = 6
# 输出：6
# 示例 2：
#
# 输入：n = 1, pick = 1
# 输出：1
# 示例 3：
#
# 输入：n = 2, pick = 1
# 输出：1
# 示例 4：
#
# 输入：n = 2, pick = 2
# 输出：2
#  
#
# 提示：
#
# 1 <= n <= 231 - 1
# 1 <= pick <= n



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                left = mid + 1
            else:
                right = mid - 1