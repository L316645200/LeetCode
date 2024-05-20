#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：4、子串.py
# @Author  ：Lin
# @Date    ：2024/5/7 17:46

"""560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107"""
import heapq
from typing import List
from collections import defaultdict, deque, Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        res = 0
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        cnt = defaultdict(int)
        for i in range(n+1):
            res += cnt[pre[i] - k]
            cnt[pre[i]] += 1
        return res


# s = Solution()
# s.subarraySum(nums = [1,2,3], k = 3)


# s.subarraySum(nums = [-1,-1,1], k = 0)

# s.subarraySum(nums = [1,1,1], k = 2)



"""239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：
输入：nums = [1], k = 1
输出：[1]
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length"""

# 维护一个先进先出队列，长度不超过k，且第一个值的下标与当前下标差值不超过k，超过则弹出第一个值
# 最后进入队列的值如果比前一个进入的值大，可以直接弹出前面进入的值，
# 一直到队列中没有值或者比最后进入的值大为止


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        ans = []

        for i, num in enumerate(nums):
            while deq and deq[-1][0] <= num:
                deq.pop()
            deq.append([num, i])
            if i >= k-1:
                if deq and i - deq[0][1] == k:
                    deq.popleft()
                ans.append(deq[0][0])
        return ans


# 大根堆On²
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]

        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


# 分块和预处理
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix, suffix = [nums[0]] * n, [nums[-1]] * n
        ans = []
        # 前缀最大值
        for i in range(1, n):
            prefix[i] = nums[i] if i % k == 0 else max(prefix[i-1], nums[i])
        # 后缀最大值
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] if (i + 1) % k == 0 else max(suffix[i+1], nums[i])

        # 取前缀最大值和后缀最大值的较大值
        for i in range(k-1, n):
            j = i - k + 1
            if j % k == 0:
                ans.append(prefix[i])
            else:
                ans.append(max(prefix[i], suffix[j]))
        return ans


s = Solution()
s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)

# s.maxSlidingWindow(nums = [7,2,4], k = 2)



"""76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
提示：
m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        left = 0
        ans_left, ans_right = -1, n - 1
        cnt_s = Counter()
        cnt_t = Counter(t)
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        left = 0
        ans_left, ans_right = -1, n - 1
        cnt_s = Counter()
        cnt_t = Counter(t)
        less = len(cnt_t)

        for right, c in enumerate(s):
            cnt_s[c] += 1
            if cnt_s[c] == cnt_t[c]:
                less -= 1
            while less == 0:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                if cnt_s[s[left]] == cnt_t[s[left]]:
                    less += 1
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


s = Solution()
s.minWindow(s = "ADOBECODEBANC", t = "ABC")




