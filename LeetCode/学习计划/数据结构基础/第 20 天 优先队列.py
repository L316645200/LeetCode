#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 20 天 优先队列.py
# @Author: Lin
# @Date  : 2022/12/1 17:37

# 215. 数组中的第K个最大元素
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1:
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
# 提示：
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
import random
from collections import Counter
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, i):
            m = random.randint(0, len(arr) - 1)

            left, right, mid = [], [], []
            for num in arr:
                if num > arr[m]:
                    right.append(num)
                elif num < arr[m]:
                    left.append(num)
                else:
                    mid.append(num)
            if len(right) >= i:
                return quick_select(right, i)
            elif len(right) + len(mid) >= i:
                return arr[m]
            else:
                return quick_select(left, i - len(right) - len(mid))

        ans = quick_select(nums, k)
        return ans


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, i):
            index = random.randint(0, len(arr) - 1)
            pivot = arr[index]
            left, right, mid = [], [], []
            for num in arr:
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)
            if len(right) >= i:
                pivot = quick_select(right, i)
            elif len(right) + len(mid) < i:
                pivot = quick_select(left, i - len(right) - len(mid))
            return pivot

        ans = quick_select(nums, k)
        return ans

s = Solution()
r = s.findKthLargest( [3,2,1,5,6,4], k = 2)




# Python Version
def sift_down(arr, start, end):
    # 计算父结点和子结点的下标
    parent = int(start)
    child = int(parent * 2 + 1)
    while child <= end: # 子结点下标在范围内才做比较
        # 先比较两个子结点大小，选择最大的
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # 如果父结点比子结点大，代表调整完毕，直接跳出函数
        if arr[parent] >= arr[child]:
            return
        else: # 否则交换父子内容，子结点再和孙结点比较
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child = int(parent * 2 + 1)

def heap_sort(arr, len):
  # 从最后一个节点的父节点开始 sift down 以完成堆化 (heapify)
    i = (len - 1 - 1) / 2
    while(i >= 0):
        sift_down(arr, i, len - 1)
        i -= 1

  # 先将第一个元素和已经排好的元素前一位做交换，再重新调整（刚调整的元素之前的元素），直到排序完毕
    i = len - 1
    while(i > 0):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i - 1)
        i -= 1

heap_sort([5,2,7,0,9,6,3,4], 8)

# 347. 前 K 个高频元素
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]
# 提示：
# 1 <= nums.length <= 105
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = sorted([[k, v] for k, v in Counter(nums).items()], key=lambda x: x[1], reverse=True)
        return [arr[i][0] for i in range(k)]


s = Solution()
r = s.topKFrequent( nums = [1,1,1,2,2,3], k = 2)
print(r)

