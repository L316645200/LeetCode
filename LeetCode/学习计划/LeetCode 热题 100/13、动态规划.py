#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：13、动态规划.py
# @Author  ：Lin
# @Date    ：2024/8/27 16:09

"""70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
提示：
1 <= n <= 45
"""
import bisect
import math
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for i in range(3, n+1):
            first, second = second, first + second
        return second

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            dp[i+1] = dp[i] + dp[i-1]
        return dp[-1]

# s = Solution()
# s.climbStairs(4)

"""118. 杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:
输入: numRows = 1
输出: [[1]]
提示:
1 <= numRows <= 30"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            row = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    row.append(res[i-2][j-1] + res[i-2][j])
            res.append(row)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j-1] + res[i-1][j])
            res.append(row)
        return res


# s = Solution()
# s.generate(8)

"""198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        return second


# s = Solution()
# s.rob([2,7,9,3,1])


"""
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
提示：
1 <= n <= 104
"""


class Solution:
    def numSquares(self, n: int) -> int:
        i, nums = 1, []
        # 所有小于n的完全平方数
        while i ** 2 <= n:
            nums.append(i ** 2)
            i += 1
        dp = [n] * (n + 1)
        dp[0] = 0
        #
        for i in range(1, n+1):
            for j in nums:
                if i >= j:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[n]


@cache
def dfs(i, j):
    if j == 0:
        return 0 if i == 0 else math.inf
    if i < j ** 2:
        return dfs(i, j - 1)
    return min(dfs(i - j ** 2, j) + 1, dfs(i, j - 1))

# 递归
class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(n, math.isqrt(n))


# s = Solution()
# s.numSquares(13)


"""322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104"""


# 递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @cache
#         def dfs(i, amount):
#             if i == -1:
#                 return 0 if amount == 0 else math.inf
#             if amount < coins[i]:
#                 return dfs(i-1, amount)
#             return min(dfs(i-1, amount), dfs(i, amount - coins[i]) + 1)
#
#         r = dfs(len(coins)-1, amount)
#         return -1 if r > amount else r

# s = Solution()
# s.coinChange(coins = [1, 2, 5], amount = 11)

# s.coinChange(coins = [2], amount = 3)

"""139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
示例 2：解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
提示：
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        cnt = set(wordDict)
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, n + 1):
                    if s[i: j] in cnt:
                        dp[j] = True
        return dp[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        cnt = set(wordDict)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i: j] in cnt:
                    dp[j] = True
        return dp[n]


# s = Solution()
# s.wordBreak( s = "applepenapple", wordDict = ["apple", "pen"])


"""300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。
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
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for i, num in enumerate(nums):
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                k = bisect.bisect_left(dp, num)
                dp[k] = num
        return len(dp)

# s = Solution()
# s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])

"""152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 
子数组
（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

 

示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 

提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何子数组的乘积都 保证 是一个 32-位 整数
"""

"""动态规划 
我们只要记录前 i 的最小值，和最大值，那么 
dp[i] = max(nums[i] * pre_max, nums[i] * pre_min, nums[i])，
这里 0 不需要单独考虑，因为当相乘不管最大值和最小值，都会置 0
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        pre_max = pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


"""根据符号的个数 [^2]
当负数个数为偶数时候，全部相乘一定最大
当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
当有 0 情况，重置就可以了"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse_nums[i] *= reverse_nums[i-1] or 1
        return max(reverse_nums + nums)


# s = Solution()
# s.maxProduct(nums = [-2,0,-1])
# s.maxProduct(nums = [2,-3, 0, -2,4])

"""416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
提示：
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

# 递归
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, num):
            if i < 0:
                return True if num == 0 else False
            if nums[i] > num:
                return dfs(i-1, num)
            return dfs(i-1, num) or dfs(i-1, num-nums[i])

        total = sum(nums)
        if total % 2 != 0:
            return False
        return dfs(len(nums)-1, total // 2)

# 动态规划
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        total //= 2
        dp = [False] * (total + 1)
        dp[0] = True
        for i in range(n):
            for j in range(total, nums[i] - 1, -1):
                dp[j] |= dp[j-nums[i]]
        return dp[total]

# 动态规划写法优化(复杂度不变)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [True] + [False] * target
        dp[0] = True
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j-num]
        return dp[target]


# s = Solution()
# s.canPartition(nums = [1,5,11,5])


"""32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号
子串
的长度。
示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：
输入：s = ""
输出：0
提示：
0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        deq = []  # 栈
        dp = [False] * len(s)  # 是否是有效括号
        res, cur = 0, 0
        for i, char in enumerate(s):
            # 将下标加入栈
            if char == '(':
                deq.append(i)
            else:
                # 判断是否有效括号
                if deq:
                    j = deq.pop()
                    dp[i], dp[j] = True, True
        # 最长的连续有效括号
        for state in dp:
            if state:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res


"""不需要额外的空间
思路和算法

在此方法中，我们利用两个计数器 left 和 right 。
首先，我们从左到右遍历字符串，对于遇到的每个 ‘(’，我们增加 left 计数器，
对于遇到的每个 ‘)’ ，我们增加 right 计数器。每当 left 计数器与 right 计数器相等时，
我们计算当前有效字符串的长度，并且记录目前为止找到的最长子字符串。
当 right 计数器比 left 计数器大时，我们将 left 和 right 计数器同时变回 0。

这样的做法贪心地考虑了以当前字符下标结尾的有效括号长度，
每次当右括号数量多于左括号数量的时候之前的字符我们都扔掉不再考虑，
重新从下一个字符开始计算，但这样会漏掉一种情况，
就是遍历的时候左括号的数量始终大于右括号的数量，即 (() ，这种时候最长有效括号是求不出来的。

解决的方法也很简单，我们只需要从右往左遍历用类似的方法计算即可，
只是这个时候判断条件反了过来：

当 left 计数器比 right 计数器大时，我们将 left 和 right 计数器同时变回 0
当 left 计数器与 right 计数器相等时，我们计算当前有效字符串的长度，
并且记录目前为止找到的最长子字符串
这样我们就能涵盖所有情况从而求解出答案。
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    res = max(res, right + left)
                elif left < right:
                    left, right = 0, 0
        left, right = 0, 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
                if left == right:
                    res = max(res, right + left)
                elif left > right:
                    left, right = 0, 0
            else:
                right += 1
        return res


# s = Solution()
# s.longestValidParentheses(s = ")()())")








