#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 5 天.py
# @Author: Lin
# @Date  : 2023/5/20 17:51

# 287. 寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
# 示例 1：
# 输入：nums = [1,3,4,2,2]
# 输出：2
# 示例 2：
# 输入：nums = [3,1,3,4,2]
# 输出：3
# 提示：
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
# 进阶：
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
import bisect
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res


"""先假设一些量：
起点到环的入口长度为 m，环的周长为 c，在 fast 和 slow 相遇时 slow 走了 n 步。
则 fast 走了 2n 步，fast 比 slow 多走了 n 步，
而这 n 步全用在了在环里循环（n%c==0）。
当 fast 和 last 相遇之后，我们设置第三个指针 finder，
它从起点开始和 slow(在 fast 和 slow 相遇处)同步前进，
当 finder 和 slow 相遇时，就是在环的入口处相遇，也就是重复的那个数字相遇。
为什么 finder 和 slow 相遇在入口
fast 和 slow 相遇时，slow 在环中行进的距离是 n-m，其中 n%c==0。
这时我们再让 slow 前进 m 步——也就是在环中走了 n 步了。
而 n%c==0 即 slow 在环里面走的距离是环的周长的整数倍，
就回到了环的入口了，而入口就是重复的数字。
我们不知道起点到入口的长度 m，所以弄个 finder 和 slow 一起走，他们必定会在入口处相遇。

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                break
        return finder


s = Solution()
s.findDuplicate(nums = [1,2,3,4,1,6,7,8,9,5])


# 1283. 使结果不超过阈值的最小除数
# 给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
# 请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
# 每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
# 题目保证一定有解。
# 示例 1：
# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
# 示例 2：
# 输入：nums = [2,3,5,7,11], threshold = 11
# 输出：3
# 示例 3：
# 输入：nums = [19], threshold = 5
# 输出：4
# 提示：
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            t = sum([(num - 1) // mid + 1 for num in nums])
            if t <= threshold:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        return res

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        return bisect.bisect_left(range(max(nums) + 1), -threshold, 1, key=lambda x: -sum([(num - 1) // x + 1 for num in nums]))


s = Solution()
s.smallestDivisor(nums = [1,2,5,9], threshold = 6)

s.smallestDivisor(nums = [2,3,5,7,11], threshold = 11)

print(list(range(1, 10)), )