#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3、二分答案：求最大.py
# @Author  ：Lin
# @Date    ：2025/1/18 10:46
"""一图掌握二分答案！四种写法！
在练习时，请注意「求最小」和「求最大」的二分写法上的区别。
前面的「求最小」和二分查找求「排序数组中某元素的第一个位置」是类似的，按照红蓝染色法，左边是不满足要求的（红色），右边则是满足要求的（蓝色）。
「求最大」的题目则相反，左边是满足要求的（蓝色），右边是不满足要求的（红色）。这会导致二分写法和上面的「求最小」有一些区别。
以开区间二分为例：
求最小：check(mid) == true 时更新 right = mid，反之更新 left = mid，最后返回 right。
求最大：check(mid) == true 时更新 left = mid，反之更新 right = mid，最后返回 left。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，个人推荐使用开区间写二分。
"""
import bisect
import heapq
from collections import defaultdict
from itertools import groupby
from typing import List

"""275. H 指数 II
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照升序排列。
计算并返回该研究者的 h指数。
h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少有 h 篇论文分别被引用了至少 h 次。
请你设计并实现对数时间复杂度的算法解决此问题。
示例 1：
输入：citations = [0,1,3,5,6]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
    由于研究者有3篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
示例 2：
输入：citations = [1,2,100]
输出：2
提示：
	n == citations.length
	1 <= n <= 10^5
	0 <= citations[i] <= 1000
	citations 按 升序排列
https://leetcode.cn/problems/h-index-ii/description/"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            # citations[n-mid] >= mid说明n-mid后面也全部大于等于mid
            # 也就是至少有mid篇论文被引用了至少mid次
            if citations[n-mid] >= mid:
                left = mid + 1
            else:
                right = mid - 1
        return right

# s = Solution()
# s.hIndex(citations = [0,1,3,5,6])
# s.hIndex(citations = [11,15])
"""2226. 每个小孩最多能分到多少糖果
给你一个 下标从 0 开始 的整数数组 candies 。
数组中的每个元素表示大小为 candies[i] 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，但 无法 再将两堆合并到一起。
另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。
返回每个小孩可以拿走的 最大糖果数目 。
示例 1：
输入：candies = [5,8,6], k = 3
输出：5
解释：可以将 candies[1] 分成大小分别为 5 和 3 的两堆，然后把 candies[2] 分成大小分别为 5 和 1 的两堆。现在就有五堆大小分别为 5、5、3、5 和 1 的糖果。可以把 3 堆大小为 5 的糖果分给 3 个小孩。可以证明无法让每个小孩得到超过 5 颗糖果。
示例 2：
输入：candies = [2,5], k = 11
输出：0
解释：总共有 11 个小孩，但只有 7 颗糖果，但如果要分配糖果的话，必须保证每个小孩至少能得到 1 颗糖果。因此，最后每个小孩都没有得到糖果，答案是 0 。
提示：
	1 <= candies.length <= 10^5
	1 <= candies[i] <= 10^7
	1 <= k <= 10^12
https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        left, right = 1, total // k
        while left <= right:
            mid = (left + right) // 2
            if sum(candie//mid for candie in candies) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return right

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return bisect.bisect_right(range(sum(candies)), -k, key=lambda x: -sum(v // (x + 1) for v in candies))


# s = Solution()
# s.maximumCandies(candies = [5,8,6], k = 3)
"""2982. 找出出现至少三次的最长特殊子字符串 II 1773
2982. 找出出现至少三次的最长特殊子字符串 II
给你一个仅由小写英文字母组成的字符串 s 。
如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。
返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。
子字符串 是字符串中的一个连续 非空 字符序列。
示例 1：
输入：s = "aaaa"
输出：2
解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。
可以证明最大长度是 2 。
示例 2：
输入：s = "abcdef"
输出：-1
解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。
示例 3：
输入：s = "abcaba"
输出：1
解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。
可以证明最大长度是 1 。
提示：
	3 <= s.length <= 5 * 10^5
	s 仅由小写英文字母组成。
https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/description/
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        for i, c in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or c != s[i+1]:
                groups[c].append(cnt)
                cnt = 0
        res = 0
        for val in groups.values():
            val.sort(reverse=True)
            val.extend([0, 0])
            res = max(res, val[0] - 2, min(val[0]-1, val[1]), val[2])
        return res if res > 0 else -1
class Solution:
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        n = len(s)
        for i, c in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or c != s[i+1]:
                groups[c].append(cnt)
                cnt = 0
        res = -1
        for val in groups.values():
            left, right = 1, n - 2
            while left <= right:
                mid = (left + right) // 2
                count = 0
                for v in val:
                    count += max(v - mid + 1, 0)
                if count >= 3:
                    res = max(res, mid)
                    left = mid + 1
                else:
                    right = mid - 1
        return res

# s = Solution()
# s.maximumLength(s = "akphhppppp")
"""2576. 求出最多标记下标 1843
给你一个下标从 0开始的整数数组nums。
一开始，所有下标都没有被标记。你可以执行以下操作任意次：
	选择两个 互不相同且未标记的下标i 和j，满足2 * nums[i] <= nums[j]，标记下标i 和j。
请你执行上述操作任意次，返回nums中最多可以标记的下标数目。
示例 1：
输入：nums = [3,5,2,4]
输出：2
解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
示例 2：
输入：nums = [9,2,5,4]
输出：4
解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
示例 3：
输入：nums = [7,6,8]
输出：0
解释：没有任何可以执行的操作，所以答案为 0 。
提示：
	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^9
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/"""

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        left, right = 0, n // 2
        while left <= right:
            mid = (left + right) // 2
            if all([nums[i] * 2 <= nums[n-mid+i] for i in range(mid)]):
                res = mid * 2
                left = mid + 1
            else:
                right = mid - 1
        return res

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums[(len(nums) + 1) // 2:]:
            if nums[i] * 2 <= x:
                i += 1
        return i * 2

# s = Solution()
# s.maxNumOfMarkedIndices(nums = [3,5,2,4])
"""1898. 可移除字符的最大数目 1913
给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。
同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
请你找出一个整数 k（0 <= k <= removable.length），选出removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。
示例 1：
输入：s = "abcacb", p = "ab", removable = [3,1,0]
输出：2
解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
"ab" 是 "accb" 的一个子序列。
如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
因此，最大的 k 是 2 。
示例 2：
输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
输出：1
解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
"abcd" 是 "abcddddd" 的一个子序列。
示例 3：
输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
输出：0
解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
提示：
	1 <= p.length <= s.length <= 10^5
	0 <= removable.length < s.length
	0 <= removable[i] < s.length
	p 是 s 的一个 子字符串
	s 和 p 都由小写英文字母组成
	removable 中的元素 互不相同
https://leetcode.cn/problems/maximum-number-of-removable-characters/
"""
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)

        def check(k):
            state = [True] * ns
            for i in range(k):
                state[removable[i]] = False
            i = j = 0
            while i < ns and j < np:
                if state[i] and s[i] == p[j]:
                    j += 1
                i += 1
            return j == np

        left, right = 0, len(removable)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


# s = Solution()
# s.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0])
"""1802. 有界数组中指定下标处的最大值 1929
给你三个正整数 n、index 和 maxSum 。
你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
	nums.length == n
	nums[i] 是 正整数 ，其中 0 <= i < n
	abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
	nums 中所有元素之和不超过 maxSum
	nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。
注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
示例 1：
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：
输入：n = 6, index = 1,  maxSum = 10
输出：3
提示：
	1 <= n <= maxSum <= 10^9
	0 <= index < n
https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        k = n - index
        while left <= right:
            mid = (left + right) // 2
            if mid <= index:
                left_sum = (1 + mid) * mid // 2 + (index + 1 - mid)
            else:
                left_sum = (mid + mid - index) * (index + 1) // 2
            if mid < k:
                right_sum = (1 + mid) * mid // 2 + (k - mid)
            else:
                right_sum = (mid + mid - k + 1) * k // 2
            if left_sum + right_sum - mid <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return right


# s = Solution()
# s.maxValue(n = 6, index = 1,  maxSum = 10)
"""1642. 可以到达的最远建筑 1962
给你一个整数数组 heights ，表示建筑物的高度。
另有一些砖块 bricks 和梯子 ladders 。
你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
	如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
	如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
示例 1：
输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。
示例 2：
输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7
示例 3：
输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3
提示：
	1 <= heights.length <= 10^5
	1 <= heights[i] <= 10^6
	0 <= bricks <= 10^9
	0 <= ladders <= heights.length
https://leetcode.cn/problems/furthest-building-you-can-reach/submissions/
"""

# 堆 时间复杂度nlogn
"""
也可以二分答案
二分中把高度差加入列表，然后排序列表
列表较大的值用梯子，小的值用砖块，
看是否可以用砖块到达该建筑，
如果可以，二分右移，否则左移
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [0] * ladders
        heapq.heapify(heap)
        n = len(heights)
        for i in range(1, n):
            k = heights[i] - heights[i-1]
            if k > 0:
                if ladders > 0 and k > heap[0]:
                    heapq.heappush(heap, k)
                    k = heapq.heappop(heap)
                bricks -= k
                if bricks < 0:
                    return i - 1
        return n - 1

# s = Solution()
# s.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2)
"""2861. 最大合金数 1981
假设你是一家合金制造公司的老板，你的公司使用多种金属来制造合金。
现在共有 n 种不同类型的金属可以使用，并且你可以使用 k 台机器来制造合金。每台机器都需要特定数量的每种金属来创建合金。
对于第 i 台机器而言，创建合金需要 composition[i][j] 份 j 类型金属。最初，你拥有 stock[i] 份 i 类型金属，而每购入一份 i 类型金属需要花费 cost[i] 的金钱。
给你整数 n、k、budget，下标从 1 开始的二维数组 composition，两个下标从 1 开始的数组 stock 和 cost，请你在预算不超过 budget 金钱的前提下，最大化 公司制造合金的数量。
所有合金都需要由同一台机器制造。
返回公司可以制造的最大合金数。
示例 1：
输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]
输出：2
解释：最优的方法是使用第 1 台机器来制造合金。
要想制造 2 份合金，我们需要购买：
- 2 份第 1 类金属。
- 2 份第 2 类金属。
- 2 份第 3 类金属。
总共需要 2 * 1 + 2 * 2 + 2 * 3 = 12 的金钱，小于等于预算 15 。
注意，我们最开始时候没有任何一类金属，所以必须买齐所有需要的金属。
可以证明在
示例条件下最多可以制造 2 份合金。
示例 2：
输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]
输出：5
解释：最优的方法是使用第 2 台机器来制造合金。 
要想制造 5 份合金，我们需要购买： 
- 5 份第 1 类金属。
- 5 份第 2 类金属。 
- 0 份第 3 类金属。 
总共需要 5 * 1 + 5 * 2 + 0 * 3 = 15 的金钱，小于等于预算 15 。 
可以证明在
示例条件下最多可以制造 5 份合金。
示例 3：
输入：n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]
输出：2
解释：最优的方法是使用第 3 台机器来制造合金。
要想制造 2 份合金，我们需要购买：
- 1 份第 1 类金属。
- 1 份第 2 类金属。
总共需要 1 * 5 + 1 * 5 = 10 的金钱，小于等于预算 10 。
可以证明在
示例条件下最多可以制造 2 份合金。
提示：
	1 <= n, k <= 100
	0 <= budget <= 10^8
	composition.length == k
	composition[i].length == n
	1 <= composition[i][j] <= 100
	stock.length == cost.length == n
	0 <= stock[i] <= 10^8
	1 <= cost[i] <= 100
https://leetcode.cn/problems/maximum-number-of-alloys/description/"""

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(m):
            for c in composition:
                spend = 0
                for i in range(n):
                    spend += max((c[i] * m - stock[i]), 0) * cost[i]
                if spend <= budget:
                    return True
            return False

        left, right = 0, budget + min(stock)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(m):
            if any(sum(max((c[i] * m - stock[i]), 0) * cost[i] for i in range(n)) <= budget for c in composition):
                return True
            return False

        left, right = 0, budget + min(stock)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right



# s = Solution()
# s.maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3])

# s.maxNumberOfAlloys(n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5])
# TODO
"""3007. 价值和小于等于 K 的最大数字 2258"""


"""3007. 价值和小于等于 K 的最大数字 2258
你有n台电脑。
给你整数n和一个下标从 0开始的整数数组batteries，其中第i个电池可以让一台电脑 运行batteries[i]分钟。你想使用这些电池让全部n台电脑 同时运行。
一开始，你可以给每台电脑连接 至多一个电池。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 任意次。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。
注意，你不能给电池充电。
请你返回你可以让 n台电脑同时运行的 最长分钟数。
示例 1：
输入：n = 2, batteries = [3,3,3]
输出：4
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 1 连接。
2 分钟后，将第二台电脑与电池 1 断开连接，并连接电池 2 。注意，电池 0 还可以供电 1 分钟。
在第 3 分钟结尾，你需要将第一台电脑与电池 0 断开连接，然后连接电池 1 。
在第 4 分钟结尾，电池 1 也被耗尽，第一台电脑无法继续运行。
我们最多能同时让两台电脑同时运行 4 分钟，所以我们返回 4 。
示例 2：
输入：n = 2, batteries = [1,1,1,1]
输出：2
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 2 连接。
一分钟后，电池 0 和电池 2 同时耗尽，所以你需要将它们断开连接，并将电池 1 和第一台电脑连接，电池 3 和第二台电脑连接。
1 分钟后，电池 1 和电池 3 也耗尽了，所以两台电脑都无法继续运行。
我们最多能让两台电脑同时运行 2 分钟，所以我们返回 2 。
提示：
	1 <= n <= batteries.length <= 10^5
	1 <= batteries[i] <= 10^9
https://leetcode.cn/problems/maximum-running-time-of-n-computers/description/
"""

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        # 如果电池和电脑数量相同，则不可更换电池，即最小的电池即为最长运行分钟数
        if m == n:
            return min(batteries)
        # 排序
        batteries.sort()
        # 二分,由数据范围可以判断下界为1,上界可以认为每个电池都可以被充分利用，为sum(batteries) // n
        left, right = 1, sum(batteries) // n
        k = m - n
        while left <= right:
            mid = (left + right) // 2
            s = 0
            for i in range(m):
                if batteries[i] >= mid:
                    break
                if i < k:
                    s += batteries[i]
                else:
                    s -= mid - batteries[i]
            if s >= 0:
                left = mid + 1
            else:
                right = mid - 1
        return right


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        # 如果电池和电脑数量相同，则不可更换电池，即最小的电池即为最长运行分钟数
        if m == n:
            return min(batteries)
        # 排序
        batteries.sort()
        # 二分,由数据范围可以判断下界为1,上界可以认为每个电池都可以被充分利用，为sum(batteries) // n
        left, right = 1, sum(batteries) // n

        while left <= right:
            mid = (left + right) // 2
            if n * mid <= sum(min(b, mid) for b in batteries):
                left = mid + 1
            else:
                right = mid - 1
        return right

# s = Solution()
# s.maxRunTime(n = 2, batteries = [3,3,3])


# TODO
"""2258. 逃离火灾 2347"""
"""2071. 你可以安排的最多任务数目 2648"""





























































































