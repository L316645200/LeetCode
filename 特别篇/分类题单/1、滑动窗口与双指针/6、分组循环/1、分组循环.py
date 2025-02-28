#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：1、分组循环.py
# @Author  ：Lin
# @Date    ：2024/12/31 16:56

"""适用场景：按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。

核心思想：

外层循环负责遍历组之前的准备工作（记录开始位置），和遍历组之后的统计工作（更新答案最大值）。
内层循环负责遍历组，找出这一组最远在哪结束。
这个写法的好处是，各个逻辑块分工明确，也不需要特判最后一组（易错点）。以我的经验，这个写法是所有写法中最不容易出 bug 的，推荐大家记住。
"""
import heapq
from collections import defaultdict
from itertools import groupby
from typing import List

"""1446. 连续字符 1165
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串 s 的 能量。
示例 1：
输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
示例 2：
输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
提示：
1 <= s.length <= 500
s 只包含小写英文字母。
"""

class Solution:
    def maxPower(self, s: str) -> int:
        res = j = 0
        for i in range(len(s)):
            if s[j] != s[i]:
                res = max(res, i - j)
                j = i
        return max(res, len(s) - j)


# s = Solution()
# s.maxPower(s = "tourist")
"""1869. 哪种连续子字符串更长 1205
给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回 false 。
例如，s = "110100010" 中，由 1 组成的最长连续子字符串的长度是 2 ，由 0 组成的最长连续子字符串的长度是 3 。
注意，如果字符串中不存在 0 ，此时认为由 0 组成的最长连续子字符串的长度是 0 。字符串中不存在 1 的情况也适用此规则。
示例 1：
输入：s = "1101"
输出：true
解释：
由 1 组成的最长连续子字符串的长度是 2："1101"
由 0 组成的最长连续子字符串的长度是 1："1101"
由 1 组成的子字符串更长，故返回 true 。
示例 2：
输入：s = "111000"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 3："111000"
由 0 组成的最长连续子字符串的长度是 3："111000"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。
示例 3：
输入：s = "110100010"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 2："110100010"
由 0 组成的最长连续子字符串的长度是 3："110100010"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。
提示：
1 <= s.length <= 100
s[i] 不是 '0' 就是 '1'
"""

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1:
            return s == '1'
        mx1 = mx0 = cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
                if s[i] == '1':
                    mx1 = max(mx1, cnt)
                else:
                    mx0 = max(mx0, cnt)
            else:
                cnt = 1
        return mx1 > mx0

# s = Solution()
# s.checkZeroOnes(s = "110100010")

"""2414. 最长的字母序连续子字符串的长度 1222
字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。
例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
示例 1：
输入：s = "abacaba"
输出：2
解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
"ab" 是最长的字母序连续子字符串。
示例 2：
输入：s = "abcde"
输出：5
解释："abcde" 是最长的字母序连续子字符串。
提示：
1 <= s.length <= 105
s 由小写英文字母组成
"""

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res, cur = 1, 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res

# s = Solution()
# s.longestContinuousSubstring(s = "abacaba")

"""1957. 删除字符使字符串变好 1358
一个字符串如果没有 三个连续 相同字符，那么它就是一个 好字符串 。
给你一个字符串 s ，请你从 s 删除 最少 的字符，使它变成一个 好字符串 。
请你返回删除后的字符串。题目数据保证答案总是 唯一的 。
示例 1：
输入：s = "leeetcode"
输出："leetcode"
解释：
从第一组 'e' 里面删除一个 'e' ，得到 "leetcode" 。
没有连续三个相同字符，所以返回 "leetcode" 。
示例 2：
输入：s = "aaabaaaa"
输出："aabaa"
解释：
从第一组 'a' 里面删除一个 'a' ，得到 "aabaaaa" 。
从第二组 'a' 里面删除两个 'a' ，得到 "aabaa" 。
没有连续三个相同字符，所以返回 "aabaa" 。
示例 3：
输入：s = "aab"
输出："aab"
解释：没有连续三个相同字符，所以返回 "aab" 。
提示：
1 <= s.length <= 105
s 只包含小写英文字母。
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        arr = [s[0]]
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
                if cur < 3:
                    arr.append(s[i])
            else:
                arr.append(s[i])
                cur = 1
        return ''.join(arr)

# s = Solution()
# s.makeFancyString(s = "aaabaaaa")
"""674. 最长连续递增序列
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
示例 1：
输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 
示例 2：
输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
提示：
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res, cur = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res
# s = Solution()
# s.findLengthOfLCIS(nums = [1,3,5,4,7])

"""978. 最长湍流子数组
给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。
如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。
更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：
若 i <= k < j ：
当 k 为奇数时， A[k] > A[k+1]，且
当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j ：
当 k 为偶数时，A[k] > A[k+1] ，且
当 k 为奇数时， A[k] < A[k+1]。
示例 1：
输入：arr = [9,4,2,10,7,8,8,1,9]
输出：5
解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
示例 2：
输入：arr = [4,8,12,16]
输出：2
示例 3：
输入：arr = [100]
输出：1
提示：
1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""

#
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = cnt = 1
        cur = 0
        for i in range(1, len(arr)):
            pre = cur
            cur = 1 if arr[i] > arr[i-1] else -1 if arr[i] < arr[i-1] else 0
            if cur == 0:
                cnt = 1
            elif cur != pre:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 2
        return res

# s = Solution()
# s.maxTurbulenceSize(arr = [9,4,2,10,7,8,8,1,9])
"""2110. 股票平滑下跌阶段的数目 1408
给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。
一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。
请你返回 平滑下降阶段 的数目。
示例 1：
输入：prices = [3,2,1,4]
输出：7
解释：总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]
注意，仅一天按照定义也是平滑下降阶段。
示例 2：
输入：prices = [8,6,7,7]
输出：4
解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
示例 3：
输入：prices = [1]
输出：1
解释：总共有 1 个平滑下降阶段：[1]
提示：
1 <= prices.length <= 105
1 <= prices[i] <= 105
"""
# 双指针
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 1
        j = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                res += i - j + 1
            else:
                j = i
                res += 1
        return res


# s = Solution()
# s.getDescentPeriods(prices = [8,6,7,7])

"""228. 汇总区间
给定一个  无重复元素 的 有序 整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
"a->b" ，如果 a != b
"a" ，如果 a == b
示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
提示：
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums 中的所有值都 互不相同
nums 按升序排列
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if i - 1 == j:
                    res.append(str(nums[j]))
                else:
                    res.append(str(nums[j]) + "->" + str(nums[i-1]))
                j = i
        if j == len(nums) - 1:
            res.append(str(nums[j]))
        else:
            res.append(str(nums[j]) + "->" + str(nums[-1]))
        return res


# s = Solution()
# s.summaryRanges(nums = [0,1,2,4,5,7])


"""2760. 最长奇偶子数组 1420
给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。
请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：
nums[l] % 2 == 0
对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
以整数形式返回满足题目要求的最长子数组的长度。
注意：子数组 是数组中的一个连续非空元素序列。
示例 1：
输入：nums = [3,2,5,4], threshold = 5
输出：3
解释：在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 => [2,5,4] ，满足上述条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
示例 2：
输入：nums = [1,2], threshold = 2
输出：1
解释：
在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 => [2] 。
该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
示例 3：
输入：nums = [2,3,4,5], threshold = 4
输出：3
解释：
在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 => [2,3,4] 。 
该子数组满足上述全部条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
提示：
1 <= nums.length <= 100 
1 <= nums[i] <= 100 
1 <= threshold <= 100
"""

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = cnt = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                cnt = 0
                continue
            elif cnt == 0:
                if nums[i] % 2 == 0:
                    cnt += 1
            else:
                if nums[i] % 2 != nums[i-1] % 2:
                    cnt += 1
                else:
                    cnt = 1 if nums[i] % 2 == 0 else 0
            res = max(res, cnt)

        return res

# s = Solution()
# s.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5)


"""1887. 使数组元素相等的减少操作次数 1428
给你一个整数数组 nums ，你的目标是令 nums 中的所有元素相等。完成一次减少操作需要遵照下面的几个步骤：
找出 nums 中的 最大 值。记这个值为 largest 并取其下标 i （下标从 0 开始计数）。如果有多个元素都是最大值，则取最小的 i 。
找出 nums 中的 下一个最大 值，这个值 严格小于 largest ，记为 nextLargest 。
将 nums[i] 减少到 nextLargest 。
返回使 nums 中的所有元素相等的操作次数。
示例 1：
输入：nums = [5,1,3]
输出：3
解释：需要 3 次操作使 nums 中的所有元素相等：
1. largest = 5 下标为 0 。nextLargest = 3 。将 nums[0] 减少到 3 。nums = [3,1,3] 。
2. largest = 3 下标为 0 。nextLargest = 1 。将 nums[0] 减少到 1 。nums = [1,1,3] 。
3. largest = 3 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1] 。
示例 2：
输入：nums = [1,1,1]
输出：0
解释：nums 中的所有元素已经是相等的。
示例 3：
输入：nums = [1,1,2,2,3]
输出：4
解释：需要 4 次操作使 nums 中的所有元素相等：
1. largest = 3 下标为 4 。nextLargest = 2 。将 nums[4] 减少到 2 。nums = [1,1,2,2,2] 。
2. largest = 2 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1,2,2] 。 
3. largest = 2 下标为 3 。nextLargest = 1 。将 nums[3] 减少到 1 。nums = [1,1,1,1,2] 。 
4. largest = 2 下标为 4 。nextLargest = 1 。将 nums[4] 减少到 1 。nums = [1,1,1,1,1] 。
提示：
1 <= nums.length <= 5 * 104
1 <= nums[i] <= 5 * 104
"""

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                res += i
        return res

# s = Solution()
# s.reductionOperations(nums = [5,1,3])


"""845. 数组中的最长山脉 1437
把符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在下标 i（0 < i < arr.length - 1），满足
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
示例 1：
输入：arr = [2,1,4,7,3,2,5]
输出：5
解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
示例 2：
输入：arr = [2,2,2]
输出：0
解释：不存在山脉子数组。
提示：
1 <= arr.length <= 104
0 <= arr[i] <= 104
进阶：
你可以仅用一趟扫描解决此问题吗？
你可以用 O(1) 空间解决此问题吗？
"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        res = 0
        n = len(arr)
        while i < n - 1:
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                left, right = i - 1, i + 1
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < n - 1 and arr[right] > arr[right+1]:
                    right += 1
                res = max(res, right - left + 1)
                i = right + 1
            else:
                i += 1
        return res

# s = Solution()
# s.longestMountain(arr = [2,1,4,7,3,2,5])
"""2038. 如果相邻两个颜色均相同则删除当前颜色
总共有 n 个颜色片段排成一列，每个颜色片段要么是 'A' 要么是 'B' 。给你一个长度为 n 的字符串 colors ，其中 colors[i] 表示第 i 个颜色片段的颜色。
Alice 和 Bob 在玩一个游戏，他们 轮流 从这个字符串中删除颜色。Alice 先手 。
如果一个颜色片段为 'A' 且 相邻两个颜色 都是颜色 'A' ，那么 Alice 可以删除该颜色片段。Alice 不可以 删除任何颜色 'B' 片段。
如果一个颜色片段为 'B' 且 相邻两个颜色 都是颜色 'B' ，那么 Bob 可以删除该颜色片段。Bob 不可以 删除任何颜色 'A' 片段。
Alice 和 Bob 不能 从字符串两端删除颜色片段。
如果其中一人无法继续操作，则该玩家 输 掉游戏且另一玩家 获胜 。
假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 true，否则 Bob 获胜，返回 false。
示例 1：
输入：colors = "AAABABB"
输出：true
解释：
AAABABB -> AABABB
Alice 先操作。
她删除从左数第二个 'A' ，这也是唯一一个相邻颜色片段都是 'A' 的 'A' 。
现在轮到 Bob 操作。
Bob 无法执行任何操作，因为没有相邻位置都是 'B' 的颜色片段 'B' 。
因此，Alice 获胜，返回 true 。
示例 2：
输入：colors = "AA"
输出：false
解释：
Alice 先操作。
只有 2 个 'A' 且它们都在字符串的两端，所以她无法执行任何操作。
因此，Bob 获胜，返回 false 。
示例 3：
输入：colors = "ABBBBBBBAAA"
输出：false
解释：
ABBBBBBBAAA -> ABBBBBBBAA
Alice 先操作。
她唯一的选择是删除从右数起第二个 'A' 。
ABBBBBBBAA -> ABBBBBBAA
接下来轮到 Bob 操作。
他有许多选择，他可以选择任何一个 'B' 删除。
然后轮到 Alice 操作，她无法删除任何片段。
所以 Bob 获胜，返回 false 。
提示：
1 <= colors.length <= 105
colors 只包含字母 'A' 和 'B'
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnta = cntb = 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == "A":
                    cnta += 1
                else:
                    cntb += 1
        return cnta > cntb

# s = Solution()
# s.winnerOfGame(colors = "ABBBBBBBAAA")
"""1759. 统计同质子字符串的数目 1491
给你一个字符串 s ，返回 s 中 同质子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。
同质字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同质字符串。
子字符串 是字符串中的一个连续字符序列。
示例 1：
输入：s = "abbcccaa"
输出：13
解释：同质子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13
示例 2：
输入：s = "xy"
输出：2
解释：同质子字符串是 "x" 和 "y" 。
示例 3：
输入：s = "zzzzz"
输出：15
提示：
1 <= s.length <= 105
s 由小写字符串组成。
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        cur = s[0]
        res, j = 0, 0
        for i in range(len(s)):
            if s[i] != cur:
                cur = s[i]
                j = i
            res += i - j + 1
        return res % mod

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        res = 0
        for c, g in groupby(s):
            n = len(list(g))
            res += n * (n + 1) // 2

        return res % mod

# s = Solution()
# s.countHomogenous(s = "abbcccaa")

"""3011. 判断一个数组是否可以变为有序 1497
给你一个下标从 0 开始且全是 正 整数的数组 nums 。
一次 操作 中，如果两个 相邻 元素在二进制下 
设置位
 的数目 相同 ，那么你可以将这两个元素交换。你可以执行这个操作 任意次 （也可以 0 次）。
如果你可以使数组变为非降序，请你返回 true ，否则返回 false 。
示例 1：
输入：nums = [8,4,2,30,15]
输出：true
解释：我们先观察每个元素的二进制表示。 2 ，4 和 8 分别都只有一个数位为 1 ，分别为 "10" ，"100" 和 "1000" 。15 和 30 分别有 4 个数位为 1 ："1111" 和 "11110" 。
我们可以通过 4 个操作使数组非降序：
- 交换 nums[0] 和 nums[1] 。8 和 4 分别只有 1 个数位为 1 。数组变为 [4,8,2,30,15] 。
- 交换 nums[1] 和 nums[2] 。8 和 2 分别只有 1 个数位为 1 。数组变为 [4,2,8,30,15] 。
- 交换 nums[0] 和 nums[1] 。4 和 2 分别只有 1 个数位为 1 。数组变为 [2,4,8,30,15] 。
- 交换 nums[3] 和 nums[4] 。30 和 15 分别有 4 个数位为 1 ，数组变为 [2,4,8,15,30] 。
数组变成有序的，所以我们返回 true 。
注意我们还可以通过其他的操作序列使数组变得有序。
示例 2：
输入：nums = [1,2,3,4,5]
输出：true
解释：数组已经是非降序的，所以我们返回 true 。
示例 3：
输入：nums = [3,16,8,4,2]
输出：false
解释：无法通过操作使数组变为非降序。
提示：
1 <= nums.length <= 100
1 <= nums[i] <= 28
"""

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        maxj, mini, maxi = 0, 2 ** 8 + 1, 0
        cur = -1
        for i, num in enumerate(nums):
            cnt = num.bit_count()
            if cnt == cur:
                maxi = max(maxi, num)
            else:
                maxj = maxi
                maxi = num
                cur = cnt
            if num <= maxj:
                return False
        return True


# s = Solution()
# s.canSortArray(nums =[3,16,8,4,2])
"""3350. 检测相邻递增子数组 II~1500
给你一个由 n 个整数组成的数组 nums ，请你找出 k 的 最大值，使得存在 两个 相邻 且长度为 k 的 严格递增 
子数组
。具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：
这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
这两个子数组必须是 相邻的，即 b = a + k。
返回 k 的 最大可能 值。
子数组 是数组中的一个连续 非空 的元素序列。
示例 1：
输入：nums = [2,5,7,8,9,2,3,4,3,1]
输出：3
解释：
从下标 2 开始的子数组是 [7, 8, 9]，它是严格递增的。
从下标 5 开始的子数组是 [2, 3, 4]，它也是严格递增的。
这两个子数组是相邻的，因此 3 是满足题目条件的 最大 k 值。
示例 2：
输入：nums = [1,2,3,4,4,4,4,5,6,7]
输出：2
解释：
从下标 0 开始的子数组是 [1, 2]，它是严格递增的。
从下标 2 开始的子数组是 [3, 4]，它也是严格递增的。
这两个子数组是相邻的，因此 2 是满足题目条件的 最大 k 值。
提示：
2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
"""


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suf = [1] * n, [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                pre[i] = pre[i-1] + 1
            if nums[n-i-1] < nums[n-i]:
                suf[n-i-1] = suf[n-i] + 1
        res = 1
        for i in range(n-1):
            res = max(res, min(pre[i], suf[i+1]))
        return res


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                suf[i] = suf[i+1] + 1
        res = pre = 1
        for i in range(1, n - 1):
            if nums[i] > nums[i-1]:
                pre += 1
            else:
                pre = 1
            res = max(res, min(pre, suf[i+1]))
        return res


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = cnt = pre_cnt= 0
        n = len(nums)
        for i in range(n):
            cnt += 1
            if i == n - 1 or nums[i] >= nums[i+1]:
                res = max(res, cnt // 2, min(cnt, pre_cnt))
                pre_cnt = cnt
                cnt = 0
        return res


# s = Solution()
# s.maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1])
"""1578. 使绳子变成彩色的最短时间1574
Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。
Alice 想要把绳子装扮成 五颜六色的 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。给你一个 下标从 0 开始 的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。
返回 Bob 使绳子变成 彩色 需要的 最少时间 。
示例 1：
输入：colors = "abaac", neededTime = [1,2,3,4,5]
输出：3
解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。
示例 2：
输入：colors = "abc", neededTime = [1,2,3]
输出：0
解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。
示例 3：
输入：colors = "aabaa", neededTime = [1,2,3,4,1]
输出：2
解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
提示：
n == colors.length == neededTime.length
1 <= n <= 105
1 <= neededTime[i] <= 104
colors 仅由小写英文字母组成
"""
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = j = 0
        pre_sum = maxi = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                maxi = max(maxi, neededTime[i])
                pre_sum += neededTime[i]
            else:
                if i - j > 1:
                    res += pre_sum - maxi
                pre_sum = maxi = neededTime[i]
                j = i
        return res if j == len(colors) - 1 else res + pre_sum - maxi


# s = Solution()
# s.minCost(colors = "abaac", neededTime = [1,2,3,4,5])

# r = s.minCost(colors = "bbbaaa", neededTime = [4,9,3,8,8,9])
"""1839. 所有元音按顺序排布的最长子字符串 1580
当一个字符串满足如下条件时，我们称它是 美丽的 ：
所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。
这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）
比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。
给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。
子字符串 是字符串中一个连续的字符序列。
示例 1：
输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。
示例 2：
输入：word = "aeeeiiiioooauuuaeiou"
输出：5
解释：最长子字符串是 "aeiou" ，长度为 5 。
示例 3：
输入：word = "a"
输出：0
解释：没有美丽子字符串，所以返回 0 。
提示：
1 <= word.length <= 5 * 105
word 只包含字符 'a'，'e'，'i'，'o' 和 'u' 。
"""

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        mp = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res = j = 0
        cur = -1
        for i, c in enumerate(word):
            if mp[c] - cur in (0, 1):
                cur = mp[c]
                if cur == 4:
                    res = max(res, i - j + 1)
            else:
                cur = 0 if c == 'a' else -1
                j = i if c == 'a' else i + 1
        return res

"""2765. 最长交替子序列 1581
给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：
m 大于 1 。
s1 = s0 + 1 。
下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。
子数组是一个数组中一段连续 非空 的元素序列。
示例 1：
输入：nums = [2,3,4,3,4]
输出：4
解释：交替子数组有 [2,3]，[3,4]，[3,4,3] 和 [3,4,3,4]。最长的子数组为 [3,4,3,4]，长度为 4。
示例 2：
输入：nums = [4,5,6]
输出：2
解释：[4,5] 和 [5,6] 是仅有的两个交替子数组。它们长度都为 2 。
提示：
2 <= nums.length <= 100
1 <= nums[i] <= 104
"""
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res, cur = 1, 1
        pre = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                if pre == nums[i]:
                    cur += 1
                else:
                    cur = 2
            elif nums[i] + 1 == nums[i-1] and pre == nums[i]:
                cur += 1
            else:
                cur = 1
            pre = nums[i-1]
            res = max(res, cur)
        return res if res > 1 else -1

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = -1
        while i < n - 1:
            if nums[i+1] - nums[i] != 1:
                i += 1
                continue
            i0 = i
            i += 2
            while i < n and nums[i] == nums[i-2]:
                i += 1
            res = max(res, i-i0)
            i -= 1
        return res
# s = Solution()
# r = s.alternatingSubarray(nums = [2,3,4,3,4])
# r = s.alternatingSubarray(nums = [88,42,53])
# print(r)

"""3255. 长度为 K 的子数组的能量值 II ~1600
给你一个长度为 n 的整数数组 nums 和一个正整数 k 。
一个数组的 能量值 定义为：
如果 所有 元素都是依次 连续（即 nums[i] + 1 = nums[i + 1]，i < n）且 上升 的，那么能量值为 最大 的元素。
否则为 -1 。
你需要求出 nums 中所有长度为 k 的 
子数组
 的能量值。
请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。
示例 1：
输入：nums = [1,2,3,4,3,2,5], k = 3
输出：[3,4,-1,-1,-1]
解释：
nums 中总共有 5 个长度为 3 的子数组：
[1, 2, 3] 中最大元素为 3 。
[2, 3, 4] 中最大元素为 4 。
[3, 4, 3] 中元素 不是 连续的。
[4, 3, 2] 中元素 不是 上升的。
[3, 2, 5] 中元素 不是 连续的。
示例 2：
输入：nums = [2,2,2,2,2], k = 4
输出：[-1,-1]
示例 3：
输入：nums = [3,2,3,2,3,2], k = 2
输出：[-1,3,-1,3,-1]
提示：
1 <= n == nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= n
"""
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] - 1 == nums[i-1]:
                dp[i] = dp[i-1] + 1
        res = []
        for i in range(n-k+1):
            if dp[i+k-1] >= k:
                res.append(nums[i+k-1])
            else:
                res.append(-1)
        return res

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cur = 1
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] - 1 == nums[i-1]:
                cur += 1
            else:
                cur = 1
            if i >= k - 1:
                if cur >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res

# s = Solution()
# r = s.resultsArray(nums = [1], k = 1)
# print(r)
"""3105. 最长的严格递增或递减子数组
给你一个整数数组 nums 。
返回数组 nums 中 
严格递增
 或 
严格递减
 的最长非空子数组的长度。
示例 1：
输入：nums = [1,4,3,3,2]
输出：2
解释：
nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及 [1,4] 。
nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3,2] 以及 [4,3] 。
因此，返回 2 。
示例 2：
输入：nums = [3,3,3,3]
输出：1
解释：
nums 中严格递增的子数组有 [3]、[3]、[3] 以及 [3] 。
nums 中严格递减的子数组有 [3]、[3]、[3] 以及 [3] 。
因此，返回 1 。
示例 3：
输入：nums = [3,2,1]
输出：3
解释：
nums 中严格递增的子数组有 [3]、[2] 以及 [1] 。
nums 中严格递减的子数组有 [3]、[2]、[1]、[3,2]、[2,1] 以及 [3,2,1] 。
因此，返回 3 。
提示：
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = up[i-1] + 1
            if nums[i] < nums[i-1]:
                down[i] = down[i-1] + 1
        return max(max(up), max(down))


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = down = up = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up += 1
                down = 1
            elif nums[i] < nums[i-1]:
                down += 1
                up = 1
            else:
                up = down = 1
            res = max(res, down, up)
        return res

# s = Solution()
# s.longestMonotonicSubarray(nums = [1,4,3,3,2])
"""467. 环绕字符串中唯一的子字符串 ~1700
定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的：
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。
示例 1：
输入：s = "a"
输出：1
解释：字符串 s 的子字符串 "a" 在 base 中出现。
示例 2：
输入：s = "cac"
输出：2
解释：字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。
示例 3：
输入：s = "zab"
输出：6
解释：字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。
提示：
1 <= s.length <= 105
s 由小写英文字母组成
"""

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())


# s = Solution()
# s.findSubstringInWraproundString(s = "zab")
"""2948. 交换得到字典序最小的数组 2047
给你一个下标从 0 开始的 正整数 数组 nums 和一个 正整数 limit 。
在一次操作中，你可以选择任意两个下标 i 和 j，如果 满足 |nums[i] - nums[j]| <= limit ，则交换 nums[i] 和 nums[j] 。
返回执行任意次操作后能得到的 字典序最小的数组 。
如果在数组 a 和数组 b 第一个不同的位置上，数组 a 中的对应元素比数组 b 中的对应元素的字典序更小，则认为数组 a 就比数组 b 字典序更小。例如，数组 [2,10,3] 比数组 [10,2,3] 字典序更小，下标 0 处是两个数组第一个不同的位置，且 2 < 10 。
示例 1：
输入：nums = [1,5,3,9,8], limit = 2
输出：[1,3,5,8,9]
解释：执行 2 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,3,5,9,8] 。
- 交换 nums[3] 和 nums[4] 。数组变为 [1,3,5,8,9] 。
即便执行更多次操作，也无法得到字典序更小的数组。
注意，执行不同的操作也可能会得到相同的结果。
示例 2：
输入：nums = [1,7,6,18,2,1], limit = 3
输出：[1,6,7,18,1,2]
解释：执行 3 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,6,7,18,2,1] 。
- 交换 nums[0] 和 nums[4] 。数组变为 [2,6,7,18,1,1] 。
- 交换 nums[0] 和 nums[5] 。数组变为 [1,6,7,18,1,2] 。
即便执行更多次操作，也无法得到字典序更小的数组。
示例 3：
输入：nums = [1,7,28,19,10], limit = 3
输出：[1,7,28,19,10]
解释：[1,7,28,19,10] 是字典序最小的数组，因为不管怎么选择下标都无法执行操作。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
"""

"""思路
由于只要大小不超过 limit 的数可以交换，所以我们可以先记录每个数的位置，
然后新建一个空数组，从小到大开始遍历，下个数的大小如果和当前数的大小差不超过 limit，
则可以加入当前数组中，否则就单独成一个数组。
将这些数组分别排序，然后按数的位置依次加入答案数组中即可。
"""

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)
        nums.sort()
        group = []
        idx = []
        for i, num in enumerate(nums):
            if not group or group[-1][-1] + limit < num:
                group.append([])
                idx.append([])
            group[-1].append(num)
            idx[-1].append(mp[num].pop())
        for ix in idx:
            ix.sort()
        for i, g in zip(idx, group):
            for j, num in zip(i, g):
                nums[j] = num
        return nums


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        a = sorted(zip(nums, range(n)))
        res = [0] * n
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and a[i-1][0] + limit >= a[i][0]:
                i += 1
            sub = a[st:i]
            sub_idx = sorted([i for _, i in sub])
            for j, (x, _) in enumerate(sub):
                res[sub_idx[j]] = x
        return res

# s = Solution()
# s.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2)
"""2593. 标记所有元素后数组的分数 做到 O(n)
给你一个数组 nums ，它包含若干正整数。
一开始分数 score = 0 ，请你按照下面算法求出最后分数：
从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。
将选中的整数加到 score 中。
标记 被选中元素，如果有相邻元素，则同时标记 与它相邻的两个元素 。
重复此过程直到数组中所有元素都被标记。
请你返回执行上述算法后最后的分数。
示例 1：
输入：nums = [2,1,3,4,5,2]
输出：7
解释：我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[2,1,3,4,5,2] 。
- 2 是最小未标记元素，所以标记它和左边相邻元素：[2,1,3,4,5,2] 。
- 4 是仅剩唯一未标记的元素，所以我们标记它：[2,1,3,4,5,2] 。
总得分为 1 + 2 + 4 = 7 。
示例 2：
输入：nums = [2,3,5,1,3,2]
输出：5
解释：我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[2,3,5,1,3,2] 。
- 2 是最小未标记元素，由于有两个 2 ，我们选择最左边的一个 2 ，也就是下标为 0 处的 2 ，以及它右边相邻的元素：[2,3,5,1,3,2] 。
- 2 是仅剩唯一未标记的元素，所以我们标记它：[2,3,5,1,3,2] 。
总得分为 1 + 2 + 2 = 5 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 106"""

# nlogn
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        mp = set()
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        res = 0
        while heap:
            val, i = heapq.heappop(heap)
            if i in mp:
                continue
            res += val
            for j in [i-1, i, i+1]:
                mp.add(j)
        return res


s = Solution()
s.findScore(nums = [2,1,3,4,5,2])






































































