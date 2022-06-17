#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天 二分查找.py
# @Author: Lin
# @Date  : 2022/5/27 10:40

# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
# 提示：
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 是一个非递减数组
# -109 <= target <= 109
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = right = mid
                while left > 0 and nums[left-1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right+1] == target:
                    right += 1
                return [left, right]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        left = search_left(nums, target)
        right = search_right(nums, target)
        return [left, right] if left <= right else [-1, -1]


s = Solution()
s.searchRange([5,7,7,8,8,10], 8)

# 33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# （下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
# 提示：
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[mid]:
                if mid > 0 and nums[left] <= target <= nums[mid-1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid < len(nums) - 1 and nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

s = Solution()
r = s.search([4,5,6,7,0,1,2], 3)


# 74. 搜索二维矩阵
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


# 二分
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            x, y = divmod(mid, n)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right -= 1
        return False
# O(logmn)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right -= 1
            else:
                left += 1
        k = right
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] > target:
                right -= 1
            else:
                left += 1
        return False
# O(logm+logn) = O(logmn)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = 0, len(matrix[0]) - 1
        while m < len(matrix) and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False

# O(m+n)


s = Solution()
# r = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
r = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)

print(r)


def guess(m):
    if m == 6:
        return 0
    elif m > 6:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            r = guess(mid)
            print(left, right, mid, r)
            if r == 0:
                return mid
            elif r == 1:
                right = mid - 1
            else:
                left = mid + 1

s = Solution()
r = s.guessNumber(10)
print(r)































