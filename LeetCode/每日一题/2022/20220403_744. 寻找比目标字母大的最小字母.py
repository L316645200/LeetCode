#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220403_744. 寻找比目标字母大的最小字母.py
# @Author: Lin
# @Date  : 2022/4/6 10:02
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
# 在比较时，字母是依序循环出现的。举个例子：
# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
# 示例 1：
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
# 示例 2:
# 输入: letters = ["c","f","j"], target = "c"
# 输出: "f"
# 示例 3:
# 输入: letters = ["c","f","j"], target = "d"
# 输出: "f"
# 提示：
#
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if letters[right] <= target:
            return letters[0]
        while left <= right:
            mid = (left + right) // 2

            if letters[mid] == target and letters[mid+1] > target:
                return letters[mid+1]
            elif letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]

s = Solution()
res = s.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], 'e')
print(res)