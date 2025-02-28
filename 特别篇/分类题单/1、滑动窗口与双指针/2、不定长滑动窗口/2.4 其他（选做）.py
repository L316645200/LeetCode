#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2.4 其他（选做）.py
# @Author  ：Lin
# @Date    ：2024/11/9 16:37


"""1438. 绝对差不超过限制的最长连续子数组 1672
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。
示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。
示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
示例 3：
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
from collections import deque, Counter, defaultdict
from typing import List

from sortedcontainers import SortedList


# 滑动窗口+有序数组
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = left = 0
        arr = SortedList()
        for right, num in enumerate(nums):
            arr.add(num)
            while arr[-1] - arr[0] > limit:
                arr.remove(nums[left])
                left += 1
            res = max(res, right - left + 1)
        return res


"""方法二：滑动窗口 + 单调队列
思路和解法
在方法一中，我们仅需要统计当前窗口内的最大值与最小值，因此我们也可以分别使用两个单调队列解决本题。
在实际代码中，我们使用一个单调递增的队列 queMin 维护最小值，一个单调递减的队列 queMax 维护最大值。
这样我们只需要计算两个队列的队首的差值，即可知道当前窗口是否满足条件。
"""
# 滑动窗口+单调队列
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = left = 0
        deq_max = deque()
        deq_min = deque()
        for right, num in enumerate(nums):
            while deq_max and nums[deq_max[-1]] < num:
                deq_max.pop()
            while deq_min and nums[deq_min[-1]] > num:
                deq_min.pop()

            deq_max.append(right)
            deq_min.append(right)
            while deq_max and deq_min and nums[deq_max[0]] - nums[deq_min[0]] > limit:
                left += 1
                if left > deq_max[0]:
                    deq_max.popleft()
                if left > deq_min[0]:
                    deq_min.popleft()
            res = max(res, right - left + 1)
        return res

# s = Solution()
# s.longestSubarray(nums = [8,2,4,7], limit = 4)

"""2401. 最长优雅子数组 1750
给你一个由 正 整数组成的数组 nums 。
如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。
返回 最长 的优雅子数组的长度。
子数组 是数组中的一个 连续 部分。
注意：长度为 1 的子数组始终视作优雅子数组。
示例 1：
输入：nums = [1,3,8,48,10]
输出：3
解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
- 3 AND 8 = 0
- 3 AND 48 = 0
- 8 AND 48 = 0
可以证明不存在更长的优雅子数组，所以返回 3 。
示例 2：
输入：nums = [3,1,5,11,13]
输出：1
解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = left = or_ = 0
        for right, num in enumerate(nums):
            while or_ & num:  # 有交集
                or_ ^= nums[left]  # 从 or_ 中去掉集合 nums[left]
                left += 1
            or_ |= num  # 把集合 x 并入 or_ 中
            res = max(res, right - left + 1)
        return res

# s = Solution()
# s.longestNiceSubarray(nums = [1,3,8,48,10])

"""1156. 单字符重复子串的最大长度 1787 有简单做法
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
示例 1：
输入：text = "ababa"
输出：3
示例 2：
输入：text = "aaabaaa"
输出：6
示例 3：
输入：text = "aaabbaaa"
输出：4
示例 4：
输入：text = "aaaaa"
输出：5
示例 5：
输入：text = "abcdef"
输出：1
提示：
1 <= text.length <= 20000
text 仅由小写英文字母组成。"""

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        res = 0
        i = 0
        while i < len(text):
            # step1: 找出当前连续的一段 [i, j)
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1

            # step3: 找到这一段后面与之相隔一个不同字符的另一段 [j + 1, k)，如果不存在则 k = j + 1
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            res = max(res, min(k - i, count[text[i]]))
            i = j
        return res


# s = Solution()
# s.maxRepOpt1("aaabaaa")


"""424. 替换后的最长重复字符
给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
可能存在其他的方法来得到同样的结果。
提示：
1 <= s.length <= 105
s 仅由大写英文字母组成
0 <= k <= s.length
"""

"""方法：双指针（滑动窗口）
右边界先移动找到一个满足题意的可以替换 k 个字符以后，所有字符都变成一样的当前看来最长的子串，
直到右边界纳入一个字符以后，不能满足的时候停下；
然后考虑左边界向右移动，左边界只须要向右移动一格以后，右边界就又可以开始向右移动了，
继续尝试找到更长的目标子串；
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        res = left = 0
        for right, c in enumerate(s):
            # 计数+1
            cnt[c] += 1
            # 当字符计数最大+k小于滑动窗口的长度时，说明当前滑动窗口无法全部替换成相同的字符串
            while max(cnt.values()) + k < right - left + 1:
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res


# 优化
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        res = left = cmax = 0
        for right, c in enumerate(s):
            #
            cnt[c] += 1
            cmax = max(cmax, cnt[c])
            if cmax + k < right - left + 1:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# s = Solution()
# s.characterReplacement(s = "ABAB", k = 2)
"""
438. 找到字符串中所有字母异位词 有定长滑窗/不定长滑窗两种写法
给定两个字符串 s 和 p，找到 s 中所有 p 的 
异位词
 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:
1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

# 定长差异数组 滑动窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt1, cnt2 = Counter(), Counter(p)
        k = len(p)
        left = c = 0
        res = []
        for i, char in enumerate(s):
            if cnt1[char] < cnt2[char]:
                c += 1
            cnt1[char] += 1
            if i >= k - 1:
                if c == k:
                    res.append(i-k+1)

                if cnt1[s[left]] <= cnt2[s[left]]:
                    c -= 1
                cnt1[s[left]] -= 1
                left += 1
        return res

# 不定长滑动窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        res = []
        k = len(p)
        left = 0
        for i, char in enumerate(s):
            cnt[char] -= 1  # 右端点字母进入窗口
            while cnt[char] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1 # 左端点字母离开窗口
                left += 1
            if i - left + 1 == k:  # s' 和 p 的每种字母的出现次数都相同
                res.append(left)  # s' 左端点下标加入答案
        return res

# s = Solution()
# s.findAnagrams(s = "cbaebabacd", p = "abc")
#

"""1712. 将数组分成三个子数组的方案数 2079
我们称一个分割整数数组的方案是 好的 ，当它满足：

数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。
示例 1：
输入：nums = [1,1,1]
输出：1
解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
示例 2：
输入：nums = [1,2,2,2,5,0]
输出：3
解释：nums 总共有 3 种好的分割方案：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
示例 3：
输入：nums = [3,2,1]
输出：0
解释：没有好的分割方案。
提示：
3 <= nums.length <= 105
0 <= nums[i] <= 104
"""

"""
pre[n] - pre[right] >= pre[right] - pre[left] >= pre[left]
可得
①2*pre[left]<=pre[right]
②pre[left]>=2*pre[right]-pre[n]
 
"""
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        left1 = left2 = 1
        res = 0
        for right in range(1, n):

            while left1 < right and pre[right] - pre[left1] >= pre[left1]:
                left1 += 1
            while left2 < left1 and pre[n] - pre[right] < pre[right] - pre[left2]:
                left2 += 1
            res += left1 - left2
        return res % (10 ** 9 + 7)


s = Solution()
s.waysToSplit(nums = [1,2,2,2,5,0])












































































