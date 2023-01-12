#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221202_1769. 移动所有球到每个盒子所需的最小操作数.py
# @Author: Lin
# @Date  : 2022/12/2 9:52

# 有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes ，其中 boxes[i] 的值为 '0' 表示第 i 个盒子是 空 的，而 boxes[i] 的值为 '1' 表示盒子里有 一个 小球。
# 在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子相邻需满足 abs(i - j) == 1 。注意，操作执行后，某些盒子中可能会存在不止一个小球。
# 返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。
# 每个 answer[i] 都需要根据盒子的 初始状态 进行计算。
# 示例 1：
# 输入：boxes = "110"
# 输出：[1,1,3]
# 解释：每个盒子对应的最小操作数如下：
# 1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
# 2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
# 3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。
# 示例 2：
# 输入：boxes = "001011"
# 输出：[11,8,5,4,3,4]
# 提示：
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] 为 '0' 或 '1'
from functools import reduce
from typing import List

# 暴力
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        arr = [0] * n
        for i in range(n):
            op = 0
            for j in range(n):
                op += abs(i-j) * int(boxes[j])
            arr[i] = op
        return arr


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left, right = [0] * n, [0] * n
        num1, num2 = 0, 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                num1 += 1
            left[i] = left[i-1] + num1
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                num2 += 1
            right[i] = right[i+1] + num2
        return list(map(lambda x, y: x + y, left, right))
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left, right, operations = int(boxes[0]), 0, 0
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                right += 1
                operations += i
        res = [operations]
        for i in range(1, len(boxes)):
            operations += left - right
            if boxes[i] == '1':
                left += 1
                right -= 1
            res.append(operations)
        return res

s = Solution()
s.minOperations(boxes = "001011")