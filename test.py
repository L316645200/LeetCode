#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Lin
# @Date  : 2021/7/27 10:23


import bisect
import heapq
from collections import Counter
from math import gcd
from typing import List


def bisect_left():
    a = [1, 4, 6, 8, 12, 15, 20]
    i = bisect.bisect_left(a, 21)
    print(i)
    print(a)


def bins():
    print(bin(111))


# 2.3 选择排序

nums = [6,1,4,8,0,10,9,7,2,3,5]


def select_sort(nums):
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1, l):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        arr = [heaters[0]-houses[0]]
        l = len(heaters)
        for i in range(1, l):
            arr.append((heaters[i] - heaters[i-1])//2)
        arr.append(houses[-1] - heaters[-1])
        print(arr)
        print(max(arr))
        return max(arr)




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def hastack(arr, index):
            if index == n:
                res.append(arr[:])
                return
            for i in range(index, n):
                print(i, index, arr)
                arr[i], arr[index] = arr[index], arr[i]

                hastack(arr, index+1)
                arr[index], arr[i] = arr[i], arr[index]
        res = []
        hastack(nums, 0)

        return res

class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            t = 0
            for i in str(num):
                t += int(i)
            num = t
        return num
# s = Solution()
# s.addDigits(10)


# 673. 最长递增子序列的个数
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
# 注意 这个数列必须是 严格 递增的。
# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 提示: 
# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106



class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        g = [1] * n
        ans = 0
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        g[i] = g[j]
                    elif dp[i] == dp[j] + 1:
                        g[i] += g[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = g[i]
            elif dp[i] == max_len:
                ans += g[i]
        return ans
# s = Solution()
# s.findNumberOfLIS([1,3,5,5,7])







# 72. 编辑距离
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 提示：
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


# dp[i, j]
# 插入一个字符，即在word1插入一个字符，使word1[i]==word2[j],
# 即dp[i-1][j] + 1
# 删除一个字符，即在word1删除一个字符，等价在word2中插入一个字符，使word1[i]==word2[j],
# 即dp[i][j-1] + 1
# 替换一个字符，即在dp[i-1][j-1]的基础上各插入一个字符，使word1[i]==word2[j],
# 即dp[i-1][j-1] + 1，如果word1[i]==word2[j]本就成立，则dp[i-1][j-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1) + 1, len(word2) + 1

        dp = [[max(i, j) for i in range(n2)] for j in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[n1-1][n2-1]



# s = Solution()
# s.minDistance(word1 = "horse", word2 = "ros")


















# 322. 零钱兑换
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
# 提示：
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            print(coin)
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
                print(dp)


# s = Solution()
# s.coinChange([5,2,1], 11)

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3, 5, 7]
        seen = {1}
        heap = [1]

        for i in range(k - 1):
            curr = heapq.heappop(heap)

            print('curr', curr)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

            print(seen)
            print('heap', heap)
        return heapq.heappop(heap)


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k+1)


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if (c == 'R' and i > j) or (c == 'L' and i < j):
                    return False

                i += 1
                j += 1

        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        print(p)
        print()

        for u, v in edges:
            print(p, u, v)
            p[find(u)] = find(v)
            print(p, )
        return find(source) == find(destination)

s = Solution()
s.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)














#
#
# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
#
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
#
#  
#
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
#
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
#
# 请返回待替换子串的最小可能长度。
#
# 如果原字符串自身就是一个平衡字符串，则返回 0。
#
#  
#
# 示例 1：
#
# 输入：s = "QWER"
# 输出：0
# 解释：s 已经是平衡的了。
# 示例 2：
#
# 输入：s = "QQWE"
# 输出：1
# 解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
# 示例 3：
#
# 输入：s = "QQQW"
# 输出：2
# 解释：我们可以把前面的 "QQ" 替换成 "ER"。
# 示例 4：
#
# 输入：s = "QQQQ"
# 输出：3
# 解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/replace-the-substring-for-balanced-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


print()
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        partial = n // 4
        def check():
            if cnt["Q"] > partial \
                    or cnt["W"] > partial \
                    or cnt["E"] > partial \
                    or cnt["R"] > partial:
                return False
            return True

        if check():
            return 0
        ans = n
        r = 0

        for i, v in enumerate(s):
            while r < n and not check():
                cnt[s[r]] -= 1
                r += 1
            if not check():
                break
            ans = min(ans, r - i)
            cnt[v] += 1
        return ans







s = Solution()
r = s.balancedString("WQWRQQQW")
print(r)
























































































