#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：7、第 K 小or大.py
# @Author  ：Lin
# @Date    ：2025/2/14 15:22
"""第 k 小等价于：求最小的 x，满足 ≤x的数至少有 k个。
第 k 大等价于：求最大的 x，满足 ≥x的数至少有 k个。
⚠注意：一般来说，题目规定 k 从 1 开始，而不是像下标那样从 0 开始。
⚠注意：一般来说，题目规定不能去重。例如数组 [1,1,1,2,2]，
其中第 1 小、第 2 小和第 3 小的数都是 1，第 4 小和第 5 小的数都是 2。
部分题目也可以用堆解决。
"""
import bisect
import heapq
import math
from typing import List

"""668. 乘法表中第 K 小的数
几乎每一个人都用乘法表。
但是你能在乘法表中快速找到第 k 小的数字吗？
乘法表是大小为 m x n 的一个整数矩阵，其中mat[i][j] == i * j（下标从 1 开始）。
给你三个整数 m、n 和 k，请你在大小为m x n 的乘法表中，找出并返回第 k小的数字。
示例 1：
输入：m = 3, n = 3, k = 5
输出：3
解释：第 5 小的数字是 3 。
示例 2：
输入：m = 2, n = 3, k = 6
输出：6
解释：第 6 小的数字是 6 。
提示：
	1 <= m, n <= 3 * 10^4
	1 <= k <= m * n
https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(x):
            cnt = 0
            # 计数，遍历每行，用x//i计算每行小于等于x的数，但这个数不会大于n
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt >= k

        left, right = 0, m * n
        # 二分答案
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# s = Solution()
# r = s.findKthNumber(m = 3, n = 3, k = 5)
# r = s.findKthNumber(m = 45, n = 12, k = 471)
# r = s.findKthNumber(m = 1, n = 3, k = 2)
"""378. 有序矩阵中第 K 小的元素

给你一个n x n矩阵matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
你必须找到一个内存复杂度优于O(n2) 的解决方案。
示例 1：
输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
示例 2：
输入：matrix = [[-5]], k = 1
输出：-5
提示：
	n == matrix.length
	n == matrix[i].length
	1 <= n <= 300
	-10^9 <= matrix[i][j] <= 10^9
	题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
	1 <= k <= n2
进阶：
	你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
	你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（this paper）很有趣。
https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/description/"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(m):
            # 计数，每行小于等于m的值计数
            cnt = 0
            for i in range(n):
                c = min(bisect.bisect_left(matrix[i], m+1), n)
                cnt += c
            return cnt >= k  # 计数大于等于k说明当前值符合

        # 二分答案
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(m):
            i, j = 0, n - 1
            cnt = 0
            while i < n and j >= 0:
                if matrix[i][j] <= m:
                    cnt += j + 1
                    i += 1
                else:
                    j -= 1
            return cnt >= k  # 计数大于等于k说明当前值符合

        # 二分答案
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# s = Solution()
# s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8)
"""719. 找出第 K 小的数对距离
数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。
示例 1：
输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0 。
示例 2：
输入：nums = [1,1,1], k = 2
输出：0
示例 3：
输入：nums = [1,6,1], k = 3
输出：5
提示：
	n == nums.length
	2 <= n <= 10^4
	0 <= nums[i] <= 10^6
	1 <= k <= n * (n - 1) / 2
https://leetcode.cn/problems/find-k-th-smallest-pair-distance/description/"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def check(m):
            cnt = 0
            for i in range(n):
                j = bisect.bisect_left(nums, m + 1, lo=i+1, key=lambda x: x - nums[i])
                cnt += j - (i + 1)
            return cnt >= k

        # 二分上下界
        left, right = 0, nums[-1] - nums[0]
        # 二分答案
        while left <= right:
            mid = (left + right) // 2
            # 如果有大于等于k个值比当前值小，则减小，否则增大
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def check(m):
            # 用双指针代替二分
            cnt = j = 0
            # 双指针求绝对差值小于等于m的数对数目
            for i in range(n):
                while j < n and nums[j] - nums[i] <= m:
                    j += 1
                cnt += j - (i + 1)
            return cnt >= k

        # 二分上下界
        left, right = 0, nums[-1] - nums[0]
        # 二分答案
        while left <= right:
            mid = (left + right) // 2
            # 如果有大于等于k个值比当前值小，则减小，否则增大
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# s = Solution()
# s.smallestDistancePair(nums = [1,6,1], k = 3)
# s.smallestDistancePair(nums = [1,3,1], k = 1)
"""878. 第 N 个神奇数字 1897
一个正整数如果能被 a 或 b 整除，那么它是神奇的。
给定三个整数 n ,a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案对10^9+ 7 取模后的值。
示例 1：
输入：n = 1, a = 2, b = 3
输出：2
示例2：
输入：n = 4, a = 2, b = 3
输出：6
提示：
	1 <= n <= 10^9
	2 <= a, b <= 4 * 10^4
https://leetcode.cn/problems/nth-magical-number/"""

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7
        lcm = math.lcm(a, b)
        def check(m):
            # 有多少个数字被a整除，就有多少个神奇数字，因为a，b的神奇数字会有重复，所以减去最小公倍数的神奇数字
            return m // a + m // b - m // lcm >= n

        left, right = min(a, b), min(a, b) * n
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left % mod

# s = Solution()
# s.nthMagicalNumber(n = 4, a = 2, b = 3)
"""1201. 丑数 III 2039
丑数是可以被a或b或 c整除的 正整数 。
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第n个丑数。
示例 1：
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：
输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：
输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
提示：
	1 <= n, a, b, c <= 10^9
	1 <= a * b * c <= 10^18
	本题结果在[1,2 * 10^9]的范围内
https://leetcode.cn/problems/ugly-number-iii/description/
"""

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm1, lcm2, lcm3 = math.lcm(a, b), math.lcm(b, c), math.lcm(a, c)
        lcm = math.lcm(a, b, c)

        # 容斥原理
        def check(m):
            return (m // a + m // b + m // c - m // lcm1 - m // lcm2 - m // lcm3 + m // lcm) >= n

        left, right = 1, min(a, b, c) * n
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# s = Solution()
# s.nthUglyNumber(n = 3, a = 2, b = 3, c = 5)
"""793. 阶乘函数后 K 个零 2100
f(x)是x!末尾是 0 的数量。
回想一下x! = 1 * 2 * 3 * ... * x，且 0! = 1。
	例如，f(3) = 0，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2，因为 11!= 39916800 末端有 2 个 0 。
给定k，找出返回能满足 f(x) = k的非负整数 x的数量。
示例 1： 
输入：k = 0
输出：5
解释：0!, 1!, 2!, 3!, 和 4!均符合 k = 0 的条件。
示例 2：
输入：k = 5
输出：0
解释：没有匹配到这样的 x!，符合 k = 5 的条件。
示例 3:
输入: k = 3
输出: 5
提示:
	0 <= k <= 10^9
https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/
"""

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def check(m):
            # 阶乘后的0的数量
            cnt = 0
            while m:
                m //= 5
                cnt += m
            return cnt
        # 二分上下界，因为每5个数必有一个0，所以上界可以是k*5
        left, right = 1, k * 5
        while left <= right:
            mid = (left + right) // 2
            if check(mid) >= k:
                right = mid - 1
            else:
                left = mid + 1
        # 不是5就是0,因为每5个数阶乘就会多0，只要相等就是5否则是0
        return 5 if check(left) == k else 0

# s = Solution()
# s.preimageSizeFZF(k = 5)
"""373. 查找和最小的 K 对数字
给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2,以及一个整数 k。
定义一对值(u,v)，其中第一个元素来自nums1，第二个元素来自 nums2。
请找到和最小的 k个数对(u1,v1), (u2,v2) ... (uk,vk)。
示例 1:
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
    [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
提示:
	1 <= nums1.length, nums2.length <= 10^5
	-10^9 <= nums1[i], nums2[i] <= 10^9
	nums1 和 nums2 均为 升序排列
	1 <= k <= 10^4
	k <=nums1.length *nums2.length
https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(len(nums1), k))]
        for _ in range(k):
            __, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        for _ in range(k):
            __, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            if j == 0 and i < len(nums1) - 1:
                heapq.heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j < len(nums2) - 1:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


# s = Solution()
# s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)


# TODO
"""1439. 有序矩阵中的第 k 个最小数组和 2134
786. 第 K 个最小的质数分数 2169
3116. 单面值组合的第 K 小金额 2387
3134. 找出唯一性数组的中位数 2451
2040. 两个有序数组的第 K 小乘积 2518
2386. 找出数组的第 K 大和 2648 转化
1508. 子数组和排序后的区间和 思考：二分做法"""































