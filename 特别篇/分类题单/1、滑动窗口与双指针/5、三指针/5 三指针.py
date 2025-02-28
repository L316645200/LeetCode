#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：5 三指针.py
# @Author  ：Lin
# @Date    ：2024/12/24 17:56

"""注：部分题目已整理到「§2.3.3 恰好型滑动窗口」中。"""
import bisect
from collections import Counter, defaultdict
from typing import List

"""2367. 等差三元组的数目 做到 O(n)
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 等差三元组 ：
i < j < k ，
nums[j] - nums[i] == diff 且
nums[k] - nums[j] == diff
返回不同 等差三元组 的数目。
示例 1：
输入：nums = [0,1,4,6,7,10], diff = 3
输出：2
解释：
(1, 2, 4) 是等差三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是等差三元组：10 - 7 == 3 且 7 - 4 == 3 。
示例 2：
输入：nums = [4,5,6,7,8,9], diff = 2
输出：2
解释：
(0, 2, 4) 是等差三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是等差三元组：9 - 7 == 2 且 7 - 5 == 2 。
提示：
3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums 严格 递增"""


# 哈希
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        visited = set()
        res = 0
        for num in nums:
            if num - diff in visited and num - 2 * diff in visited:
                res += 1
            visited.add(num)
        return res


# 三指针
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        i, j, k = 0, 1, 2
        res = 0
        n = len(nums)
        while i < n - 2 and j < n - 1 and k < n:
            while j < n - 1 and nums[j] < nums[i] + diff:
                j += 1
            while k < n and nums[k] < nums[j] + diff:
                k += 1
            if j < n - 1 and k < n and nums[j] - nums[i] == nums[k] - nums[j] == diff:
                res += 1
            i += 1
        return res


# s = Solution()
# s.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)

"""2563. 统计公平数对的数目 1721
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。
如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：
0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper
示例 1：
输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
示例 2：
输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。
提示：
1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)  # <= upper-nums[j] 的 nums[i] 的个数
            l = bisect_left(nums, lower - x, 0, j)  # < lower-nums[j] 的 nums[i] 的个数
            ans += r - l
        return ans


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        计算满足 lower <= nums[i] + nums[j] <= upper 的公平数对的数量

        参数:
            nums: 整数列表
            lower: 下限
            upper: 上限

        返回:
            公平数对的数量
        """
        # 将每个元素及其索引组成元组，并按照元素值升序排列
        nums.sort()
        n = len(nums)
        k = j = n - 1
        res = 0
        for i in range(n - 1):
            if i >= j:
                break
            while j > i and nums[i] + nums[j] > upper:
                j -= 1
            while k > i and nums[i] + nums[k] >= lower:
                k -= 1
            res += j - max(i, k)

        return res


# s = Solution()
# s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
# s.countFairPairs(nums = [0,0,0,0,0,0], lower = 0, upper = 0)

"""795. 区间子数组个数 1817
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。
生成的测试用例保证结果符合 32-bit 整数范围。
示例 1：
输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]
示例 2：
输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7
提示：
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= left <= right <= 109
"""


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = i = 0
        n = len(nums)
        while i < n:
            j = i
            k = i - 1
            while j < n:
                if nums[j] > right:
                    break
                elif nums[j] < left:
                    res += (k - i + 1)
                else:
                    k = j
                    res += (j - i + 1)
                j += 1
            i = j + 1
        return res



class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        i0 = i1 = -1
        for i in range(len(nums)):
            if nums[i] > right:
                i0 = i
            if nums[i] >= left:
                i1 = i
            res += i1 - i0
        return res

# s = Solution()
# s.numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3)

# r = s.numSubarrayBoundedMax(nums = [73,55,36,5,55,14,9,7,72,52], left = 32, right = 69)
# r = s.numSubarrayBoundedMax(nums = [16,69,88,85,79,87,37,33,39,34], left = 55, right = 57)


"""2444. 统计定界子数组的数目 2093
给你一个整数数组 nums 和两个整数 minK 以及 maxK 。
nums 的定界子数组是满足下述条件的一个子数组：
子数组中的 最小值 等于 minK 。
子数组中的 最大值 等于 maxK 。
返回定界子数组的数目。
子数组是数组中的一个连续部分。
示例 1：
输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
示例 2：
输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
提示：
2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
"""

# 暴力
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         n = len(nums)
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 arr = [nums[k] for k in range(i, j + 1)]
#                 if min(arr) == minK and max(arr) == maxK:
#                     res += 1
#         return res
# 双指针
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # 初始化指针 j, mini, maxi 为 -1，表示它们尚未找到有效的位置
        j = mini = maxi = -1
        # 初始化结果变量 res 为 0
        res = 0
        # 遍历数组 nums
        for i, num in enumerate(nums):
            # 如果当前元素 num 在 minK 和 maxK 之间
            if minK <= num <= maxK:
                # 如果当前元素等于 minK，更新 mini 为当前索引 i
                if num == minK:
                    mini = i
                # 如果当前元素等于 maxK，更新 maxi 为当前索引 i
                if num == maxK:
                    maxi = i
                # 更新结果 res，增加 min(mini, maxi) - j
                res += min(mini, maxi) - j
            # 如果当前元素 num 不在 minK 和 maxK 之间
            else:
                # 更新指针 j, mini, maxi 为当前索引 i
                j = mini = maxi = i
        return res


# s = Solution()
# s.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5)

"""3347. 执行操作后元素的最高频率 II ~2100
给你一个整数数组 nums 和两个整数 k 和 numOperations 。
你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
选择一个下标 i ，它在之前的操作中 没有 被选择过。
将 nums[i] 增加范围 [-k, k] 中的一个整数。
在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
一个元素 x 的 频率 指的是它在数组中出现的次数。
示例 1：
输入：nums = [1,4,5], k = 1, numOperations = 2
输出：2
解释：
通过以下操作得到最高频率 2 ：
将 nums[1] 增加 0 ，nums 变为 [1, 4, 5] 。
将 nums[2] 增加 -1 ，nums 变为 [1, 4, 4] 。
示例 2：
输入：nums = [5,11,20,20], k = 5, numOperations = 1
输出：2
解释：
通过以下操作得到最高频率 2 ：
将 nums[1] 增加 0 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
0 <= numOperations <= nums.length
"""

# 差分数组
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        res = c = 0
        for x, i in sorted(diff.items()):
            c += i
            res = max(res, min(c, cnt[x] + numOperations))
        return res

# 双指针
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            for x in (num-k, num, num + k):
                left = bisect.bisect_left(nums, x - k)
                right = bisect.bisect_right(nums, x + k)
                res = max(res, min(right - left, cnt[x] + numOperations))
        return res
s = Solution()
# s.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2)


s.maxFrequency(nums = [5,64], k = 42, numOperations = 2)








































