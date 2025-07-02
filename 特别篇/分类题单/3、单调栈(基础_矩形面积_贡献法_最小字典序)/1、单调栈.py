#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/5 17:07
# @Author  : Lin
# @File    : 1、单调栈.py
"""1.1 基础"""
from collections import deque
from itertools import accumulate
from typing import List, Optional

"""
739. 每日温度 模板题
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
提示：
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        deq = []
        for i in range(n-1, -1, -1):
            while deq and temperatures[i] >= temperatures[deq[-1]]:
                deq.pop()
            if deq:
                ans[i] = deq[-1] - i
            deq.append(i)
        return ans

# 从前往后
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        deq = []
        for i in range(n):
            while deq and temperatures[i] > temperatures[deq[-1]]:
                j = deq.pop()
                ans[j] = i - j
            deq.append(i)
        return ans
"""1475. 商品折扣后的最终价格 非暴力做法
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
示例 1：
输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
示例 2：
输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。
示例 3：
输入：prices = [10,1,1,6]
输出：[9,0,1,6]
提示：
1 <= prices.length <= 500
1 <= prices[i] <= 10^3"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = []
        ans = prices[::]
        for i in range(n-1,-1,-1):
            while st and prices[i] < prices[st[-1]]:
                st.pop()
            if st:
                ans[i] -= prices[st[-1]]
            st.append(i)
        return ans

# s = Solution()
# s.finalPrices(prices = [8,7,4,2,8,1,7,7,10,1])

"""496. 下一个更大元素 I
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
示例 1：
输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：
输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
提示：
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中
进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []
        # 单调栈，把下一个更大元素下标存在栈中，因为不存在重复元素，所以可以用哈希保存答案
        for i in range(len(nums2)-1, - 1, -1):
            while stack and nums2[stack[-1]] < nums2[i]:
                stack.pop()
            mp[nums2[i]] = nums2[stack[-1]] if stack else -1
            stack.append(i)

        return [mp[x] for x in nums1]
# s = Solution()
# s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
"""503. 下一个更大元素 II
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
示例 1:
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
示例 2:
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
提示:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 最大值和最大值下标
        max_val, max_idx = -(10**9+1), 0
        for i, x in enumerate(nums):
            if max_val < x:
                max_val = x
                max_idx = i
        n = len(nums)
        # 单调栈
        stack = []
        ans = [-1] * n  # 结果集
        # 从最大值下标开始倒序遍历
        for i in range(max_idx+n, max_idx, -1):
            i = i % n
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = nums[stack[-1]]
            stack.append(i)
        return ans

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 单调栈
        stack = []
        ans = [-1] * n  # 结果集
        # 从最大值下标开始倒序遍历
        for i in range(n * 2 - 1, -1, -1):
            i = i % n
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = nums[stack[-1]]
            stack.append(i)
        return ans
# s = Solution()
# s.nextGreaterElements(nums = [-1, 0])
"""901. 股票价格跨度 1709
设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。
当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
实现 StockSpanner 类：
StockSpanner() 初始化类对象。
int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。
示例：
输入：
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
输出：
[null, 1, 1, 1, 2, 1, 4, 6]
解释：
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // 返回 1
stockSpanner.next(80);  // 返回 1
stockSpanner.next(60);  // 返回 1
stockSpanner.next(70);  // 返回 2
stockSpanner.next(60);  // 返回 1
stockSpanner.next(75);  // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
stockSpanner.next(85);  // 返回 6
提示：
1 <= price <= 105
最多调用 next 方法 104 次
"""

class StockSpanner:
    def __init__(self):
        self.stack = []  # 初始化栈

    def next(self, price: int) -> int:
        i = 1
        # 如果存在栈且栈顶元素小于等于当前值
        while self.stack and self.stack[-1][0] <= price:
            i += self.stack[-1][1]  # 把栈顶的跨度都加给当前值
            self.stack.pop()  # 推出栈顶元素
        self.stack.append([price, i])
        return i
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
"""853. 车队
在一条单行道上，有 n 辆车开往同一目的地。目的地是几英里以外的 target 。
给定两个整数数组 position 和 speed ，长度都是 n ，其中 position[i] 是第 i 辆车的位置， speed[i] 是第 i 辆车的速度(单位是英里/小时)。
一辆车永远不会超过前面的另一辆车，但它可以追上去，并以较慢车的速度在另一辆车旁边行驶。
车队 是指并排行驶的一辆或几辆汽车。车队的速度是车队中 最慢 的车的速度。
即便一辆车在 target 才赶上了一个车队，它们仍然会被视作是同一个车队。
返回到达目的地的车队数量 。
示例 1：
输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
输出：3
解释：
从 10（速度为 2）和 8（速度为 4）开始的车会组成一个车队，它们在 12 相遇。车队在 target 形成。
从 0（速度为 1）开始的车不会追上其它任何车，所以它自己是一个车队。
从 5（速度为 1） 和 3（速度为 3）开始的车组成一个车队，在 6 相遇。车队以速度 1 移动直到它到达 target。
示例 2：
输入：target = 10, position = [3], speed = [3]
输出：1
解释：
只有一辆车，因此只有一个车队。
示例 3：
输入：target = 100, position = [0,2,4], speed = [4,2,1]
输出：1
解释：
从 0（速度为 4） 和 2（速度为 2）开始的车组成一个车队，在 4 相遇。从 4 开始的车（速度为 1）移动到了 5。
然后，在 4（速度为 2）的车队和在 5（速度为 1）的车成为一个车队，在 6 相遇。车队以速度 1 移动直到它到达 target。
提示：
n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
position 中每个值都 不同
0 < speed[i] <= 106
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 排序
        nums = sorted([(x, y) for x, y in zip(position, speed)], reverse=True)
        ans = 0
        stack = []
        for x, y in nums:
            if stack:
                # 如果能在target前追上栈顶车，则可以组成一个车队，如果不能追上，则栈顶的车队的车都已经遍历完成，重新再加一个车队，
                x1, y1 = stack[-1]
                if ((target - x) / y) > ((target - x1) / y1):
                    stack.pop()
            if not stack:
                ans += 1
                stack.append((x, y))
        return ans

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 排序
        cars = sorted([(x, y) for x, y in zip(position, speed)], reverse=True)
        times = [(target - x) / y for x, y in cars]
        ans = pre = 0
        for t in times:
            # 如果能在target前追上栈顶车，则可以组成一个车队，如果不能追上，则栈顶的车队的车都已经遍历完成，重新再加一个车队，
            if t > pre:
                ans += 1
                pre = t
        return ans
# s = Solution()
# s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])

"""1.2 进阶（选做）
1019. 链表中的下一个更大节点 1571
给定一个长度为 n 的链表 head
对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。
示例 1：
输入：head = [2,1,5]
输出：[5,5,0]
示例 2：
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]
提示：
链表中节点数为 n
1 <= n <= 104
1 <= Node.val <= 109"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack, i = [], -1
        while head:
            i += 1
            while stack and head.val > stack[-1][0]:
                x, y = stack.pop()
                ans[y] = head.val
            stack.append((head.val, i))
            ans.append(0)
            head = head.next
        return ans


# stack只保留下标
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack, i = [], -1
        while head:
            i += 1
            while stack and head.val > ans[stack[-1]]:
                ans[stack.pop()] = head.val
            stack.append(i)
            ans.append(head.val)
            head = head.next
        for i in stack:
            ans[i] = 0
        return ans


"""思维扩展：
962. 最大宽度坡 1608
给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
找出 A 中的坡的最大宽度，如果不存在，返回 0 。
示例 1：
输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：
输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
提示：
2 <= A.length <= 50000
0 <= A[i] <= 50000
"""

"""
思路，先遍历nums，预处理出一个递减的单调栈，
然后再逆向遍历
"""
# 时间复杂度O(n)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # 先遍历nums，预处理出一个递减的单调栈，
        for i, x in enumerate(nums):
            while not stack or nums[stack[-1]] > x:
                stack.append(i)
        ans = 0
        for i in range(len(nums)-1, 0, -1):
            x = nums[i]
            # 逆向遍历，大于栈顶的元素可能就是所需要的下标对
            while stack and nums[stack[-1]] <= x:
                j = stack.pop()
                ans = max(ans, i - j)
        return ans
# s = Solution()
# s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1])
"""3542. 将所有元素变为 0 的最少操作次数 ~1900
给你一个大小为 n 的 非负 整数数组 nums 。你的任务是对该数组执行若干次（可能为 0 次）操作，使得 所有 元素都变为 0。
在一次操作中，你可以选择一个子数组 [i, j]（其中 0 <= i <= j < n），将该子数组中所有 最小的非负整数 的设为 0。
返回使整个数组变为 0 所需的最少操作次数。
一个 子数组 是数组中的一段连续元素。
示例 1：
输入: nums = [0,2]
输出: 1
解释:
选择子数组 [1,1]（即 [2]），其中最小的非负整数是 2。将所有 2 设为 0，结果为 [0,0]。
因此，所需的最少操作次数为 1。
示例 2：
输入: nums = [3,1,2,1] 
输出: 3
解释:
选择子数组 [1,3]（即 [1,2,1]），最小非负整数是 1。将所有 1 设为 0，结果为 [3,0,2,0]。
选择子数组 [2,2]（即 [2]），将 2 设为 0，结果为 [3,0,0,0]。
选择子数组 [0,0]（即 [3]），将 3 设为 0，结果为 [0,0,0,0]。
因此，最少操作次数为 3。
示例 3：
输入: nums = [1,2,1,2,1,2]
输出: 4
解释:
选择子数组 [0,5]（即 [1,2,1,2,1,2]），最小非负整数是 1。将所有 1 设为 0，结果为 [0,2,0,2,0,2]。
选择子数组 [1,1]（即 [2]），将 2 设为 0，结果为 [0,0,0,2,0,2]。
选择子数组 [3,3]（即 [2]），将 2 设为 0，结果为 [0,0,0,0,0,2]。
选择子数组 [5,5]（即 [2]），将 2 设为 0，结果为 [0,0,0,0,0,0]。
因此，最少操作次数为 4。
提示:
1 <= n == nums.length <= 105
0 <= nums[i] <= 105"""

"""一个子数组内，所有的最小值可以一次性变为0"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for x in nums:
            while stack and stack[-1] > x:
                ans += 1
                stack.pop()
            if not stack or stack[-1] != x:
                stack.append(x)
        return ans + len(stack) - (stack[0] == 0)

# s = Solution()
# s.minOperations(nums = [1,0])
"""1124. 表现良好的最长时间段 1908
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
请你返回「表现良好时间段」的最大长度。
示例 1：
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
示例 2：
输入：hours = [6,6,6]
输出：0
提示：
1 <= hours.length <= 104
0 <= hours[i] <= 16
"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        pre = [0] * (n + 1)  # 前缀和
        stack = [0]
        # 先遍历nums，预处理出一个递减的单调栈，
        for i, x in enumerate(hours, 1):
            pre[i] = pre[i-1] + (1 if x > 8 else -1)
            while pre[stack[-1]] > pre[i]:
                stack.append(i)
        ans = 0
        for i in range(n, 0, -1):
            # 逆向遍历，大于栈顶的元素可能就是所需要的下标对
            while stack and pre[stack[-1]] < pre[i]:
                j = stack.pop()
                ans = max(ans, i - j)   # [st[-1],i) 可能是最长子数组
        return ans
s = Solution()
s.longestWPI(hours = [9,9,6,0,6,6,9])
# s.longestWPI(hours = [6,9,9])
