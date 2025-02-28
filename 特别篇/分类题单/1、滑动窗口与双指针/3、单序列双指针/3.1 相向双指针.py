#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3.1 相向双指针.py
# @Author  ：Lin
# @Date    ：2024/11/13 16:45

"""§3.1 相向双指针
两个指针 left=0,right=n−1，从数组的两端开始，向中间移动，这叫相向双指针。
上面的滑动窗口相当于同向双指针。
344. 反转字符串
125. 验证回文串
1750. 删除字符串两端相同字符后的最短长度 1502
2105. 给植物浇水 II 1507
977. 有序数组的平方 做到 O(n)
658. 找到 K 个最接近的元素
1471. 数组中的 K 个最强值 用双指针解决
167. 两数之和 II - 输入有序数组
633. 平方数之和
2824. 统计和小于目标的下标对数目
LCP 28. 采购方案 同 2824 题
15. 三数之和
16. 最接近的三数之和
18. 四数之和
611. 有效三角形的个数
1577. 数的平方等于两数乘积的方法数 用双指针实现
923. 三数之和的多种可能 1711
948. 令牌放置 1762
11. 盛最多水的容器
42. 接雨水
1616. 分割两个字符串得到回文串 1868
1498. 满足条件的子序列数目 2276
1782. 统计点对的数目 2457"""
"""两个指针
left=0,right=𝑛−1，从数组的两端开始，向中间移动，这叫相向双指针。
上面的滑动窗口相当于同向双指针。"""
import math
from collections import Counter, deque
from math import isqrt

"""344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
提示：
1 <= s.length <= 105
s[i] 都是 ASCII 码表中的可打印字符"""


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]


"""125. 验证回文串
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
字母和数字都属于字母数字字符。
给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
示例 1：
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
示例 2：
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
示例 3：
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
提示：
1 <= s.length <= 2 * 105
s 仅由可打印的 ASCII 字符组成
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = list(filter(str.isalnum, s.lower()))
        for i in range(len(s)//2):
            if arr[i] != arr[-i-1]:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# s = Solution()
# s.isPalindrome(s = "A man, a plan, a canal: Panama")
"""1750. 删除字符串两端相同字符后的最短长度 1502
给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：
选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
前缀和后缀在字符串中任意位置都不能有交集。
前缀和后缀包含的所有字符都要相同。
同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。
示例 1：
输入：s = "ca"
输出：2
解释：你没法删除任何一个字符，所以字符串长度仍然保持不变。
示例 2：
输入：s = "cabaabac"
输出：0
解释：最优操作序列为：
- 选择前缀 "c" 和后缀 "c" 并删除它们，得到 s = "abaaba" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "baab" 。
- 选择前缀 "b" 和后缀 "b" 并删除它们，得到 s = "aa" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "" 。
示例 3：
输入：s = "aabccabba"
输出：3
解释：最优操作序列为：
- 选择前缀 "aa" 和后缀 "a" 并删除它们，得到 s = "bccabb" 。
- 选择前缀 "b" 和后缀 "bb" 并删除它们，得到 s = "cca" 。
提示：
1 <= s.length <= 105
s 只包含字符 'a'，'b' 和 'c' 。

"""


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        cur = s[0]
        while left < right and s[left] == s[right]:
            while left < right and s[left] == cur:
                left += 1
            while left <= right and s[right] == cur:
                right -= 1
            cur = s[left]
        return right - left + 1


# s = Solution()
# s.minimumLength(s = "cabaabac")
#

"""2105. 给植物浇水 II 1507
Alice 和 Bob 打算给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1 。其中，第 i 株植物的位置是 x = i 。
每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，最初是满的 。他们按下面描述的方式完成浇水：
 Alice 按 从左到右 的顺序给植物浇水，从植物 0 开始。Bob 按 从右到左 的顺序给植物浇水，从植物 n - 1 开始。他们 同时 给植物浇水。
如果没有足够的水 完全 浇灌下一株植物，他 / 她会立即重新灌满浇水罐。
不管植物需要多少水，浇水所耗费的时间都是一样的。
不能 提前重新灌满水罐。
每株植物都可以由 Alice 或者 Bob 来浇水。
如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。
给你一个下标从 0 开始的整数数组 plants ，数组由 n 个整数组成。其中，plants[i] 为第 i 株植物需要的水量。另有两个整数 capacityA 和 capacityB 分别表示 Alice 和 Bob 水罐的容量。返回两人浇灌所有植物过程中重新灌满水罐的 次数 。
示例 1：
输入：plants = [2,2,3,3], capacityA = 5, capacityB = 5
输出：1
解释：
- 最初，Alice 和 Bob 的水罐中各有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 2 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 2 ，所以他先重新装满水，再浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 0 = 1 。
示例 2：
输入：plants = [2,2,3,3], capacityA = 3, capacityB = 4
输出：2
解释：
- 最初，Alice 的水罐中有 3 单元水，Bob 的水罐中有 4 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在都只有 1 单元水，并分别需要给植物 1 和植物 2 浇水。
- 由于他们的水量均不足以浇水，所以他们重新灌满水罐再进行浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 1 + 1 + 0 = 2 。
示例 3：
输入：plants = [5], capacityA = 10, capacityB = 8
输出：0
解释：
- 只有一株植物
- Alice 的水罐有 10 单元水，Bob 的水罐有 8 单元水。因此 Alice 的水罐中水更多，她会给这株植物浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 。
提示：

n == plants.length
1 <= n <= 105
1 <= plants[i] <= 106
max(plants[i]) <= capacityA, capacityB <= 109"""
from typing import List


# 模拟
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        a, b = capacityA, capacityB
        left, right = 0, n-1
        res = 0
        while left <= right:
            # 如果两个人到了同一个位置，让剩余水较多的人去浇水
            if left == right:
                if max(a, b) < plants[left]:
                    res += 1
            else:
                # 没有足够的水，需要重新装满水
                if a < plants[left]:
                    res += 1
                    a = capacityA
                if b < plants[right]:
                    res += 1
                    b = capacityB
                a -= plants[left]
                b -= plants[right]
            left += 1
            right -= 1
        return res

# s = Solution()
# s.minimumRefill(plants = [726,739,934,116,643,648,473,984,482,85,850,806,146,764,156,66,186,339,985,237,662,552,800,78,617,933,481,652,796,594,151,82,183,241,525,221,951,732,799,483,368,354,776,175,974,187,913,842]
#                 , capacityA = 1439, capacityB = 1207)


"""977. 有序数组的平方 做到 O(n)
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
提示：
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        res = [0] * n
        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res


# s = Solution()
# s.sortedSquares(nums = [-4,-1,0,3,10])


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
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        return arr[left: right + 1]


# s = Solution()
# s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)
"""1471. 数组中的 K 个最强值 用双指针解决
给你一个整数数组 arr 和一个整数 k 。
设 m 为数组的中位数，只要满足下述两个前提之一，就可以判定 arr[i] 的值比 arr[j] 的值更强：
 |arr[i] - m| > |arr[j] - m|
 |arr[i] - m| == |arr[j] - m|，且 arr[i] > arr[j]
请返回由数组中最强的 k 个值组成的列表。答案可以以 任意顺序 返回。
中位数 是一个有序整数列表中处于中间位置的值。形式上，如果列表的长度为 n ，那么中位数就是该有序列表（下标从 0 开始）中位于 ((n - 1) / 2) 的元素。
例如 arr = [6, -3, 7, 2, 11]，n = 5：数组排序后得到 arr = [-3, 2, 6, 7, 11] ，数组的中间位置为 m = ((5 - 1) / 2) = 2 ，中位数 arr[m] 的值为 6 。
例如 arr = [-7, 22, 17, 3]，n = 4：数组排序后得到 arr = [-7, 3, 17, 22] ，数组的中间位置为 m = ((4 - 1) / 2) = 1 ，中位数 arr[m] 的值为 3 。
示例 1：
输入：arr = [1,2,3,4,5], k = 2
输出：[5,1]
解释：中位数为 3，按从强到弱顺序排序后，数组变为 [5,1,4,2,3]。最强的两个元素是 [5, 1]。[1, 5] 也是正确答案。
注意，尽管 |5 - 3| == |1 - 3| ，但是 5 比 1 更强，因为 5 > 1 。
示例 2：
输入：arr = [1,1,3,5,5], k = 2
输出：[5,5]
解释：中位数为 3, 按从强到弱顺序排序后，数组变为 [5,5,1,1,3]。最强的两个元素是 [5, 5]。
示例 3：
输入：arr = [6,7,11,7,6,8], k = 5
输出：[11,8,6,6,7]
解释：中位数为 7, 按从强到弱顺序排序后，数组变为 [11,8,6,6,7,7]。
[11,8,6,6,7] 的任何排列都是正确答案。
示例 4：
输入：arr = [6,-3,7,2,11], k = 3
输出：[-3,11,2]
示例 5：
输入：arr = [-7,22,17,3], k = 2
输出：[22,17]
提示：
1 <= arr.length <= 10^5
-10^5 <= arr[i] <= 10^5
1 <= k <= arr.length
"""


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        mid = arr[(n-1)//2]
        res = []
        left, right = 0, n-1
        for i in range(k):
            if arr[right] - mid >= mid - arr[left]:
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
        return res
# s = Solution()
# s.getStrongest(arr = [6,7,11,7,6,8], k = 5)

"""167. 两数之和 II - 输入有序数组
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

 
示例 1：

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
示例 3：

输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
 

提示：

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 非递减顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


"""633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：
输入：c = 3
输出：false
提示：
0 <= c <= 231 - 1"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a * 2 <= c:
            b = isqrt(c - a * a)
            if a * a + b * b == c:
                return True
            a += 1
        return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        while a <= b:
            if a * a + b * b == c:
                return True
            elif a * a + b * b > c:
                b -= 1
            else:
                a += 1
        return False


# s = Solution()
# s.judgeSquareSum(1000)

"""2824. 统计和小于目标的下标对数目
给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。
示例 1：
输入：nums = [-1,1,2,3,1], target = 2
输出：3
解释：总共有 3 个下标对满足题目描述：
- (0, 1) ，0 < 1 且 nums[0] + nums[1] = 0 < target
- (0, 2) ，0 < 2 且 nums[0] + nums[2] = 1 < target 
- (0, 4) ，0 < 4 且 nums[0] + nums[4] = 0 < target
注意 (0, 3) 不计入答案因为 nums[0] + nums[3] 不是严格小于 target 。
示例 2：
输入：nums = [-6,2,5,-2,-7,-1,3], target = -2
输出：10
解释：总共有 10 个下标对满足题目描述：
- (0, 1) ，0 < 1 且 nums[0] + nums[1] = -4 < target
- (0, 3) ，0 < 3 且 nums[0] + nums[3] = -8 < target
- (0, 4) ，0 < 4 且 nums[0] + nums[4] = -13 < target
- (0, 5) ，0 < 5 且 nums[0] + nums[5] = -7 < target
- (0, 6) ，0 < 6 且 nums[0] + nums[6] = -3 < target
- (1, 4) ，1 < 4 且 nums[1] + nums[4] = -5 < target
- (3, 4) ，3 < 4 且 nums[3] + nums[4] = -9 < target
- (3, 5) ，3 < 5 且 nums[3] + nums[5] = -3 < target
- (4, 5) ，4 < 5 且 nums[4] + nums[5] = -8 < target
- (4, 6) ，4 < 6 且 nums[4] + nums[6] = -4 < target
提示：
1 <= nums.length == n <= 50
-50 <= nums[i], target <= 50
"""


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        res = 0
        while left < right:
            while left < right and nums[left] + nums[right] >= target:
                right -= 1
            res += right - left
            left += 1
        return res

# s = Solution()
# s.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)

"""LCP 28. 采购方案 同 2824 题
小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
示例 1：
输入：nums = [2,5,3,5], target = 6
输出：1
解释：预算内仅能购买 nums[0] 与 nums[2]。
示例 2：
输入：nums = [2,2,1,9], target = 10
输出：4
解释：符合预算的采购方案如下： nums[0] + nums[1] = 4 nums[0] + nums[2] = 3 nums[1] + nums[2] = 3 nums[2] + nums[3] = 10
提示：
2 <= nums.length <= 10^5
1 <= nums[i], target <= 10^5
"""

class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        res = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)

# s = Solution()
# s.purchasePlans(nums = [2,2,1,9], target = 10)

"""15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
提示：
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
# TODO 优化策略
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return res

# s = Solution()
# s.threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4])

"""16. 最接近的三数之和
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：
输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = sum(nums[:3])
        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return res
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return res


# s = Solution()
# s.threeSumClosest(nums = [0,1,2], target = 0)

"""18. 四数之和
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
提示：
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
# TODO 优化策略
"""设 s=nums[a]+nums[a+1]+nums[a+2]+nums[a+3]。如果 s>target，由于数组已经排序，
后面无论怎么选，选出的四个数的和不会比 s 还小，所以后面不会找到等于 target 的四数之和了。
所以只要 s>target，就可以直接 break 外层循环了。
设 s=nums[a]+nums[n−3]+nums[n−2]+nums[n−1]。如果 s<target，由于数组已经排序，
nums[a] 加上后面任意三个数都不会超过 s，
所以无法在后面找到另外三个数与 nums[a] 相加等于 target。
但是后面还有更大的 nums[a]，可能出现四数之和等于 target 的情况，所以还需要继续枚举，
continue 外层循环。
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            # 重复值跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n - 2):
                # 重复值跳过
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    # 重复值跳过
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
        return res


# s = Solution()
# s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)

"""611. 有效三角形的个数
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
示例 1:
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
示例 2:
输入: nums = [4,2,3,4]
输出: 4
提示:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            k = i + 1
            for j in range(i + 1, n):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += max(k - j - 1, 0)
        return res

# s = Solution()
# s.triangleNumber(nums = [4,2,3,4])

"""1577. 数的平方等于两数乘积的方法数 用双指针实现
给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：
类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length
示例 1：
输入：nums1 = [7,4], nums2 = [5,2,8,9]
输出：1
解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)
示例 2：
输入：nums1 = [1,1], nums2 = [1,1,1]
输出：9
解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k]
类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]
示例 3：
输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
输出：2
解释：有两个符合题目要求的三元组
类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]
示例 4：
输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
输出：0
解释：不存在符合题目要求的三元组
提示：
1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5
"""


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # 哈希次数
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        # 去重排序
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        res = 0
        m, n = len(nums1), len(nums2)
        # 双指针
        for i in range(m):
            left, right = 0, n - 1
            while left <= right:

                if nums1[i] ** 2 == nums2[left] * nums2[right]:
                    if left == right:
                        res += cnt2[nums2[left]] * (cnt2[nums2[left]] - 1) // 2 * cnt1[nums1[i]]
                    else:
                        res += cnt2[nums2[left]] * cnt2[nums2[right]] * cnt1[nums1[i]]
                    left += 1
                    right -= 1
                elif nums1[i] ** 2 > nums2[left] * nums2[right]:
                    left += 1
                else:
                    right -= 1
        for i in range(n):
            left, right = 0, m - 1
            while left <= right:
                if nums2[i] ** 2 == nums1[left] * nums1[right]:
                    if left == right:
                        res += cnt1[nums1[left]] * (cnt1[nums1[left]] - 1) // 2 * cnt2[nums2[i]]
                    else:
                        res += cnt1[nums1[left]] * cnt1[nums1[right]] * cnt2[nums2[i]]
                    left += 1
                    right -= 1
                elif nums2[i] ** 2 > nums1[left] * nums1[right]:
                    left += 1
                else:
                    right -= 1
        return res


# s = Solution()
# s.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9])
"""923. 三数之和的多种可能 1711
给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。
由于结果会非常大，请返回 109 + 7 的模。
示例 1：
输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：
输入：arr = [1,1,2,2,2,2], target = 5
输出：12
解释：
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
提示：
3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = Counter(arr)
        arr = sorted(list(set(arr)))
        n = len(arr)
        res = 0
        # 遍历i
        for i in range(n):
            # 因为是去重的数组，所以下标可能重合
            left, right = i, n-1
            while left <= right:
                # 三数之和
                s = arr[i] + arr[left] + arr[right]
                # 三数之和 太大右指针左移，太小左指针右移
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:  # 三数之和等于目标值
                    if i == right:  # 三个指针相等
                        res += math.comb(cnt[arr[i]], 3)
                    elif i == left:  # 前两个指针相等
                        res += math.comb(cnt[arr[i]], 2) * cnt[arr[right]]
                    elif left == right:  # 后两个指针相等
                        res += math.comb(cnt[arr[left]], 2) * cnt[arr[i]]
                    else:  # 三个指针都不相等
                        res += cnt[arr[i]] * cnt[arr[left]] * cnt[arr[right]]
                    left += 1
                    right -= 1
        return res % (10 ** 9 + 7)


# s = Solution()
# s.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8)

"""948. 令牌放置 1762
你的初始 能量 为 power，初始 分数 为 0，只有一包令牌以整数数组 tokens 给出。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。

你的目标是通过有策略地使用这些令牌以 最大化 总 分数。在一次行动中，你可以用两种方式中的一种来使用一个 未被使用的 令牌（但不是对同一个令牌使用两种方式）：

朝上：如果你当前 至少 有 tokens[i] 点 能量 ，可以使用令牌 i ，失去 tokens[i] 点 能量 ，并得到 1 分 。
朝下：如果你当前至少有 1 分 ，可以使用令牌 i ，获得 tokens[i] 点 能量 ，并失去 1 分 。
在使用 任意 数量的令牌后，返回我们可以得到的最大 分数 。
示例 1：
输入：tokens = [100], power = 50
输出：0
解释：因为你的初始分数为 0，无法使令牌朝下。你也不能使令牌朝上因为你的能量（50）比 tokens[0] 少（100）。
示例 2：
输入：tokens = [200,100], power = 150
输出：1
解释：使令牌 1 正面朝上，能量变为 50，分数变为 1 。
不必使用令牌 0，因为你无法使用它来提高分数。可得到的最大分数是 1。
示例 3：
输入：tokens = [100,200,300,400], power = 200
输出：2
解释：按下面顺序使用令牌可以得到 2 分：
1. 令牌 0 (100)正面朝上，能量变为 100 ，分数变为 1
2. 令牌 3 (400)正面朝下，能量变为 500 ，分数变为 0
3. 令牌 1 (200)正面朝上，能量变为 300 ，分数变为 1
4. 令牌 2 (300)正面朝上，能量变为 0 ，分数变为 2
可得的最大分数是 2。
提示：
0 <= tokens.length <= 1000
0 <= tokens[i], power < 104
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # 排序
        res = score = 0
        n = len(tokens)
        # 左右指针
        left, right = 0, n - 1
        while left <= right:
            # 如果能量充足，优先去得到分数
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                res = max(res, score)
                left += 1
            else:
                # 能量不足且分数不够时直接返回
                if score == 0:
                    return res
                score -= 1
                power += tokens[right]
                right -= 1
        return res


s = Solution()
s.bagOfTokensScore(tokens = [100,200,300,400], power = 200)


"""11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：
输入：height = [1,1]
输出：1
提示：
n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res

"""42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = [height[0]] * n, [height[-1]] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1])
        return sum([min(left_max[i], right_max[i]) - height[i] for i in range(n)])


# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        deq = deque()
        res = 0
        for i, h in enumerate(height):
            print(deq, res)
            while deq and h > height[deq[-1]]:
                top = deq.pop()
                if not deq:
                    break
                left = deq[-1]
                cur_width = i - left - 1
                res += (min(height[left], h) - height[top]) * cur_width
            deq.append(i)
        return res

# 双指针
"""方法三：双指针
动态规划的做法中，需要维护两个数组 leftMax 和 rightMax，因此空间复杂度是 O(n)。
是否可以将空间复杂度降到 O(1)？

注意到下标 i 处能接的雨水量由 leftMax[i] 和 rightMax[i] 中的最小值决定。
由于数组 leftMax 是从左往右计算，数组 rightMax 是从右往左计算，因此可以使用双指针和两个变量代替两个数组。

维护两个指针 left 和 right，以及两个变量 leftMax 和 rightMax，初始时 left=0,right=n−1,leftMax=0,rightMax=0。指针 left 只会向右移动，指针 right 只会向左移动，在移动指针的过程中维护两个变量 leftMax 和 rightMax 的值。

当两个指针没有相遇时，进行如下操作：

使用 height[left] 和 height[right] 的值更新 leftMax 和 rightMax 的值；

如果 height[left]<height[right]，则必有 leftMax<rightMax，下标 left 处能接的雨水量等于 leftMax−height[left]，将下标 left 处能接的雨水量加到能接的雨水总量，然后将 left 加 1（即向右移动一位）；

如果 height[left]≥height[right]，则必有 leftMax≥rightMax，下标 right 处能接的雨水量等于 rightMax−height[right]，将下标 right 处能接的雨水量加到能接的雨水总量，然后将 right 减 1（即向左移动一位）。
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        while left <= right:
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res


# s = Solution()
# s.trap(height = [4,2,0,3,2,5])

"""1616. 分割两个字符串得到回文串 1868
给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。
当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
注意， x + y 表示连接字符串 x 和 y 。
示例 1：
输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。
示例 2：
输入：a = "xbdef", b = "xecab"
输出：false
示例 3：
输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
提示：
1 <= a.length, b.length <= 105
a.length == b.length
a 和 b 都只包含小写英文字母
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # 如果 a_prefix + b_suffix 可以构成回文串则返回 True，否则返回 False
        def check(a, b):
            left, right = 0, len(a) - 1  # 相向双指针
            while left < right:
                if a[left] != b[right]:
                    # 中间剩余部分 判断是否为回文串
                    return a[left:right+1] == a[left:right+1][::-1] or b[left:right+1] == b[left:right+1][::-1]

                left += 1
                right -= 1
            return True
        return check(a, b) or check(b, a)


# s = Solution()
# s.checkPalindromeFormation(a = "ulacfd", b = "jizalu")

# r = s.checkPalindromeFormation(a = "abdef", b = "fecab")
# r = s.checkPalindromeFormation(a = "pvhmupgqeltozftlmfjjde", b = "yjgpzbezspnnpszebzmhvp")

"""1498. 满足条件的子序列数目 2276
给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 109 + 7 取余后返回。
示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
示例 2：
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
示例 3：
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            res += 2 ** (right - left) % (10 ** 9 + 7)
            left += 1
        return res % (10 ** 9 + 7)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        f = [1] + [0] * (n - 1)  # 2的i次方数组
        p = 10 ** 9 + 7
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % p   # 2的i次方

        left, right = 0, n - 1
        res = 0
        # 双指针
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            res += f[right - left]
            left += 1
        return res % (10 ** 9 + 7)


# s = Solution()
# s.numSubseq(nums = [3,5,6,7], target = 9)




























































































































































































































