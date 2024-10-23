#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2.1 求最长、最大.py
# @Author  ：Lin
# @Date    ：2024/9/21 10:16

"""3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长
子串
 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""
import bisect
from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        i, res = 0, 0
        for j in range(len(s)):
            while s[j] in mp:
                mp.remove(s[i])
                i += 1
            mp.add(s[j])
            res = max(res, j - i + 1)
        return res

# s = Solution()
# s.lengthOfLongestSubstring( s = "abcabcbb")

"""3090. 每个字符最多出现两次的最长子字符串 1329
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该
子字符串
的 最大 长度。
示例 1：
输入： s = "bcbbbcba"
输出： 4
解释：
以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
示例 2：
输入： s = "aaaa"
输出： 2
解释：
以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
提示：
2 <= s.length <= 100
s 仅由小写英文字母组成。
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        i = 0
        res = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while cnt[s[j]] > 2:
                cnt[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

# s = Solution()
# s.maximumLengthSubstring(s = "bcbbbcba")

"""1493. 删掉一个元素以后全为 1 的最长子数组 1423
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。
提示 1：
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
提示：
1 <= nums.length <= 105
nums[i] 要么是 0 要么是 1 。
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = -1, -1
        n = len(nums)
        res = 0
        for k, num in enumerate(nums):
            if num == 0:
                if j == -1:
                    j = k
                else:
                    i, j = j, k
            else:
                res = max(res, k - i - (j != -1))
        return min(res, n-1)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        res = 0
        for num in nums:
            if num == 0:
                i, j = j, 0
            else:
                i += 1
                j += 1
            res = max(res, j)
        return min(res, len(nums) - 1)


# s = Solution()
# s.longestSubarray(nums = [1,1,0,1])

# s.longestSubarray(nums = [1,0,0,0,0])
# s.longestSubarray(nums = [1,1,1])


"""1208. 尽可能使字符串相等 1497
给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
示例 1：
输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
示例 2：
输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
示例 3：
输入：s = "abcd", t = "acde", maxCost = 0
输出：1
解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。
提示：
1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s 和 t 都只含小写英文字母。
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [0] * (n + 1)
        # 相同位置字符ASCII码值的差的绝对值的  前缀和
        for i in range(n):
            diff[i+1] = diff[i] + abs(ord(s[i]) - ord(t[i]))

        left, res = 0, 0
        # 滑动窗口
        for i in range(1, n+1):
            while diff[i] - diff[left] > maxCost:
                left += 1
            res = max(res, i - left)
        return res

# s = Solution()
# s.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)
# s.equalSubstring(s = "krpgjbjjznpzdfy", t = "nxargkbydxmsgby", maxCost = 14)

"""2730. 找到最长的半重复子字符串 1502
给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。
如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，"0010" 、"002020" 、"0123" 、"2002" 和 "54944" 是半重复字符串，而 "00101022" （相邻的相同数字对是 00 和 22）和 "1101234883" （相邻的相同数字对是 11 和 88）不是半重复字符串。
请你返回 s 中最长 半重复 
子字符串
 的长度。
示例 1：
输入：s = "52233"
输出：4
解释：
最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。
示例 2：
输入：s = "5494"
输出：4
解释：
s 是一个半重复字符串。
示例 3：
输入：s = "1111111"
输出：2
解释：
最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。
提示：
1 <= s.length <= 50
'0' <= s[i] <= '9'
"""

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # left:子字符串起始下标，right：子字符串中唯一相邻字符相等的右字符的下标
        left, right = 0, 0
        res = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                left, right = right, i
            res = max(res, i - left + 1)
        return res

# s = Solution()
# s.longestSemiRepetitiveSubstring(s = "0010")


"""904. 水果成篮 1516
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。
示例 1：
输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。
示例 2：
输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。
示例 3：
输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。
示例 4：
输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。
提示：

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        left, res = 0, 1
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                k = fruits[left]
                cnt[k] -= 1
                if cnt[k] == 0:
                    del cnt[k]
                left += 1
            res = max(res, right - left + 1)
        return res


# s = Solution()
# s.totalFruit(fruits = [3,3,3,1,2,1,1,2,3,3,4])

"""1695. 删除子数组的最大得分 1529
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。
示例 1：
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp = set()
        left = total = res = 0
        for i, num in enumerate(nums):
            while num in mp:
                total -= nums[left]
                mp.remove(nums[left])
                left += 1
            total += num
            mp.add(num)
            res = max(res, total)
        return res
# s = Solution()
# s.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])


"""2958. 最多 K 个重复元素的最长子数组 1535
给你一个整数数组 nums 和一个整数 k 。
一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。
如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。
请你返回 nums 中 最长好 子数组的长度。
子数组 指的是一个数组中一段连续非空的元素序列。
示例 1：
输入：nums = [1,2,3,1,2,3,1,2], k = 2
输出：6
解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。
最长好子数组的长度为 6 。
示例 2：
输入：nums = [1,2,1,2,1,2,1,2], k = 1
输出：2
解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
最长好子数组的长度为 2 。
示例 3：
输入：nums = [5,5,5,5,5,5,5], k = 4
输出：4
解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
最长好子数组的长度为 4 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= nums.length
"""

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left = res = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# s = Solution()
# s.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1)

"""2779. 数组的最大美丽值 1638
给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。
在一步操作中，你可以执行下述指令：
在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。
对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。
注意：你 只 能对每个下标执行 一次 此操作。
数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。
示例 1：
输入：nums = [4,6,1,2], k = 2
输出：3
解释：在这个示例中，我们执行下述操作：
- 选择下标 1 ，将其替换为 4（从范围 [4,8] 中选出），此时 nums = [4,4,1,2] 。
- 选择下标 3 ，将其替换为 4（从范围 [0,4] 中选出），此时 nums = [4,4,1,4] 。
执行上述操作后，数组的美丽值是 3（子序列由下标 0 、1 、3 对应的元素组成）。
可以证明 3 是我们可以得到的由相等元素组成的最长子序列长度。
示例 2：
输入：nums = [1,1,1,1], k = 10
输出：4
解释：在这个示例中，我们无需执行任何操作。
数组 nums 的美丽值是 4（整个数组）。
提示：
1 <= nums.length <= 105
0 <= nums[i], k <= 105
"""

# 排序+滑动窗口
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, res = 0, 0
        for right in range(len(nums)):
            while nums[right] > nums[left] + k * 2:
                left += 1
            res = max(res, right - left + 1)
        return res


# 差分数组
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = max(nums)
        cnt = [0] * (n + 2)
        for num in nums:
            cnt[max(num-k, 0)] += 1
            cnt[min(num+k, n)+1] -= 1
        res, cur = 0, 0
        for c in cnt:
            cur += c
            res = max(res, cur)
        return res


# s = Solution()
# s.maximumBeauty(nums = [4,6,1,2], k = 2)


"""2024. 考试的最大困扰度 1643
一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。
给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：
每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。
示例 1：
输入：answerKey = "TTFF", k = 2
输出：4
解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
总共有四个连续的 'T' 。
示例 2：
输入：answerKey = "TFFT", k = 1
输出：3
解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
两种情况下，都有三个连续的 'F' 。
示例 3：
输入：answerKey = "TTFTTFTT", k = 1
输出：5
解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
两种情况下，都有五个连续的 'T' 。
提示：
n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] 要么是 'T' ，要么是 'F'
1 <= k <= n
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutive(char):
            cnt = 0
            left, ans = 0, 0
            for right, c in enumerate(answerKey):
                if c == char:
                    cnt += 1
                while cnt > k:
                    if answerKey[left] == char:
                        cnt -= 1
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutive('F'), maxConsecutive('T'))


# s = Solution()
# s.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)

"""1004. 最大连续 1 的个数 III 1656
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
示例 1：
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1
0 <= k <= nums.length
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left, cnt = 0, 0
        for right, num in enumerate(nums):
            cnt += 1 if num == 0 else 0
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# s = Solution()
# s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)

"""1658. 将 x 减到 0 的最小操作数
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1
示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total, n = sum(nums), len(nums)
        if total < x:
            return -1
        left, ans = 0, n + 1
        for i in range(n):
            total -= nums[i]
            while total < x:
                total += nums[left]
                left += 1
            if total == x:
                ans = min(ans, n - i + left - 1)
        return ans if ans < n + 1 else -1


# s = Solution()
# s.minOperations(nums = [1,1,4,2,3], x = 5)
# s.minOperations(nums = [3,2,20,1,1,3], x = 10)

"""1838. 最高频元素的频数 1876
元素的 频数 是该元素在一个数组中出现的次数。
给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
示例 1：
输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
示例 2：
输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
示例 3：

输入：nums = [3,9,6], k = 2
输出：1
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""

# 二分+滑动窗口
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = left = total = 0
        for right in range(len(nums)):
            total += (nums[right] - nums[right-1]) * (right - left)
            while total > k:
                total -= (nums[right] - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# s = Solution()
# r = s.maxFrequency(nums = [1,4,8,13], k = 5)
# print(r)


"""2516. 每种字符至少取 K 个 1948
给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
示例 1：
输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
示例 2：
输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
提示：
1 <= s.length <= 105
s 仅由字母 'a'、'b'、'c' 组成
0 <= k <= s.length
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [0] * 3
        for i in range(n):
            cnt[ord(s[i]) - ord('a')] += 1
        if cnt[0] < k or cnt[1] < k or cnt[2] < k:
            return -1

        res, left = n, 0
        for i, c in enumerate(s):
            cnt[ord(c) - ord('a')] -= 1
            while cnt[0] < k or cnt[1] < k or cnt[2] < k:
                cnt[ord(s[left]) - ord('a')] += 1
                left += 1
            res = min(res, n-i-1+left)
        return res

# s = Solution()
# s.takeCharacters(s = "aabaaaacaabc", k = 2)


"""2831. 找出最长等值子数组 1976
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。
从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。
子数组 是数组中一个连续且可能为空的元素序列。
示例 1：
输入：nums = [1,3,2,3,1,3], k = 3
输出：3
解释：最优的方案是删除下标 2 和下标 4 的元素。
删除后，nums 等于 [1, 3, 3, 3] 。
最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
可以证明无法创建更长的等值子数组。
示例 2：
输入：nums = [1,1,2,2,1,1], k = 2
输出：4
解释：最优的方案是删除下标 2 和下标 3 的元素。 
删除后，nums 等于 [1, 1, 1, 1] 。 
数组自身就是等值子数组，长度等于 4 。 
可以证明无法创建更长的等值子数组。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= nums.length
0 <= k <= nums.length
"""


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = 0
        for idx in pos.values():
            j, left = 0, idx[0]
            for i, right in enumerate(idx):
                while right - left - (i - j) > k:
                    j += 1
                    left = idx[j]
                ans = max(ans, i - j + 1)
        return ans

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left, ans = 0, 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while right - left + 1 - cnt[nums[left]] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, cnt[nums[right]])  # 因为最大值时nums[left]==num[right]
        return ans


# s = Solution()
# s.longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3)
# s.longestEqualSubarray(nums = [3,1,1,], k = 2)

"""2271. 毯子覆盖的最多白色砖块数 2022
给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。
同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子的长度。
请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
示例 1：
输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
输出：9
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 9 块瓷砖，所以返回 9 。
注意可能有其他方案也可以覆盖 9 块瓷砖。
可以看出，瓷砖无法覆盖超过 9 块瓷砖。
示例 2：
输入：tiles = [[10,11],[1,1]], carpetLen = 2
输出：2
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 2 块瓷砖，所以我们返回 2 。
提示：
1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
tiles 互相 不会重叠 。
"""
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left = 0
        res, white = 0, 0
        for i, tile in enumerate(tiles):
            if i > 0:
                white += (tile[0] - tiles[i-1][1] - 1)
            while tile[1] - tiles[left][0] + 1 >= carpetLen and left < i:
                res = max(res, carpetLen - white)
                white -= (tiles[left+1][0] - tiles[left][1] - 1)
                left += 1

            res = max(res, min(tile[1] - tiles[left][0] + 1 - white, carpetLen))
        return res

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left = 0
        res, cover = 0, 0
        for i, tile in enumerate(tiles):
            cover += tile[1] - tile[0] + 1
            while tiles[left][1] < tile[1] - carpetLen + 1:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # 0 表示毯子左端点不在瓷砖内的情况
            res = max(res, cover - max((tile[1] - tiles[left][0] + 1 - carpetLen), 0))
        return res


# s = Solution()
# s.maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10)
# r = s.maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2)

"""2106. 摘水果 2062[hard]
在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 fruits ，其中 fruits[i] = [positioni, amounti] 表示共有 amounti 个水果放置在 positioni 上。fruits 已经按 positioni 升序排列 ，每个 positioni 互不相同 。
另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。
返回你可以摘到水果的 最大总数 。
示例 1：
输入：fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
输出：9
解释：
最佳路线为：
- 向右移动到位置 6 ，摘到 3 个水果
- 向右移动到位置 8 ，摘到 6 个水果
移动 3 步，共摘到 3 + 6 = 9 个水果
示例 2：
输入：fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
输出：14
解释：
可以移动最多 k = 4 步，所以无法到达位置 0 和位置 10 。
最佳路线为：
- 在初始位置 5 ，摘到 7 个水果
- 向左移动到位置 4 ，摘到 1 个水果
- 向右移动到位置 6 ，摘到 2 个水果
- 向右移动到位置 7 ，摘到 4 个水果
移动 1 + 3 = 4 步，共摘到 7 + 1 + 2 + 4 = 14 个水果
示例 3：
输入：fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
输出：0
解释：
最多可以移动 k = 2 步，无法到达任一有水果的地方
提示：

1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
对于任意 i > 0 ，positioni-1 < positioni 均成立（下标从 0 开始计数）
1 <= amounti <= 104
0 <= k <= 2 * 105
"""

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        mp = defaultdict(int)
        for position, amount in fruits:
            mp[position] = amount
        total = sum([mp[i] for i in range(startPos - k, startPos+1)])
        ans = total
        left, right = k, 0
        while left > 0 and right < k:
            total -= mp[startPos - left]
            left -= 1
            right += 1
            total += mp[startPos + right]
            if left + 1 == right:
                pass
            elif left == right:
                total -= mp[startPos - left]
                left -= 1
                right += 1
                total += mp[startPos + right]
            elif left > right:
                total -= mp[startPos - left]
                left -= 1
            elif right > left and left != 0:
                right += 1
                total += mp[startPos + right]

            ans = max(ans, total)
        if left == 0 and right == k - 1:
            ans = max(ans, total + mp[startPos + k])
        return ans
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = bisect.bisect_left(fruits, startPos - k, key=lambda x: x[0])
        right = bisect.bisect_left(fruits, startPos + 1, key=lambda x: x[0])
        ans = total = sum(c for _, c in fruits[left:right])

        while right < len(fruits) and fruits[right][0] <= startPos + k:
            total += fruits[right][1]  # 枚举最右位置为 fruits[right][0]
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                    fruits[right][0] - fruits[left][0] * 2 + startPos > k:
                total -= fruits[left][1]  # fruits[left][0] 无法到达
                left += 1
            ans = max(ans, total)  # 更新答案最大值
            right += 1  # 继续枚举下一个最右位置
        return ans


"""2555. 两个线段获得的最多奖品 2081
在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，其中 prizePositions[i] 是第 i 件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 k 。
你可以同时选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。
比方说 k = 2 ，你可以选择线段 [1, 3] 和 [2, 4] ，你可以获得满足 1 <= prizePositions[i] <= 3 或者 2 <= prizePositions[i] <= 4 的所有奖品 i 。
请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。
示例 1：
输入：prizePositions = [1,1,2,2,3,3,5], k = 2
输出：7
解释：这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
示例 2：
输入：prizePositions = [1,2,3,4], k = 0
输出：2
解释：这个例子中，一个选择是选择线段 [3, 3] 和 [4, 4] ，获得 2 个奖品。
提示：
1 <= prizePositions.length <= 105
1 <= prizePositions[i] <= 109
0 <= k <= 109 
prizePositions 有序非递减。
"""

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if 2 * k + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        mx = [0] * (n + 1)
        left = 0
        res = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            mx[right+1] = max(mx[right], right - left + 1)

            res = max(res, mx[left] + right - left + 1)
        return res


s = Solution()
# s.maximizeWin(prizePositions = [1,1,2,2,3,3,5], k = 2)

s.maximizeWin(prizePositions = [3937,3938,3939,3951,3951,3959,3975,3988,3993,4010,4031,4033,4036,4038,4039,4041,4047,4058,4059,4064,4072,4081,4084,4084,4089,4094,4098,4112,4114,4116,4123,4123,4127,4130,4135,4143,4149,4152,4163,4164,4176,4178,4180,4198,4216,4224,4233,4240,4253,4259,4273,4286,4305,4322,4335,4350,4364,4378,4396,4397,4398,4404,4415,4421,4430,4469,4476,4490,4492,4497,4504,4519,4519,4525,4526,4530,4530,4540,4550,4554,4563,4571,4571,4595,4595,4606,4639,4639,4660,4663,4676,4678,4680,4695,4697,4709,4709,4711,4724,4751,4781,4786,4786,4794,4797,4801,4807,4808,4817,4822,4824,4825,4840,4851,4887,4889,4891,4910,4917,4927,4931,4932,4951,4959,4964,4993,4997,5003,5003,5006,5006,5022,5029,5035,5043,5045,5045,5046,5059,5060,5079,5084,5105,5109,5109,5112,5120,5126,5130,5142,5143,5151,5152,5154,5156,5168,5189,5213,5214,5223,5226,5235,5247,5259,5272,5289,5303,5309,5317,5322,5344,5347,5352,5374,5379,5380,5383,5385,5391,5418,5425,5429,5432,5479,5486,5490,5502,5502,5505,5506,5509,5515,5518,5519,5521,5526,5528,5533,5536,5536,5538,5555,5556,5557,5557,5566,5571,5580,5585,5596,5604,5619,5634,5649,5668,5694,5696,5699,5701,5704,5709,5732,5745,5745,5746,5749,5762,5766,5766,5770,5773,5796,5810,5817,5823,5838,5843,5846,5860,5869,5872,5877,5880,5896,5899,5902,5905,5910,5913,5913,5915,5923], k = 220)





















