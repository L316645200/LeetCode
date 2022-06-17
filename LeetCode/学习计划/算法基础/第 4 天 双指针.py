#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天 双指针.py
# @Author: Lin
# @Date  : 2022/6/9 10:59

# 844. 比较含退格的字符串
# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
# 注意：如果对空文本输入退格字符，文本继续为空。
# 示例 1：
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：s 和 t 都会变成 "ac"。
# 示例 2：
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 ""。
# 示例 3：
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 "c"，但 t 仍然是 "b"。
# 提示：
# 1 <= s.length, t.length <= 200
# s 和 t 只含有小写字母以及字符 '#'
# 进阶：
#
# 你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st):
            lis = []
            for i in st:
                if i == "#" and lis:
                    lis.pop()
                elif i != "#":
                    lis.append(i)
            return "".join(lis)
        return build(s) == build(t)

s = Solution()
s.backspaceCompare(s = "ab#c", t = "ad#c")


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True


# 986. 区间列表的交集
# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
# 返回这 两个区间列表的交集 。
# 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
# 示例 1：
# 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 示例 2：
# 输入：firstList = [[1,3],[5,9]], secondList = []
# 输出：[]
# 示例 3：
# 输入：firstList = [], secondList = [[4,8],[10,12]]
# 输出：[]
# 示例 4：
# 输入：firstList = [[1,7]], secondList = [[3,10]]
# 输出：[[3,7]]
# 提示：
#
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1


# 参考题解前
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0
        arr = []
        while left < len(firstList) and right < len(secondList):
            if firstList[left][0] > secondList[right][1]:
                right += 1
            elif firstList[left][1] < secondList[right][0]:
                left += 1
            else:
                arr.append([max(firstList[left][0], secondList[right][0]), min(firstList[left][1], secondList[right][1])])
                if firstList[left][1] > secondList[right][1]:
                    right += 1
                else:
                    left += 1
        return arr


# 参考题解后
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0
        arr = []
        while left < len(firstList) and right < len(secondList):
            lo = max(firstList[left][0], secondList[right][0])
            hi = min(firstList[left][1], secondList[right][1])
            if lo <= hi:
                arr.append([lo, hi])
            if firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left += 1
        return arr


s = Solution()
s.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
s.intervalIntersection(firstList = [[1,3],[5,9]], secondList = [])
s.intervalIntersection(firstList = [[1,7]], secondList = [[3,10]])

# 11. 盛最多水的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
# 示例 1：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2
# 输入：height = [1,1]
# 输出：1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])








