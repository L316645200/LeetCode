#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：12、贪心算法.py
# @Author  ：Lin
# @Date    ：2024/8/23 10:03


"""
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit


# s = Solution()
# s.maxProfit([7,1,5,3,6,4])

"""55. 跳跃游戏
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
提示：
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_idx = 0
        for i in range(len(nums)):
            if cur_idx < i:
                return False
            cur_idx = max(cur_idx, i + nums[i])
        return True

# s = Solution()
# s.canJump(nums = [3,2,1,0,4])

"""45. 跳跃游戏 II
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:
输入: nums = [2,3,0,1,4]
输出: 2
提示:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [i for i in range(n)]
        cur_idx = 0
        for i in range(n):
            # 当当前跳跃次数小于i时
            while dp[cur_idx] < i:
                cur_idx += 1
            dp[cur_idx+1] = max(dp[cur_idx+1], i + nums[i])
            if dp[cur_idx+1] >= n - 1:
                return cur_idx + 1


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n-1):
            # 当前跳跃次数的最远距离
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    step += 1
                    end = max_pos
        return step


# s = Solution()
# s.jump(nums = [2,3,1,1,4])

# r = s.jump(nums = [3,1,3,1,1,4])

"""763. 划分字母区间
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。
示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
示例 2：
输入：s = "eccbbbbdec"
输出：[10]
提示：
1 <= s.length <= 500
s 仅由小写英文字母组成
"""

# 由题意， 将同字母最后出现的位置记录在字典中
# 遍历字母，将当前字母最后出现的位置作为当前字母区间的最后位置，遍历这个区间，并更新最后位置，
# 直到当前位置为最后位置，即可得出当前区间的长度，如此循环得出所有区间

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        max_pos, end = 0, 0
        res = []
        # 当前字母的相同字母最后出现位置
        mp = {w: i for i, w in enumerate(s)}
        for i, w in enumerate(s):
            #
            max_pos = max(max_pos, mp[w])
            if max_pos == i:
                res.append(max_pos - end + 1)
                max_pos += 1
                end = max_pos
        return res

s = Solution()
s.partitionLabels(s = "ababcbacadefegdehijhklij")














