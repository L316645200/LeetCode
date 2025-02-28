#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：1、二分查找.py
# @Author  ：Lin
# @Date    ：2025/1/6 17:51

"""34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
import bisect
from collections import defaultdict, Counter
from itertools import accumulate
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        return [left, right]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def my_bisect(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        start = my_bisect(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        end = my_bisect(nums, target + 1) - 1
        return [start, end]

"""35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
提示:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def my_bisect(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        return my_bisect(nums, target)

"""704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def my_bisect(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        ans = my_bisect(nums, target)
        return ans if ans < len(nums) and nums[ans] == target else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = bisect.bisect_left(nums, target)
        return res if res < len(nums) and nums[res] == target else -1

"""744. 寻找比目标字母大的最小字母
给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
示例 1：
输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
解释：letters 中字典上比 'a' 大的最小字符是 'c'。
示例 2:
输入: letters = ["c","f","j"], target = "c"
输出: "f"
解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
示例 3:
输入: letters = ["x","x","y","y"], target = "z"
输出: "x"
解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
提示：
2 <= letters.length <= 104
letters[i] 是一个小写字母
letters 按非递减顺序排序
letters 最少包含两个不同的字母
target 是一个小写字母
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def my_bisect(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        res = my_bisect(letters, target)
        return letters[res] if res < len(letters) else letters[0]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = bisect.bisect_right(letters, target)
        if res == len(letters):
            res = 0
        return letters[res]

# s = Solution()
# r = s.nextGreatestLetter(["c","f","j"], 'c')
"""2529. 正整数和负整数的最大计数
给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。
示例 1：
输入：nums = [-2,-1,-1,1,2,3]
输出：3
解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 2：
输入：nums = [-3,-2,-1,0,0,1,2]
输出：3
解释：共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 3：
输入：nums = [5,20,66,1314]
输出：4
解释：共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。
提示：
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums 按 非递减顺序 排列。
进阶：你可以设计并实现时间复杂度为 O(log(n)) 的算法解决此问题吗？
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect.bisect_left(nums, 0), len(nums) - bisect.bisect_right(nums, 0))

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def my_bisect(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        left = my_bisect(nums, 0)
        right = my_bisect(nums, 1)
        return max(left, len(nums) - right)


"""1385. 两个数组间的距离值
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
示例 1：
输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
输出：2
解释：
对于 arr1[0]=4 我们有：
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
所以 arr1[0]=4 符合距离要求
对于 arr1[1]=5 我们有：
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
所以 arr1[1]=5 也符合距离要求
对于 arr1[2]=8 我们有：
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
存在距离小于等于 2 的情况，不符合距离要求 
故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
示例 2：
输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
输出：2
示例 3：
输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
输出：1
提示：
1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""

# 二分
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            left = bisect.bisect_left(arr2, i - d)
            right = bisect.bisect_right(arr2, i + d)
            if right - left == 0:
                ans += 1
        return ans

# 滑动窗口
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = j = 0
        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] + d < arr1[i]:
                j += 1
            if j == len(arr2) or arr2[j] > arr1[i] + d:
                ans += 1
        return ans
"""1385. 两个数组间的距离值
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
示例 1：
输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
输出：[4,0,3]
解释：
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
示例 2：
输入：spells = [3,1,2], potions = [8,5,8], success = 16
输出：[2,0,2]
解释：
- 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
- 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
- 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
所以返回 [2,0,2] 。
提示：
n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010
"""
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = j = 0
        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] + d < arr1[i]:
                j += 1
            if j == len(arr2) or arr2[j] > arr1[i] + d:
                ans += 1
        return ans

"""2300. 咒语和药水的成功对数 1477
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
示例 1：
输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
输出：[4,0,3]
解释：
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
示例 2：
输入：spells = [3,1,2], potions = [8,5,8], success = 16
输出：[2,0,2]
解释：
- 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
- 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
- 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
所以返回 [2,0,2] 。
提示：
n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)
        res = [0] * n
        for i in range(n):
            j = bisect.bisect_left(potions, success / spells[i])
            res[i] = m - j
        return res
"""2389. 和有限的最长子序列
给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。
返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度  。
子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。
示例 1：
输入：nums = [4,5,2,1], queries = [3,10,21]
输出：[2,3,4]
解释：queries 对应的 answer 如下：
- 子序列 [2,1] 的和小于或等于 3 。可以证明满足题目要求的子序列的最大长度是 2 ，所以 answer[0] = 2 。
- 子序列 [4,5,1] 的和小于或等于 10 。可以证明满足题目要求的子序列的最大长度是 3 ，所以 answer[1] = 3 。
- 子序列 [4,5,2,1] 的和小于或等于 21 。可以证明满足题目要求的子序列的最大长度是 4 ，所以 answer[2] = 4 。
示例 2：
输入：nums = [2,3,4,5], queries = [1]
输出：[0]
解释：空子序列是唯一一个满足元素和小于或等于 1 的子序列，所以 answer[0] = 0 。
提示：
n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""
# 排序二分
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        for i in range(n):
            nums[i] = nums[i] + nums[i-1] if i > 0 else nums[i]
        for j in range(m):
            queries[j] = bisect.bisect_right(nums, queries[j])
        return queries
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = list(accumulate(sorted(nums)))
        return [bisect.bisect_right(nums, q) for q in queries]

# s = Solution()
# s.answerQueries(nums = [4,5,2,1], queries = [3,10,21])
"""1170. 比较字符串最小字母出现频次
定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
示例 1：
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
示例 2：
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
提示：
1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j]、words[i][j] 都由小写英文字母组成
"""


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 字符串最小字母出现频次
        def get_frequency(char):
            cnt, cur = 0, 'z'
            for c in char:
                if c == cur:
                    cnt += 1
                elif c < cur:
                    cur = c
                    cnt = 1
            return cnt

        words = sorted([get_frequency(word) for word in words])
        n = len(words)
        ans = []
        for query in queries:
            cnt = get_frequency(query)
            ans.append(n - bisect.bisect_right(words, cnt))
        return ans
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 字符串最小字母出现频次
        def get_frequency(char):
            cnt, cur = 0, 'z'
            for c in char:
                if c == cur:
                    cnt += 1
                elif c < cur:
                    cur = c
                    cnt = 1
            return cnt

        count = [0] * 12
        for word in words:
            count[get_frequency(word)] += 1
        for i in range(9, 0, -1):
            count[i] += count[i+1]
        ans = []
        for query in queries:
            ans.append(count[get_frequency(query)+1])
        return ans
# s = Solution()
# s.numSmallerByFrequency(queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"],
#                         words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"])

"""2080. 区间内查询数字的频率 1702
请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。
请你实现 RangeFreqQuery 类：
RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。
示例 1：
输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：
[null, 1, 2]
解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
提示：
1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
调用 query 不超过 105 次。
"""

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.idx = defaultdict(list)
        for i, v in enumerate(arr):
            self.idx[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        idx = self.idx[value]
        start = bisect.bisect_left(idx, left)
        end = bisect.bisect_right(idx, right)
        return end - start

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

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
        res = 0
        n = len(nums)
        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], 0, i)
            right = bisect.bisect_right(nums, upper - nums[i], 0, i)
            res += right - left
        return res

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        left = right = n - 1
        for i in range(n - 1):
            if i >= right:
                break
            while left > i and nums[i] + nums[left] >= lower:
                left -= 1
            while right > i and nums[i] + nums[right] > upper:
                right -= 1
            res += right - max(left, i)
        return res


# s = Solution()
# s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
#
# s.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
"""2856. 删除数对后的最小数组长度 1750
给你一个下标从 0 开始的 非递减 整数数组 nums 。
你可以执行以下操作任意次：
选择 两个 下标 i 和 j ，满足 nums[i] < nums[j] 。
将 nums 中下标在 i 和 j 处的元素删除。剩余元素按照原来的顺序组成新的数组，下标也重新从 0 开始编号。
请你返回一个整数，表示执行以上操作任意次后（可以执行 0 次），nums 数组的 最小 数组长度。
示例 1：
输入：nums = [1,2,3,4]
输出：0
解释：
示例 2：
输入：nums = [1,1,2,2,3,3]
输出：0
解释：
示例 3：
输入：nums = [1000000000,1000000000]
输出：2
解释：
由于两个数字相等，不能删除它们。
示例 4：
输入：nums = [2,3,4,4,4]
输出：1
解释：
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
nums 是 非递减 数组。
"""


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(Counter(nums).values())
        if mx > n // 2:
            return mx * 2 - n
        return n % 2


# 二分
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mx_cnt = bisect.bisect_right(nums, nums[n // 2]) - bisect.bisect_left(nums, nums[n // 2])
        if mx_cnt > n // 2:
            return mx_cnt * 2 - n
        return n % 2
"""981. 基于时间的键值存储
设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。
实现 TimeMap 类：
TimeMap() 初始化数据结构对象
void set(String key, String value, int timestamp) 存储给定时间戳 timestamp 时的键 key 和值 value。
String get(String key, int timestamp) 返回一个值，该值在之前调用了 set，其中 timestamp_prev <= timestamp 。如果有多个这样的值，它将返回与最大  timestamp_prev 关联的值。如果没有值，则返回空字符串（""）。
示例 1：
输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]
解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"
提示：
1 <= key.length, value.length <= 100
key 和 value 由小写英文字母和数字组成
1 <= timestamp <= 107
set 操作中的时间戳 timestamp 都是严格递增的
最多调用 set 和 get 操作 2 * 105 次
"""


class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.timeMap[key]
        idx = bisect.bisect_right(val, timestamp, key=lambda x: x[1]) - 1
        return val[idx][0] if idx >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""1146. 快照数组 1771
实现支持下列接口的「快照数组」- SnapshotArray：
SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
示例：
输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
提示：
1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [[(0, 0)] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.snap_id, val))
        print(self.data)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]
        k = bisect.bisect_right(arr, snap_id, key=lambda x: x[0])
        return arr[k - 1][1]


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]
        k = bisect.bisect_right(arr, snap_id, key=lambda x: x[0])
        return arr[k - 1][1] if len(arr) > 0 and arr[k-1][0] <= snap_id else 0


# d = [[(0, 0)] for i in range(2)]
# print(d)
"""658. 找到 K 个最接近的元素
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
整数 a 比整数 b 更接近 x 需要满足：
|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
示例 1：
输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：
输入：arr = [1,1,2,3,4,5], k = 4, x = -1
输出：[1,1,2,3]
提示：
1 <= k <= arr.length
1 <= arr.length <= 104
arr 按 升序 排列
-104 <= arr[i], x <= 104
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
        return arr[left: right + 1]

"""1818. 绝对差值和 1934
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
|x| 定义为：
如果 x >= 0 ，值为 x ，或者
如果 x <= 0 ，值为 -x
示例 1：
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
示例 2：
输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
示例 3：
输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
提示：
n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105
"""

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """
        计算通过替换 nums1 中的一个元素来最小化绝对差值和的结果

        参数:
        nums1: 整数列表，需要替换元素的数组
        nums2: 整数列表，用于计算绝对差值和的数组

        返回:
        int: 最小化后的绝对差值和
        """
        # 对 nums1 进行排序，以便后续使用二分查找
        sorted_num = sorted(nums1)
        # 获取数组长度
        n = len(nums1)
        # 初始化最大差值和当前差值和
        mx = res = 0
        # 遍历 nums1 和 nums2，计算当前绝对差值和，并找到最大的可优化差值
        for i in range(n):
            # 计算当前元素的绝对差值并累加到 res 中
            res += abs(nums1[i] - nums2[i])
            # 在 sorted_num 中找到最接近 nums2[i] 的元素索引
            idx = bisect.bisect_left(sorted_num, nums2[i])
            # 确保索引在数组范围内，并且当前索引或前一个索引的差值更小
            idx = idx if idx < n and (idx == 0 or abs(sorted_num[idx] - nums2[i]) <= abs(sorted_num[idx - 1] - nums2[i])) else idx - 1
            # 更新最大可优化差值
            mx = max(mx, abs(nums1[i] - nums2[i]) - abs(sorted_num[idx] - nums2[i]))
        # 返回最小化后的绝对差值和，对 10^9 + 7 取模
        return (res - mx) % (10 ** 9 + 7)

# s = Solution()
# s.minAbsoluteSumDiff(nums1 = [56,51,39,1,12,14,58,82,18,41,70,64,18,7,44,90,55,23,11,79,59,76,67,92,60,80,57,11,66,32,76,73,35,65,55,37,38,26,4,7,64,84,98,61,78,1,80,33,5,66,32,30,52,29,41,2,21,83,30,35,21,30,13,26,36,93,81,41,98,23,20,19,45,52,25,51,52,24,2,45,21,97,11,92,28,37,58,29,5,18,98,94,86,65,88,8,75,12,9,66],
#                      nums2 = [64,32,98,65,67,40,71,93,74,24,49,80,98,35,86,52,99,65,15,92,83,84,80,71,46,11,26,70,80,2,81,57,97,12,68,10,49,80,24,18,45,72,33,94,60,5,94,99,14,41,25,83,77,67,49,70,94,83,55,17,61,44,50,62,3,36,67,10,2,39,53,62,44,72,66,7,3,6,80,38,43,100,17,25,24,78,8,4,36,86,9,68,99,64,65,15,42,59,79,66])
"""911. 在线选举 2001
给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。
对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。
在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
实现 TopVotedCandidate 类：
TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。
int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。
示例：
输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]
解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
提示：
1 <= persons.length <= 5000
times.length == persons.length
0 <= persons[i] < persons.length
0 <= times[i] <= 109
times 是一个严格递增的有序数组
times[0] <= t <= 109
每个测试用例最多调用 104 次 q
"""

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        n = len(persons)
        self.lead = [0] * n
        self.vote = defaultdict(int)
        max_vote = 0
        for i, p in enumerate(persons):
            self.vote[p] += 1
            if self.vote[p] >= max_vote:
                max_vote = self.vote[p]
                self.lead[i] = p
            else:
                self.lead[i] = self.lead[i - 1]

    def q(self, t: int) -> int:
        k = bisect.bisect_right(self.times, t)
        return self.lead[k-1] if k > 0 else self.lead[0]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
"""LCP 08. 剧情触发时间
在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。在游戏开始时（第 0 天），三种属性的值均为 0。
随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。
所有剧情的触发条件也用一个二维数组 requirements 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。
根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。
示例 1：
输入： increase = [[2,8,4],[2,5,0],[10,9,8]] requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]
输出: [2,-1,3,-1]
解释：
初始时，C = 0，R = 0，H = 0
第 1 天，C = 2，R = 8，H = 4
第 2 天，C = 4，R = 13，H = 4，此时触发剧情 0
第 3 天，C = 14，R = 22，H = 12，此时触发剧情 2
剧情 1 和 3 无法触发。
示例 2：
输入： increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]] requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
输出: [-1,4,3,3,3]
示例 3：
输入： increase = [[1,1,1]] requirements = [[0,0,0]]
输出: [0]
限制：
1 <= increase.length <= 10000
1 <= requirements.length <= 100000
0 <= increase[i] <= 10
0 <= requirements[i] <= 100000
"""
class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        """
        计算每个剧情的触发时间

        参数：
        increase (List[List[int]]): 表示每天属性的增加量
        requirements (List[List[int]]): 表示每个剧情的触发条件

        返回：
        List[int]: 每个剧情的触发时间，如果不会被触发则为-1
        """
        # 获取增加属性的天数和剧情数量
        m, n = len(increase), len(requirements)
        # 初始化前缀和数组，用于存储每个属性的累计增加量
        pre = [[0, 0, 0] for _ in range(m+1)]
        # 计算每个属性的前缀和
        for i in range(1, m+1):
            for j in range(3):
                pre[i][j] = pre[i-1][j] + increase[i-1][j]

        # 初始化结果数组，用于存储每个剧情的触发时间
        res = [-1] * n
        # 遍历每个剧情
        for i in range(n):
            # 初始化一个列表，用于存储每个属性达到触发条件所需的最小天数
            t = max([bisect.bisect_left(pre, requirements[i][j], key=lambda x: x[j]) for j in range(3)])
            # 如果最小天数小于总天数，则将该剧情的触发时间设置为最小天数
            if t < m + 1:
                res[i] = t
        # 返回结果数组
        return res
s = Solution()
# s.getTriggerTime(increase = [[2,8,4],[2,5,0],[10,9,8]], requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]])

s.getTriggerTime(increase = [[6,3,4],[6,7,2]], requirements = [[0,13,14],[0,5,5],[0,4,18],[4,3,4]])













