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
import heapq
import math
from collections import Counter, defaultdict
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
        left, right = 0, n - 1
        for i in range(1, n):
            if arr[i] >= arr[i-1] and i - 1 == left:
                left += 1
            if arr[n-i-1] <= arr[n-i] and n - i == right:
                right -= 1
        if left >= right:
            return 0
        res = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j < n:
            while i <= left and arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            while j <= n - 1 and arr[i] > arr[j]:
                j += 1
        return res

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
            right -= 1
        if right == 0:
            return 0
        res = right

        for left in range(n-1):
            while right < n and arr[left] > arr[right]:
                right += 1
            res = min(res, right - left - 1)
            if arr[left] > arr[left + 1]:
                return res
        return res


# s = Solution()
# s.findLengthOfShortestSubarray(arr = [6,3,10,11,15,20,13,3,18,12])

# s.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5])

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
        cnt = Counter(t)
        less = len(cnt)
        left, res = 0, ''
        for right in range(len(s)):
            if s[right] in cnt:
                cnt[s[right]] -= 1
                if cnt[s[right]] == 0:
                    less -= 1
            while less == 0:
                if res == '' or right - left + 1 < len(res):
                    res = s[left:right + 1]
                if s[left] in cnt:
                    cnt[s[left]] += 1
                    if cnt[s[left]] == 1:
                        less += 1
                left += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        less = len(cnt) # 不同字母的数量
        left = 0  # 左指针
        ans_left, ans_right = -1, -1 # 结果的左右边界
        # 右指针遍历
        for right in range(len(s)):
            # 遍历字母数-1
            cnt[s[right]] -= 1
            # 如果字母数为0，则不同字母的数量-1
            if cnt[s[right]] == 0:
                less -= 1
            # 当不同字母的数量为0时，说明当前子串包含了t
            while less == 0:
                if ans_left < 0 or right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt[s[left]] += 1
                if cnt[s[left]] == 1:
                    less += 1
                left += 1
        return '' if ans_left < 0 else s[ans_left: ans_right+1]


# s = Solution()
# s.minWindow(s = "ADOBECODEBANC", t = "ABC")

"""632. 最小区间
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
示例 1：
输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：
输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
提示：
nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] 按非递减顺序排列
"""

# 贪心+最小堆
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        # 右指针的值， 和最小堆，右指针为维护堆的最大值
        right, heap = nums[0][0], []
        # 初始化最小堆
        for i in range(k):
            heap.append([nums[i][0], i, 0])
            right = max(right, nums[i][0])
        heapq.heapify(heap)
        # 初始化区间大小size和结果区间res
        size, res = right - heap[0][0], [heap[0][0], right]
        while True:
            # 移除最小堆的最小值， 判断此时区间right-left和之前的size大小
            left, i, j = heapq.heappop(heap)
            if size > right - left:
                size = right - left
                res = [left, right]
            j += 1
            # 当某个列表的所有值都参与过区间最小值时，结束循环
            if j == len(nums[i]):
                return res
            # 最小堆加入被移除最小值的列表的下一个值
            heapq.heappush(heap, [nums[i][j], i, j])
            # 更新堆的最大值
            right = max(right, nums[i][j])

"""
在讲这个方法之前我们先思考这样一个问题：有一个序列 A和一个序列 B，
请找出一个 B 中的一个最小的区间，使得在这个区间中 A 序列的每个数字至少出现一次，
请注意 A 中的元素可能重复，也就是说如果 A 中有 p 个 u，
那么你选择的这个区间中 u 的个数一定不少于 p。没错，这就是我们五月份的一道打卡题：
「76. 最小覆盖子串」。官方题解使用了一种滑动窗口的方法，
遍历整个 B 序列并用一个哈希表表示当前窗口中的元素：
右边界在每次遍历到新元素的时候右移，同时将拓展到的新元素加入哈希表；
左边界右移当且仅当当前区间为一个合法的答案区间，即当前窗口内的元素包含 A 中所有的元素，
同时将原来左边界指向的元素从哈希表中移除；
答案更新当且仅当当前窗口内的元素包含 A 中所有的元素。
如果这个地方不理解，可以参考「76. 最小覆盖子串的官方题解」。

回到这道题，我们发现这两道题的相似之处在于都要求我们找到某个符合条件的最小区间，
我们可以借鉴「76. 最小覆盖子串」的做法：这里序列 {0,1,⋯,k−1} 就是上面描述的 A 序列，
即 k 个列表，我们需要在一个 B 序列当中找到一个区间，可以覆盖 A 序列。
这里的 B 序列是什么？我们可以用一个哈希映射来表示 B 序列—— B[i] 表示 i 在哪些列表当中出现过，
这里哈希映射的键是一个整数，表示列表中的某个数值，哈希映射的值是一个数组，
这个数组里的元素代表当前的键出现在哪些列表里。也许文字表述比较抽象，大家可以结合下面这个例子来理解。

如果列表集合为：
0: [-1, 2, 3]
1: [1]
2: [1, 2]
3: [1, 1, 3]
那么可以得到这样一个哈希映射
-1: [0]
 1: [1, 2, 3, 3]
 2: [0, 2]
 3: [0, 3]
我们得到的这个哈希映射就是这里的 B 序列。我们要做的就是在 B 序列上使用两个指针维护一个滑动窗口，
并用一个哈希表维护当前窗口中已经包含了哪些列表中的元素，记录它们的索引。遍历 B 序列的每一个元素：
指向窗口右边界的指针右移当且仅当每次遍历到新的元素，
并将这个新的元素对应的值数组中的每一个数加入到哈希表中；
指向窗口左边界的指针右移当且仅当当前区间内的元素包含 A 中所有的元素，
同时将原来左边界对应的值数组的元素们从哈希表中移除；
答案更新当且仅当当前窗口内的元素包含 A 中所有的元素。
"""

# 哈希+滑动窗口
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        indices = defaultdict(list)
        n = len(nums)
        # 初始化最大值和最小值
        xmin, xmax = 10 ** 9, -10 ** 9
        # 将nums中的数把值当key下标当value放入字典中
        for i, arr in enumerate(nums):
            for x in arr:
                indices[x].append(i)
            # 最大和最小值
            xmin = min(xmin, *arr)
            xmax = max(xmax, *arr)
        # 初始化滑动窗口的左右端点
        left, right = xmin, xmin - 1
        # 初始化结果值
        bestleft, bestright = xmin, xmax
        cnt = [0] * n
        inside = 0
        # 滑动窗口
        while right < xmax:
            right += 1
            # 遍历key值
            if right in indices:
                for i in indices[right]:
                    cnt[i] += 1
                    # 如果数量为1，说明又有一个列表被包含在内
                    if cnt[i] == 1:
                        inside += 1
            # 当所有列表都被包含在内时
            while inside == n:
                # 当前窗口小于最佳窗口则更新最佳窗口0
                if right - left < bestright - bestleft:
                    bestleft, bestright = left, right
                if left in indices:
                    for i in indices[left]:
                        cnt[i] -= 1
                        #如果数量为0，说明有一个列表不再被包含在内
                        if cnt[i] == 0:
                            inside -= 1
                left += 1
        return [bestleft, bestright]


s = Solution()
# r = s.smallestRange(nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
r = s.smallestRange([[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],[-10,10],[-11,11],[-12,12],[-13,13],[-14,14],[-15,15],[-16,16],[-17,17],[-18,18],[-19,19],[-20,20],[-21,21],[-22,22],[-23,23],[-24,24],[-25,25],[-26,26],[-27,27],[-28,28],[-29,29],[-30,30],[-31,31],[-32,32],[-33,33],[-34,34],[-35,35],[-36,36],[-37,37],[-38,38],[-39,39],[-40,40],[-41,41],[-42,42],[-43,43],[-44,44],[-45,45],[-46,46],[-47,47],[-48,48],[-49,49],[-50,50],[-51,51],[-52,52],[-53,53],[-54,54],[-55,55]])
print(r)









