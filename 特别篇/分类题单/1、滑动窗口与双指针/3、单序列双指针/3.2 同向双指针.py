#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3.2 同向双指针.py
# @Author  ：Lin
# @Date    ：2024/11/18 16:06

"""两个指针的移动方向相同（都向右，或者都向左）。
2972. 统计移除递增子数组的数目 II 2153
2122. 还原原数组 2159
3323. 通过插入区间最小化连通组（会员题）"""
"""两个指针的移动方向相同（都向右，或者都向左）。
"""
from typing import List

"""581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：
输入：nums = [1,2,3,4]
输出：0
示例 3：
输入：nums = [1]
输出：0
提示：
1 <= nums.length <= 104
-105 <= nums[i] <= 105
进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
"""


# 排序
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        left, right = 0, -1

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                left = i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] != arr[j]:
                right = j
                break
        return right - left + 1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        xmax, right = float('-inf'), -1
        xmin, left = float('inf'), n
        for i in range(n):
            if nums[i] < xmax:
                right = i
            else:
                xmax = nums[i]

            if nums[n-1-i] > xmin:
                left = n-1-i
            else:
                xmin = nums[n-1-i]
        return 0 if right == -1 else right - left + 1


# s = Solution()
# s.findUnsortedSubarray(nums = [2,6,4,8,10,9,15])


"""2972. 统计移除递增子数组的数目 II 2153
给你一个下标从 0 开始的 正 整数数组 nums 。
如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增 ，那么我们称这个子数组为 移除递增 子数组。比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。
请你返回 nums 中 移除递增 子数组的总数目。
注意 ，剩余元素为空的数组也视为是递增的。
子数组 指的是一个数组中一段连续的元素序列。
示例 1：
输入：nums = [1,2,3,4]
输出：10
解释：10 个移除递增子数组分别为：[1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4] 和 [1,2,3,4]。移除任意一个子数组后，剩余元素都是递增的。注意，空数组不是移除递增子数组。
示例 2：
输入：nums = [6,5,7,8]
输出：7
解释：7 个移除递增子数组分别为：[5], [6], [5,7], [6,5], [5,7,8], [6,5,7] 和 [6,5,7,8] 。
nums 中只有这 7 个移除递增子数组。
示例 3：
输入：nums = [8,7,6,6]
输出：3
解释：3 个移除递增子数组分别为：[8,7,6], [7,6,6] 和 [8,7,6,6] 。注意 [8,7] 不是移除递增子数组因为移除 [8,7] 后 nums 变为 [6,6] ，它不是严格递增的。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109"""


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        # 先将左指针从前往后扫，指针停留在最长严格递增的位置left
        while left < n - 1 and nums[left+1] > nums[left]:
            left += 1
        # 如果left==n-1，说明整个数组都严格递增，直接返回 n * (n + 1) // 2
        if left == n - 1:
            return n * (n + 1) // 2
        # 此时有left+2个子数组
        res = left + 2
        while left >= 0:
            # 右指针大于左指针时,res+=left+2,右指针往左移,不满足时左指针左移
            while nums[left] < nums[right] and (right == n - 1 or nums[right] < nums[right+1]):
                print(left, right, res)
                res += left + 2
                right -= 1
            left -= 1
        while right == n - 1 or nums[right] < nums[right+1]:
            right -= 1
            res += left + 2
        print(res)

        return res


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0

        # 先将左指针从前往后扫，指针停留在最长严格递增的位置left
        while left < n - 1 and nums[left+1] > nums[left]:
            left += 1
        # 如果left==n-1，说明整个数组都严格递增，直接返回 n * (n + 1) // 2
        if left == n - 1:
            return n * (n + 1) // 2
        # 此时有left+2个子数组
        res = left + 2

        for right in range(n-1, -1, -1):
            if right < n - 1 and nums[right] >= nums[right+1]:
                break
            while left >= 0 and nums[left] >= nums[right]:
                left -= 1
            res += left + 2
        return res

# s = Solution()
# s.incremovableSubarrayCount(nums = [1,2,10,6])


"""2122. 还原原数组 2159
Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：
对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。
给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。如果出现答案不唯一的情况，返回 任一 有效数组。
注意：生成的测试用例保证存在 至少一个 有效数组 arr 。
示例 1：
输入：nums = [2,10,6,4,8,12]
输出：[3,7,11]
解释：
如果 arr = [3,7,11] 且 k = 1 ，那么 lower = [2,6,10] 且 higher = [4,8,12] 。
组合 lower 和 higher 得到 [2,6,10,4,8,12] ，这是 nums 的一个排列。
另一个有效的数组是 arr = [5,7,9] 且 k = 3 。在这种情况下，lower = [2,4,6] 且 higher = [8,10,12] 。
示例 2：
输入：nums = [1,1,3,3]
输出：[2,2]
解释：
如果 arr = [2,2] 且 k = 1 ，那么 lower = [1,1] 且 higher = [3,3] 。
组合 lower 和 higher 得到 [1,1,3,3] ，这是 nums 的一个排列。
注意，数组不能是 [1,3] ，因为在这种情况下，获得 [1,1,3,3] 唯一可行的方案是 k = 0 。
这种方案是无效的，k 必须是一个正整数。
示例 3：
输入：nums = [5,435]
输出：[220]
解释：
唯一可行的组合是 arr = [220] 且 k = 215 。在这种情况下，lower = [5] 且 higher = [435] 。
提示：
2 * n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 109
生成的测试用例保证存在 至少一个 有效数组 arr
"""


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        print(nums)
        for i in range(1, n):
            # k是正整数
            k = nums[i] - nums[0]
            if k % 2 != 0 or k == 0:
                continue
            k = k // 2

            res = [nums[0] + k]
            vis = [0] * n  # 是否使用过的下标
            vis[i] = 1
            # 双指针
            left, right = 1, i + 1
            # 最多再执行n//2-1 次
            for j in range(n//2 - 1):
                # left未访问过
                while vis[left]:
                    left += 1
                # right未访问过且 nums[left] + 2 * k 不小于nums[right]
                while right < n and (vis[right] or nums[right] - nums[left] != 2 * k):
                    right += 1
                # nums[right] - nums[left] != 2 * k 可以确定剩余元素都无法满足要求
                if right == n:
                    break
                res.append(nums[left] + k)
                vis[left] = vis[right] = 1
            if len(res) == n // 2:
                return res


s = Solution()
r = s.recoverArray(nums =[8,4,5,1,9,8,6,5,6,9,7,3,8,3,6,7,10,11,6,4])
print(r)











































































