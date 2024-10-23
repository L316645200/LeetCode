#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：15、技巧.py
# @Author  ：Lin
# @Date    ：2024/9/3 17:45

"""
136. 只出现一次的数字
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
示例 1 ：
输入：nums = [2,2,1]
输出：1
示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4
示例 3 ：
输入：nums = [1]
输出：1
提示：
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
除了某个元素只出现一次以外，其余每个元素均出现两次。
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


# s = Solution()
# r = s.singleNumber(nums = [4,1,2,1,2])
# print(r)

"""169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：nums = [3,2,3]
输出：3
示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, cnt = -1, 0
        for num in nums:
            if cnt == 0:
                cur = num
                cnt += 1
            elif cur == num:
                cnt += 1
            else:
                cnt -= 1
        return cur

# s = Solution()
# s.majorityElement(nums = [2,2,1,1,1,2,2])

"""
75. 颜色分类
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。
示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
提示：
n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
进阶：
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, n - 1
        i = 0
        while i <= right:
            if nums[i] == 2:
                while right > i and nums[right] == 2:
                    right -= 1
                nums[i], nums[right] = nums[right], nums[i]
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
            print(nums)

# s = Solution()
# s.sortColors(nums = [1,2,0])
# s.sortColors(nums = [0,2])


"""
31. 下一个排列
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
必须 原地 修改，只允许使用额外常数空间。
示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        max_idx = n - 1  # 最大值的下标
        mark = 0

        for i in range(n - 2, -1, -1):
            # 当前遍历值大于等于最大值时，更换最大值下标
            if nums[i] >= nums[max_idx]:
                max_idx = i
            else:
                # 此时说明从 i - n-1 中必有下一个排列
                # 把当前值和大于当前值的最小值互换
                for j in range(i + 1, n):
                    if nums[i] < nums[j] <= nums[max_idx]:
                        max_idx = j
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                # 剩余元素逆序即可
                left, right = i + 1, n - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                mark = 1
                break
        if not mark:
            left, right = 0, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
# s = Solution()
# s.nextPermutation(nums = [2,3,1,3,3])


"""287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
示例 1：
输入：nums = [1,3,4,2,2]
输出：2
示例 2：
输入：nums = [3,1,3,4,2]
输出：3
示例 3 :
输入：nums = [3,3,3,3,3]
输出：3
提示：
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
"""



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            cnt = 0

            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

s = Solution()
# s.findDuplicate(nums = [3,1,3,4,2])


# s.findDuplicate([1,3,4,2,2])

s.findDuplicate([1,4,4,2,4])












