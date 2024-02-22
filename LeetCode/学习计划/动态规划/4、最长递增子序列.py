#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：4、最长递增子序列.py
# @Author  ：Lin
# @Date    ：2023/12/16 16:37

"""300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?"""
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
            else:
                idx = bisect.bisect_left(res, num)
                res[idx] = num
        return len(res)


# s = Solution()
# s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])

"""673. 最长递增子序列的个数
给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
注意 这个数列必须是 严格 递增的。
示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
提示: 
1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""


"""定义 dp[i] 表示以 nums[i]结尾的最长上升子序列的长度，
cnt[i]表示以 nums[i]结尾的最长上升子序列的个数。
设 nums的最长上升子序列的长度为 maxLen，那么答案为所有满足 dp[i]=maxLen的 i所对应的 cnt[i]之和。

"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n

        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]  # 重置计数
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]

        return ans


# s = Solution()
# s.findNumberOfLIS([1,3,5,4,7])


"""646. 最长数对链
给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。
现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。
找出并返回能够形成的 最长数对链的长度 。
你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
示例 1：
输入：pairs = [[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4] 。
示例 2：
输入：pairs = [[1,2],[7,8],[4,5]]
输出：3
解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。
提示：
n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000"""
# 贪心
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])

        deq = [pairs[0]]

        for pair in pairs[1:]:
            if pair[0] > deq[-1][1]:
                deq.append(pair)
            elif pair[1] < deq[-1][1]:
                deq.pop()
                deq.append(pair)
        return len(deq)

# 贪心:原地修改
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = 0
        for i in range(1, len(pairs)):
            if pairs[i][0] > pairs[n][1]:
                pairs[n+1] = pairs[i]
                n += 1
            elif pairs[i][1] < pairs[n][1]:
                pairs[n] = pairs[i]
        return n + 1

# 动态规划
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans


# s = Solution()
# s.findLongestChain(pairs = [[1,2],[9,11],[3,5],[7,10],[6,7]])
# s.findLongestChain(pairs = [[1,2], [2,3], [3,4]])


"""1218.最长定差子序列
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

 

示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
 

提示：

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104"""


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for v in arr:
            c = max(dp.get(v, 0), dp.get(v - difference, 0) + 1)
            dp[v] = c
            ans = max(ans, c)
        return ans


# s = Solution()
# s.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        dic = {}
        for i in arr:
            dic[i] = dic.get(i-difference, 0) + 1
            ans = max(ans, dic[i])

        return ans

from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())


"""1027.最长等差数列
给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
示例 1：
输入：nums = [3,6,9,12]
输出：4
解释： 
整个数组是公差为 3 的等差数列。
示例 2：
输入：nums = [9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。
示例 3：
输入：nums = [20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
提示：
2 <= nums.length <= 1000
0 <= nums[i] <= 500"""


# class Solution:
#     def longestArithSeqLength(self, nums: List[int]) -> int:
#         max_num, min_num = max(nums), min(nums)
#         ans = 1
#         for d in range(-max_num, max_num+1):
#             f = {}
#             for num in nums:
#                 if num - d in f:
#                     f[num] = f[num-d] + 1
#                     ans = max(ans, f[num])
#                 else:
#                     f[num] = 1
#         return ans


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        ans = 1
        diff = max_num - min_num
        for d in range(-diff, diff+1):
            f = {}
            for num in nums:
                if num - d in f:
                    f[num] = f[num-d] + 1
                    ans = max(ans, f[num])
                else:
                    f[num] = 1
        return ans




s = Solution()
s.longestArithSeqLength(nums = [20,1,15,3,10,5,8])















































































































































