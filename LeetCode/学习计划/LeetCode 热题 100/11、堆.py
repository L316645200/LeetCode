#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：11、堆.py
# @Author  ：Lin
# @Date    ：2024/8/10 17:49

"""215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
提示：
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import random
from collections import Counter
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, m):
            left, right, mid = [], [], []
            q = random.randint(0, len(arr) - 1)
            for i in range(len(arr)):
                if arr[i] > arr[q]:
                    right.append(arr[i])
                elif arr[i] < arr[q]:
                    left.append(arr[i])
                else:
                    mid.append(arr[i])

            if len(right) >= m:
                return quick_select(right, m)
            elif len(right) + len(mid) >= m:
                return arr[q]
            else:
                return quick_select(left, m - len(right) - len(mid))

        return quick_select(nums, k)


# s = Solution()
# r = s.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)
# print(r)


"""347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = [[k, v] for k, v in Counter(nums).items()]
        cnt.sort(key=lambda x: x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        element = list(cnt.keys())
        def quick_select(arr, m, ans):
            left, right, mid = [], [], []
            q = random.randint(0, len(arr) - 1)
            for i in range(len(arr)):
                if cnt[arr[i]] > cnt[arr[q]]:
                    right.append(arr[i])
                elif cnt[arr[i]] < cnt[arr[q]]:
                    left.append(arr[i])
                else:
                    mid.append(arr[i])

            if len(right) >= m:
                return quick_select(right, m, ans)
            elif len(right) + len(mid) == m:
                return right + mid + ans
            else:
                return quick_select(left, m - len(right) - len(mid), right + mid + ans)

        return quick_select(element, k, [])

# s = Solution()
# s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)


"""295. 数据流的中位数
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:
MedianFinder() 初始化 MedianFinder 对象。
void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
示例 1：
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]
解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:
-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian
"""

import heapq


"""方法一：优先队列
思路和算法

我们用两个优先队列 queMax 和 queMin 分别记录大于中位数的数和小于等于中位数的数。
当累计添加的数的数量为奇数时，queMin 中的数的数量比 queMax 多一个，此时中位数为 queMin 的队头。
当累计添加的数的数量为偶数时，两个优先队列中的数的数量相同，此时中位数为它们的队头的平均值。

当我们尝试添加一个数 num 到数据结构中，我们需要分情况讨论：

num≤max{queMin}

此时 num 小于等于中位数，我们需要将该数添加到 queMin 中。
新的中位数将小于等于原来的中位数，因此我们可能需要将 queMin 中最大的数移动到 queMax 中。

num>max{queMin}
此时 num 大于中位数，我们需要将该数添加到 queMin 中。
新的中位数将大于等于原来的中位数，因此我们可能需要将 queMax 中最小的数移动到 queMin 中。

特别地，当累计添加的数的数量为 0 时，我们将 num 添加到 queMin 中。
"""
# class MedianFinder:
#
#     def __init__(self):
#         self.queMin = []
#         self.queMax = []
#
#     def addNum(self, num: int) -> None:
#         que_min = self.queMin
#         que_max = self.queMax
#
#         if not que_min or num < - que_min[0]:
#             heapq.heappush(que_min, -num)
#             if len(que_min) > len(que_max) + 1:
#                 k = heapq.heappop(que_min)
#                 heapq.heappush(que_max, -k)
#         else:
#             heapq.heappush(que_max, num)
#             if len(que_max) > len(que_min):
#                 k = heapq.heappop(que_max)
#                 heapq.heappush(que_min, -k)
#
#     def findMedian(self) -> float:
#         que_min = self.queMin
#         que_max = self.queMax
#
#         if len(que_min) > len(que_max):
#             return -que_min[0]
#         return (-que_min[0] + que_max[0]) / 2

class MedianFinder:

    def __init__(self):
        self.que_max = []
        self.que_min = []

    def addNum(self, num: int) -> None:
        que_max_ = self.que_max
        que_min_ = self.que_min

        if not que_min_ or num <= -que_min_[0]:
            heapq.heappush(que_min_, -num)
            if len(que_min_) > len(que_max_) + 1:
                heapq.heappush(que_max_, -heapq.heappop(que_min_))
        else:
            heapq.heappush(que_max_, num)
            if len(que_max_) > len(que_min_):
                heapq.heappush(que_min_, -heapq.heappop(que_max_))

    def findMedian(self) -> float:
        que_max_ = self.que_max
        que_min_ = self.que_min
        if len(que_min_) > len(que_max_):
            return -que_min_[0]
        return (-que_min_[0] + que_max_[0]) / 2


m = MedianFinder()
m.addNum(6)

m.addNum(10)
m.addNum(2)
m.addNum(6)
m.addNum(5)
m.addNum(0)
m.addNum(6)
m.addNum(3)
s = m.findMedian()
print(s)
m.addNum(1)

s = m.findMedian()
print(s)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


































