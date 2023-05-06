#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 7 天.py
# @Author: Lin
# @Date  : 2023/4/17 17:16

# 167. 两数之和 II - 输入有序数组
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用常量级的额外空间。
# 示例 1：
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 示例 2：
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
# 解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
# 示例 3：
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
# 解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 提示：
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers 按 非递减顺序 排列
# -1000 <= target <= 1000
# 仅存在一个有效答案
#
from typing import List

# 二分
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        for i in range(n):
            tar = target - numbers[i]
            left, right = i + 1, n
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tar:
                    return [i, mid]
                elif numbers[mid] > tar:
                    right = mid - 1
                else:
                    left = mid + 1


s = Solution()
r = s.twoSum(numbers = [2,7,11,15], target = 9)
print(r)


# 双指针
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]

# 1608. 特殊数组的特征值

# 给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。
# 注意： x 不必 是 nums 的中的元素。
# 如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。
# 示例 1：
# 输入：nums = [3,5]
# 输出：2
# 解释：有 2 个元素（3 和 5）大于或等于 2 。
# 示例 2：
# 输入：nums = [0,0]
# 输出：-1
# 解释：没有满足题目要求的特殊数组，故而也不存在特征值 x 。
# 如果 x = 0，应该有 0 个元素 >= x，但实际有 2 个。
# 如果 x = 1，应该有 1 个元素 >= x，但实际有 0 个。
# 如果 x = 2，应该有 2 个元素 >= x，但实际有 0 个。
# x 不能取更大的值，因为 nums 中只有两个元素。
# 示例 3：
# 输入：nums = [0,4,3,0,4]
# 输出：3
# 解释：有 3 个元素大于或等于 3 。
# 示例 4：
# 输入：nums = [3,6,7,7,0]
# 输出：-1
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        x = 0
        for i in range(1, min(nums[n-1]+1, n+1)):
            while nums[x] < i:
                x += 1
            if i == n - x:
                return i
        return -1

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1


if __name__ == '__main__':

    s = Solution()
    s.specialArray([3,5])







s = Solution()
r = s.specialArray(nums = [0,4,3,0,4])






























