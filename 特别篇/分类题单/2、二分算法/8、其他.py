#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/29 20:16
# @Author  : Lin
# @File    : 8、其他.py

"""69. x 的平方根 二分求最大的 m，满足 m² ≤x（也可以二分求最小的满足 m² >x 的 m，减一得到答案）
提示：
0 <= x <= 231 - 1"""
import bisect
import datetime
import math
import time
from typing import List, Optional


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (right - left ) // 2 + left
            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        return left

# s = Solution()
# r = s.mySqrt(10)
# print(r)
"""74. 搜索二维矩阵
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        i = j = -1
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid][0] <= target:
                i = mid
                left = mid + 1
            else:
                right = mid - 1
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[i][mid] <= target:
                j = mid
                left = mid + 1
            else:
                right = mid - 1
        return matrix[i][j] == target
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


# s = Solution()
# s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
"""240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
提示：
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

"""2476. 二叉搜索树最近节点查询
给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。
请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：
mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
返回数组 answer 。
示例 1 ：
输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
输出：[[2,2],[4,6],[15,-1]]
解释：按下面的描述找出并返回查询的答案：
- 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
- 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
- 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
示例 2 ：
输入：root = [4,null,9], queries = [3]
输出：[[-1,4]]
解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。
提示：
树中节点的数目在范围 [2, 105] 内
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(nums):
    def level(index: int):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(index * 2 + 1)
        root.right = level(index * 2 + 2)
        return root
    return level(0)

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans = []
        def search_left(root: TreeNode, val=-1):
            while root is not None:
                if root.val > q:
                    root = root.left
                else:
                    val = root.val
                    root = root.right
            return val

        def search_right(root: TreeNode, val=-1):
            while root is not None:
                if root.val < q:
                    root = root.right
                else:
                    val = root.val
                    root = root.left
            return val
        for q in queries:
            ans.append([search_left(root), search_right(root)])
        return ans

# nums = [6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]
# root = create_tree(nums)
#
# print(root.left.right.val)
#
# s = Solution()
# s.closestNodes(root=root, queries = [2,5,16])
#
"""278. 第一个错误的版本
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
示例 1：
输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
示例 2：
输入：n = 1, bad = 1
输出：1
提示：
1 <= bad <= n <= 231 - 1
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
"""374. 猜数字大小
"""
"""162. 寻找峰值
峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。
你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
示例 1：
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
提示：
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return n - 1
        left, right = 1, n - 2
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

"""1901. 寻找峰值 II
一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。
给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 mat[i][j] 并 返回其位置 [i,j] 。
你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。
要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法
示例 1:
输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3 和 4 都是峰值，所以[1,0]和[0,1]都是可接受的答案。
示例 2:
输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30 和 32 都是峰值，所以[1,1]和[2,2]都是可接受的答案。
提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
任意两个相邻元素均不相等.
"""
#
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # 开区间
        left, right = -1, m-1
        while left + 1 < right:
            mid = (left + right) // 2
            # 二分当前行的最大值
            val = max(mat[mid])
            # 当前行的最大值如果小于下一行同下标的值时，下半部分必定有峰值，反之亦然
            if val < mat[mid+1][mat[mid].index(val)]:
                left = mid
            else:
                right = mid
        return [right, mat[right].index(max(mat[right]))]
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, m-1
        while left < right:
            mid = (left + right) // 2
            val = max(mat[mid])
            if val < mat[mid+1][mat[mid].index(val)]:
                left = mid + 1
            else:
                right = mid
        return [right, mat[right].index(max(mat[right]))]


# s = Solution()
# s.findPeakGrid(mat = [[10,20,15],[21,30,14],[7,16,32]])
"""852. 山脉数组的峰顶索引
给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
返回峰值元素的下标。
你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。
示例 1：
输入：arr = [0,1,0]
输出：1
示例 2：
输入：arr = [0,2,1,0]
输出：1
示例 3：
输入：arr = [0,10,5,2]
输出：1
提示：
3 <= arr.length <= 105
0 <= arr[i] <= 106
题目数据 保证 arr 是一个山脉数组"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
        return right
"""1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）
你可以将一个数组 arr 称为 山脉数组 当且仅当：
arr.length >= 3
存在一些 0 < i < arr.length - 1 的 i 使得：
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给定一个山脉数组 mountainArr ，返回 最小 的 index 使得 mountainArr.get(index) == target。如果不存在这样的 index，返回 -1 。
你无法直接访问山脉数组。你只能使用 MountainArray 接口来访问数组：
MountainArray.get(k) 返回数组中下标为 k 的元素（从 0 开始）。
MountainArray.length() 返回数组的长度。
调用 MountainArray.get 超过 100 次的提交会被判定为错误答案。此外，任何试图绕过在线评测的解决方案都将导致取消资格。
示例 1：
输入：mountainArr = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：
输入：mountainArr = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
提示：
3 <= mountainArr.length() <= 104
0 <= target <= 109
0 <= mountainArr.get(index) <= 109
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#        ...
#    def length(self) -> int:
#        ...


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mount = mountainArr
        # 先找出峰顶元素下标
        n = mount.length()
        left, right = 1, n - 2
        while left <= right:
            mid = (left + right) // 2
            if mount.get(mid) > mount.get(mid - 1):
                left = mid + 1
            else:
                right = mid - 1

        idx = right
        # 找出开始位置到峰顶是否存在目标元素
        left, right = 0, idx
        while left <= right:
            mid = (left + right) // 2
            val = mount.get(mid)
            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        # 找出峰顶到结束为止是否存在目标元素
        left, right = idx, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mount.get(mid)
            if val == target:
                return mid
            elif val > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1




class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary_search(mountain, target, l, r, k):
            left, right = l, r
            target = target * k
            while left <= right:
                mid = (left + right) // 2
                val = mountain.get(mid) * k
                if val == target:
                    return mid
                elif val > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        mountain = mountainArr
        # 先找出峰顶元素下标
        n = mountain.length()
        left, right = 1, n - 2
        while left <= right:
            mid = (left + right) // 2
            if mountain.get(mid) > mountain.get(mid - 1):
                left = mid + 1
            else:
                right = mid - 1

        idx = binary_search(mountain, target, 0, right, 1)
        if idx != -1:
            return idx
        idx = binary_search(mountain, target, right, n - 1, -1)
        return idx

"""153. 寻找旋转排序数组中的最小值
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
示例 1：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
示例 2：
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
示例 3：
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]

# s = Solution()
# s.findMin(nums = [4,5,6,7,0,1,2])
# s.findMin(nums = [2,1])
"""154. 寻找旋转排序数组中的最小值 II  1827
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须尽可能减少整个过程的操作步骤。
示例 1：
输入：nums = [1,3,5]
输出：1
示例 2：
输入：nums = [2,2,2,0,1]
输出：0
提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
进阶：这道题与 寻找旋转排序数组中的最小值 类似，但 nums 可能包含重复元素。允许重复会影响算法的时间复杂度吗？会如何影响，为什么？"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]

"""33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：
输入：nums = [1], target = 0
输出：-1
提示：
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 先寻找旋转排序数组中的最小值的下标
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        # 如果数组最后一个值小于目标值，取前半段，反之取后半段
        if nums[-1] < target:
            left, right = 0, left - 1
        else:
            left, right = left, n - 1
        # 在半段有序数组内二分找目标值
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def check(x):
            if x > nums[n-1]:
                return target > nums[n-1] and x >= target
            return target > nums[n-1] or target < x

        # 先寻找旋转排序数组中的最小值的下标
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            x = nums[mid]
            if x == target:
                return mid
            elif check(x):
                right = mid - 1
            else:
                left = mid + 1
        return -1



# s = Solution()
# s.search(nums = [4,5,6,7,0,1,2], target = 0)
# left = 0
# nums = [0,0,1,1,1,2,2,3,3,4]
# for right in range(len(nums)):
#     if nums[right] > nums[left]:
#         nums[left+1], nums[right] = nums[right], nums[left+1]
#         left += 1
# print(nums)
"""81. 搜索旋转排序数组 II
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
你必须尽可能减少整个操作步骤。
示例 1：
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：
输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
提示：
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104
进阶：
此题与 搜索旋转排序数组 相似，但本题中的 nums  可能包含 重复 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
 """


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        def check(x):
            if x > nums[right]:
                return target > nums[right] and target <= x
            return target > nums[right] or target < x

        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            x = nums[mid]
            if x == target:
                return True
            elif nums[right] == x:
                right -= 1
            elif check(x):
                right = mid - 1
            else:
                left = mid + 1
        return False
# s = Solution()
# s.search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2)
"""1539. 第 k 个缺失的正整数
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
请你找到这个数组里第 k 个缺失的正整数。
示例 1：
输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：
输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
提示：
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
进阶：
你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # n = len(arr)
        # if arr[n-1] - n < k:
        #     return k + n
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - 1 - mid < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
# s = Solution()
# s.findKthPositive(arr = [2,3,4,7,11], k = 5)

# r = s.findKthPositive(arr = [4,5,6,7], k = 2)
# print(r)


"""540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
提示:
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
# [1,1,2,3,3,4,4,8,8]

"""题目有两个已知条件：
数组是有序的。
除了一个数出现一次外，其余每个数都出现两次。
第二个条件意味着，数组的长度一定是奇数。
第一个条件意味着，出现两次的数，必然相邻，不可能出现 1,2,1 这样的顺序。
这也意味着，只出现一次的那个数，一定位于偶数下标上。
这启发我们去检查偶数下标 2k。
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if mid > 0 and nums[mid] == nums[mid - 1]:
                idx = mid - 1
            elif mid < n - 1 and nums[mid] == nums[mid + 1]:
                idx = mid
            else:
                return nums[mid]

            if idx % 2:
                right = mid - 1
            else:
                left = mid + 1

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n // 2
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid*2] != nums[mid*2+1]:
                right = mid
            else:
                left = mid + 1
        return nums[right * 2]
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = -1, len(nums) // 2
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid * 2] != nums[mid * 2 + 1]:
                right = mid
            else:
                left = mid
        return nums[right * 2]

s = Solution()
s.singleNonDuplicate(nums = [3,3,7,7,10,11,11])
"""4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

# 双指针
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # num1始终是长度大的
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        # (m + n + 1) // 2 个数字是无用的
        i, j = (m + n + 1) // 2, 0
        nums1 = [-math.inf] + nums1 + [math.inf]
        nums2 = [-math.inf] + nums2 + [math.inf]
        while nums1[i] > nums2[j+1]:
            i -= 1
            j += 1
        max1 = max(nums1[i], nums2[j])
        min2 = min(nums1[i+1], nums2[j+1])
        return max1 if (m + n) % 2 else (max1 + min2) / 2

# 二分
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        k = (m + n + 1) // 2
        left, right = 0, n + 1
        nums1 = [-math.inf] + nums1 + [math.inf]
        nums2 = [-math.inf] + nums2 + [math.inf]
        while left + 1 < right:
            i = (left + right) // 2
            j = k - i
            if nums1[j+1] >= nums2[i]:
                left = i
            else:
                right = i
        j = left
        i = k - j
        max1 = max(nums1[i], nums2[j])
        min2 = min(nums1[i+1], nums2[j+1])
        return max1 if (m + n) % 2 else (max1 + min2) / 2

s=  Solution()
# s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])

s.findMedianSortedArrays(nums1 = [], nums2 = [1,2,3,4])
#































































































