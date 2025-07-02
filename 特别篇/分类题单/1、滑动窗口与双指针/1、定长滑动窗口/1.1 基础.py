#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：1、单调栈.py
# @Author  ：Lin
# @Date    ：2024/9/9 16:53
"""https://leetcode.cn/circle/discuss/0viNMK/"""
"""1456. 定长子串中元音的最大数目 1263
给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。
示例 1：
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1
提示：
1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        for i in range(k):
            if s[i] in vowel:
                cnt += 1
        res = cnt

        for j in range(k, len(s)):
            if s[j] in vowel:
                cnt += 1
            if s[j-k] in vowel:
                cnt -= 1
            res = max(res, cnt)
        return res


# s = Solution()
# s.maxVowels(s = "abciiidef", k = 3)
# s.maxVowels("novowels", 1)

"""643. 子数组最大平均数 I
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10-5 的答案都将被视为正确答案。
示例 1：
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
示例 2：
输入：nums = [5], k = 1
输出：5.00000
提示：
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        total = sum(nums[:k])
        res = total
        for i in range(k, n):
            total += nums[i] - nums[i-k]
            res = max(res, total)
        return res / k


# s = Solution()
# s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)

"""1343. 大小为 K 且平均值大于等于阈值的子数组数目 1317
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
示例 1：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
示例 2：

输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
提示：
1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        total = sum(arr[:k])
        res = 0 if total < threshold else 1
        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            if total >= threshold:
                res += 1
        return res

# s = Solution()
# s.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)


"""
2090. 半径为 k 的子数组平均值 1358
给你一个下标从 0 开始的数组 nums ，数组中有 n 个整数，另给你一个整数 k 。
半径为 k 的子数组平均值 是指：nums 中一个以下标 i 为 中心 且 半径 为 k 的子数组中所有元素的平均值，即下标在 i - k 和 i + k 范围（含 i - k 和 i + k）内所有元素的平均值。如果在下标 i 前或后不足 k 个元素，那么 半径为 k 的子数组平均值 是 -1 。
构建并返回一个长度为 n 的数组 avgs ，其中 avgs[i] 是以下标 i 为中心的子数组的 半径为 k 的子数组平均值 。
x 个元素的 平均值 是 x 个元素相加之和除以 x ，此时使用截断式 整数除法 ，即需要去掉结果的小数部分。
例如，四个元素 2、3、1 和 5 的平均值是 (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75，截断后得到 2 。
示例 1：
输入：nums = [7,4,3,9,1,8,5,2,6], k = 3
输出：[-1,-1,-1,5,4,4,-1,-1,-1]
解释：
- avg[0]、avg[1] 和 avg[2] 是 -1 ，因为在这几个下标前的元素数量都不足 k 个。
- 中心为下标 3 且半径为 3 的子数组的元素总和是：7 + 4 + 3 + 9 + 1 + 8 + 5 = 37 。
  使用截断式 整数除法，avg[3] = 37 / 7 = 5 。
- 中心为下标 4 的子数组，avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4 。
- 中心为下标 5 的子数组，avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4 。
- avg[6]、avg[7] 和 avg[8] 是 -1 ，因为在这几个下标后的元素数量都不足 k 个。
示例 2：
输入：nums = [100000], k = 0
输出：[100000]
解释：
- 中心为下标 0 且半径 0 的子数组的元素总和是：100000 。
  avg[0] = 100000 / 1 = 100000 。
示例 3：
输入：nums = [8], k = 100000
输出：[-1]
解释：
- avg[0] 是 -1 ，因为在下标 0 前后的元素数量均不足 k 。
提示：
n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        total = sum(nums[:2*k+1])
        ans = [-1] * n

        for i in range(k, n - k):
            ans[i] = total // (2 * k + 1)
            if k + i + 1 < n:
                total += nums[k+i+1] - nums[i-k]
        return ans

# s = Solution()
# s.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)


"""2379. 得到 K 个黑块的最少涂色次数 1360
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
给你一个整数 k ，表示想要 连续 黑色块的数目。
每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
示例 1：
输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
示例 2：
输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
提示：
n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        for i in range(k):
            if blocks[i] == 'W':
                res += 1
        cnt = res
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                cnt += 1
            if blocks[i-k] == 'W':
                cnt -= 1
            res = min(res, cnt)
        return res

# s = Solution()
# s.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)

"""1652. 拆炸弹 1417
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
给你一个整数 k ，表示想要 连续 黑色块的数目。
每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
示例 1：
输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
示例 2：
输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
提示：
n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n
"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        if k > 0:
            total = sum(code[1:k+1])
        else:
            total = sum(code[n+k:])

        for i in range(n):
            if i > 0:
                if k > 0:
                    total += code[(i+k) % n] - code[i]
                else:
                    total += code[i-1] - code[(i+k-1) % n]
            ans[i] = total
        return ans

# s = Solution()
# s.decrypt(code = [5,7,1,4], k = 3)

"""1052. 爱生气的书店老板 1418
有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。
在某些分钟内，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。
请你返回 这一天营业下来，最多有多少客户能够感到满意 。
示例 1：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
示例 2：
输入：customers = [1], grumpy = [0], minutes = 1
输出：1
提示：
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] == 0 or 1
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = sum([customers[i] * grumpy[i] for i in range(minutes)])
        res = total
        for i in range(minutes, n):
            total += (customers[i] * grumpy[i]) - (customers[i - minutes] * grumpy[i - minutes])
            res = max(res, total)

        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
        return res


"""2841. 几乎唯一子数组的最大和 1546
给你一个整数数组 nums 和两个正整数 m 和 k 。
请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
子数组指的是一个数组中一段连续 非空 的元素序列。
示例 1：
输入：nums = [2,6,7,3,1,7], m = 3, k = 4
输出：18
解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
示例 2：
输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
输出：23
解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
示例 3：
输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
输出：0
解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。
提示：
1 <= nums.length <= 2 * 104
1 <= m <= k <= nums.length
1 <= nums[i] <= 109
"""


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = defaultdict(int)
        res, total = 0, 0
        for i in range(k):
            total += nums[i]
            cnt[nums[i]] += 1
        if len(cnt) >= m:
            res = total
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            cnt[nums[i]] += 1
            cnt[nums[i-k]] -= 1
            if cnt[nums[i-k]] == 0:
                cnt.pop(nums[i-k])
            if len(cnt) >= m:
                res = max(res, total)
        return res

# s = Solution()
# s.maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)

"""2461. 长度为 K 子数组中的最大和 1553
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：
子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。
子数组 是数组中一段连续非空的元素序列。
示例 1：
输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。
示例 2：
输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。
提示：
1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = sum(nums[:k-1])
        cnt = Counter(nums[:k-1])
        res = 0
        for i in range(k-1, len(nums)):
            total += nums[i]
            cnt[nums[i]] += 1
            if len(cnt) == k:
                res = max(res, total)

            out = nums[i-k+1]
            total -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return res


# s = Solution()
# s.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
# s.maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3)


"""1423. 可获得的最大点数 1574
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
示例 1：
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
示例 2：
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
示例 3：
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
示例 4：
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
示例 5：
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202
提示：
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        res = total
        for i in range(k):
            total += cardPoints[n-1-i] - cardPoints[k-i-1]
            res = max(res, total)
        return res


# s = Solution()
# s.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)


"""1297. 子串的最大出现次数 1748
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：
子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
示例 1：
输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：
输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：
输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：
输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
提示：
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
"""

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        n, res = len(s), 0
        for size in range(minSize, maxSize+1):
            str_cnt = Counter(s[:size-1])

            for i in range(size-1, n):
                str_cnt[s[i]] += 1
                k = i+1-size
                if len(str_cnt) <= maxLetters:
                    word = s[k: i+1]
                    cnt[word] += 1
                    res = max(res, cnt[word])

                str_cnt[s[k]] -= 1
                if str_cnt[s[k]] == 0:
                    del str_cnt[s[k]]
        return res

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        n, res = len(s), 0
        str_cnt = Counter(s[:minSize-1])

        for i in range(minSize-1, n):
            str_cnt[s[i]] += 1
            k = i+1-minSize
            if len(str_cnt) <= maxLetters:
                word = s[k: i+1]
                cnt[word] += 1
                res = max(res, cnt[word])

            str_cnt[s[k]] -= 1
            if str_cnt[s[k]] == 0:
                del str_cnt[s[k]]
        return res

# s = Solution()
# s.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)


"""2653. 滑动子数组的美丽值 1786
给你一个长度为 n 的整数数组 nums ，请你求出每个长度为 k 的子数组的 美丽值 。
一个子数组的 美丽值 定义为：如果子数组中第 x 小整数 是 负数 ，那么美丽值为第 x 小的数，否则美丽值为 0 。
请你返回一个包含 n - k + 1 个整数的数组，依次 表示数组中从第一个下标开始，每个长度为 k 的子数组的 美丽值 。
子数组指的是数组中一段连续 非空 的元素序列。
示例 1：
输入：nums = [1,-1,-3,-2,3], k = 3, x = 2
输出：[-1,-2,-2]
解释：总共有 3 个 k = 3 的子数组。
第一个子数组是 [1, -1, -3] ，第二小的数是负数 -1 。
第二个子数组是 [-1, -3, -2] ，第二小的数是负数 -2 。
第三个子数组是 [-3, -2, 3] ，第二小的数是负数 -2 。
示例 2：
输入：nums = [-1,-2,-3,-4,-5], k = 2, x = 2
输出：[-1,-2,-3,-4]
解释：总共有 4 个 k = 2 的子数组。
[-1, -2] 中第二小的数是负数 -1 。
[-2, -3] 中第二小的数是负数 -2 。
[-3, -4] 中第二小的数是负数 -3 。
[-4, -5] 中第二小的数是负数 -4 。
示例 3：
输入：nums = [-3,1,2,-3,0,-3], k = 2, x = 1
输出：[-3,0,-3,-3,-3]
解释：总共有 5 个 k = 2 的子数组。
[-3, 1] 中最小的数是负数 -3 。
[1, 2] 中最小的数不是负数，所以美丽值为 0 。
[2, -3] 中最小的数是负数 -3 。
[-3, 0] 中最小的数是负数 -3 。
[0, -3] 中最小的数是负数 -3 。
提示：
n == nums.length 
1 <= n <= 105
1 <= k <= n
1 <= x <= k 
-50 <= nums[i] <= 50 
"""


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101  # 各个数字出现的次数，题目中范围是 -50<=x<=50
        n = len(nums)
        res = [0] * (n - k + 1)  # 答案数组的长度

        for i in range(n):
            cnt[nums[i] + 50] += 1  # 次数+1

            if i >= k - 1:
                t = 0
                for j in range(50):  # 只统计负数
                    t += cnt[j]
                    if t >= x:
                        res[i-k+1] = j - 50
                        break
                cnt[nums[i-k+1] + 50] -= 1  # 超出长度k的部分次数要减
        return res


s = Solution()
s.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2)




101001







































