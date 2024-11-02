#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2.2 求最短、最小.py
# @Author  ：Lin
# @Date    ：2024/11/2 11:47

"""一般题目都有「至少」的要求。

209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：
输入：target = 4, nums = [1,4,4]
输出：1
示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
提示：
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
"""
import math
from collections import Counter
from itertools import count
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, n = 0, len(nums)
        res, total = n + 1, 0
        for right in range(n):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res <= n else 0


s = Solution()
s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])

"""2904. 最短且字典序最小的美丽子字符串 做到 O(n²)
给你一个二进制字符串 s 和一个正整数 k 。
如果 s 的某个子字符串中 1 的个数恰好等于 k ，则称这个子字符串是一个 美丽子字符串 。
令 len 等于 最短 美丽子字符串的长度。
返回长度等于 len 且字典序 最小 的美丽子字符串。如果 s 中不含美丽子字符串，则返回一个 空 字符串。
对于相同长度的两个字符串 a 和 b ，如果在 a 和 b 出现不同的第一个位置上，a 中该位置上的字符严格大于 b 中的对应字符，则认为字符串 a 字典序 大于 字符串 b 。
例如，"abcd" 的字典序大于 "abcc" ，因为两个字符串出现不同的第一个位置对应第四个字符，而 d 大于 c 。
示例 1：
输入：s = "100011001", k = 3
输出："11001"
解释：示例中共有 7 个美丽子字符串：
1. 子字符串 "100011001" 。
2. 子字符串 "100011001" 。
3. 子字符串 "100011001" 。
4. 子字符串 "100011001" 。
5. 子字符串 "100011001" 。
6. 子字符串 "100011001" 。
7. 子字符串 "100011001" 。
最短美丽子字符串的长度是 5 。
长度为 5 且字典序最小的美丽子字符串是子字符串 "11001" 。
示例 2：
输入：s = "1011", k = 2
输出："11"
解释：示例中共有 3 个美丽子字符串：
1. 子字符串 "1011" 。
2. 子字符串 "1011" 。
3. 子字符串 "1011" 。
最短美丽子字符串的长度是 2 。
长度为 2 且字典序最小的美丽子字符串是子字符串 "11" 。 
示例 3：
输入：s = "000", k = 1
输出：""
解释：示例中不存在美丽子字符串。
提示：
1 <= s.length <= 100
1 <= k <= s.length
"""


# 滑动窗口
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        res = s
        # 左指针
        left, cnt = 0, 0
        # 右指针
        for right in range(len(s)):
            # 等于1   +1
            if s[right] == '1':
                cnt += 1
            # 当计数大于等于k时
            while cnt >= k:
                # 先长度最小，再字典序最小
                if len(res) > right - left + 1 or (len(res) == right - left + 1 and res > s[left:right + 1]):
                    res = s[left:right + 1]
                if s[left] == '1':
                    cnt -= 1
                left += 1
        return res


# s = Solution()
# s.shortestBeautifulSubstring(s = "100011001", k = 3)
# s.shortestBeautifulSubstring(s = "001110101101101111", k = 10)

"""1234. 替换子串得到平衡字符串 1878
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
请返回待替换子串的最小可能长度。
如果原字符串自身就是一个平衡字符串，则返回 0。
示例 1：
输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：
输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
示例 3：
输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。 
示例 4：
输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
提示：
1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符
"""


# 替换子字符串可以改为找到左右起始的两段最长子字符串加在一起符合 所有字符出现都小于等于 n/4

#
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        # 字符出现超过n/4的字符种类
        diff = sum([1 for k in cnt.values() if k > n // 4])
        if diff == 0:
            return 0
        res, left = n, 0
        # 滑动窗口，左右指针
        for right in range(n):
            # 右指针滑动，字符数减少
            cnt[s[right]] -= 1
            # 如果字符数刚好等于n/4，说明少了一个 超过n/4的字符种类
            if cnt[s[right]] == n // 4:
                diff -= 1
            # 所有字符计数都小于等于 n/4时，可以移动左指针去求最小的可能长度
            while diff == 0:
                res = min(res, right - left + 1)
                cnt[s[left]] += 1
                # 当字符数刚好等于 n/4+1时，说明多了一个超过n/4的字符种类，要再去移动右指针
                if cnt[s[left]] == n // 4 + 1:
                    diff += 1
                left += 1
        return res

# s = Solution()
# s.balancedString(s = "WQWRQQQW")


"""1234. 替换子串得到平衡字符串 1878
给你一个下标从 0 开始的数组 nums 和一个整数 target 。
下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。
请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。
示例 1：
输入：nums = [1,2,3], target = 5
输出：2
解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。
区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。
示例 2：
输入：nums = [1,1,1,2,3], target = 4
输出：2
解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...].
区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
示例 3：
输入：nums = [2,4,6,8], target = 3
输出：-1
解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。
可以证明，不存在元素和等于目标值 target = 3 的子数组。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= target <= 109
"""


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        k, target = divmod(target, total)
        if target == 0:
            return k * n
        res = (k + 1) * n
        left = 0
        for right in range(n * 2):
            target -= nums[right % n]
            while target < 0:
                target += nums[left % n]
                left += 1
            if target == 0:
                res = min(res, k * n + right - left + 1)
            if left >= n:
                break
        return res if res < (k + 1) * n else -1

# s = Solution()
# r = s.minSizeSubarray(nums = [2,1,5,7,7,1,6,3], target = 39)
# print(r)

"""1574. 删除最短的子数组使剩余数组有序 1932
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。
示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
示例 2：
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
示例 3：
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
示例 4：
输入：arr = [1]
输出：0
提示：
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = n
        left, right = 0, n - 1
        for i in range(1, n):
            if arr[i] >= arr[i-1]:
                left += 1
            if arr[n-i-1] <= arr[n-i]:
                right -= 1
        print(left, right)


s = Solution()
s.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5])
























