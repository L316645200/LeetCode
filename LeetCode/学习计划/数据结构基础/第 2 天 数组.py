#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 2 天 数组.py
# @Author: Lin
# @Date  : 2022/1/21 19:50

# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 示例 1：
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 示例 3：
# 输入：nums = [0]
# 输出：[0]
# 示例 4：
# 输入：nums = [1]
# 输出：[1]
# 提示：
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
# 进阶：
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, i = len(nums), 0
        left, right = 0, n - 1
        while i <= right and left <= right:

            while left <= right and nums[left] == 0:
                left += 1
                i = min(i+1, left)
            while left <= right and nums[right] == 2:
                right -= 1

            if left > right or i > right:
                break
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                if nums[i] == 0:
                    nums[left], nums[i] = nums[i], nums[left]

                right -= 1
            i += 1
        print(nums)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, 0
        for i in range(n):
            if nums[i] == 1:
                nums[right], nums[i] = nums[i], nums[right]
                right += 1
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                if nums[i] == 1:
                    nums[right], nums[i] = nums[i], nums[right]
                left += 1
                right += 1

            print(left, right, nums)



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, i = len(nums), 0
        left, right = 0, n - 1
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1
        print(nums)

s = Solution()
s.sortColors(nums = [2,0,2,1,1,0,1,2,1,2,1,0,0,0,2,2,2,1,1,0])
# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
# 提示：
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l = len(intervals)
        arr = []
        for i in range(l-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
            else:
               arr.append(intervals[i])
        arr.append(intervals[l-1])
        return arr


s = Solution()
s.merge([[1,3],[2,6],[8,10],[15,18]])


# 706. 设计哈希映射
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
# 示例：
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
# 提示：
# 0 <= key, value <= 106
# 最多调用 104 次 put、get 和 remove 方法


class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for k in self.hashmap[hashkey ]:
            if k[0] == key:
                k[1] = value
                return
        self.hashmap[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for k in self.hashmap[hashkey]:
            if k[0] == key:
                return k[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, k in enumerate(self.hashmap[hashkey]):
            if k[0] == key:
                self.hashmap[hashkey].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)































