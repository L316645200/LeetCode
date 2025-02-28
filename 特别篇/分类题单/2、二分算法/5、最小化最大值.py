#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：5、最小化最大值.py
# @Author  ：Lin
# @Date    ：2025/1/23 16:22
"""本质是二分答案求最小。二分的 mid 表示上界。"""
from collections import deque
from math import lcm
from typing import List

"""410. 分割数组的最大值
给定一个非负整数数组 nums 和一个整数k ，你需要将这个数组分成k个非空的连续子数组，使得这k个子数组各自和的最大值 最小。
返回分割后最小的和的最大值。
子数组 是数组中连续的部份。
示例 1：
输入：nums = [7,2,5,10,8], k = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
示例 2：
输入：nums = [1,2,3,4,5], k = 2
输出：9
示例 3：
输入：nums = [1,4,4], k = 3
输出：4
提示：
	1 <= nums.length <= 1000
	0 <= nums[i] <= 10^6
	1 <= k <= min(50, nums.length)
https://leetcode.cn/problems/split-array-largest-sum/description/
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 定义一个内部函数 check，用于检查给定的上界 m 是否满足条件
        def check(m):
            # 初始化子数组数量为 1，当前子数组的和为 0
            cnt, cur = 1, 0
            # 遍历数组中的每个元素
            for num in nums:
                # 如果当前子数组的和加上当前元素超过了上界 m
                if cur + num > m:
                    # 则需要增加一个子数组
                    cnt += 1
                    # 并将当前元素作为新子数组的第一个元素
                    cur = num
                else:
                    # 否则将当前元素加入当前子数组
                    cur += num
            # 返回子数组数量是否小于等于 k
            return cnt <= k

        # 初始化二分查找的左右边界
        left, right = max(nums), sum(nums)
        # 当左边界小于等于右边界时，继续二分查找
        while left <= right:
            # 计算中间值
            mid = (left + right) // 2
            # 如果中间值满足条件
            if check(mid):
                # 则缩小右边界
                right = mid - 1
            else:
                # 否则扩大左边界
                left = mid + 1
        # 返回最终的结果，即最小的和的最大值
        return left


# s = Solution()
# s.splitArray(nums = [7,2,5,10,8], k = 2)
"""2064. 分配给商店的最多商品的最小值 1886
给你一个整数n，表示有n间零售商店。
总共有m种产品，每种产品的数目用一个下标从 0开始的整数数组quantities表示，其中quantities[i]表示第i种商品的数目。
你需要将 所有商品分配到零售商店，并遵守这些规则：
	一间商店 至多只能有 一种商品 ，但一间商店拥有的商品数目可以为任意件。
	分配后，每间商店都会被分配一定数目的商品（可能为 0件）。用x表示所有商店中分配商品数目的最大值，你希望 x越小越好。也就是说，你想 最小化分配给任意商店商品数目的 最大值。
请你返回最小的可能的x。
示例 1：
输入：n = 6, quantities = [11,6]
输出：3
解释： 一种最优方案为：
- 11 件种类为 0 的商品被分配到前 4 间商店，分配数目分别为：2，3，3，3 。
- 6 件种类为 1 的商品被分配到另外 2 间商店，分配数目分别为：3，3 。
分配给所有商店的最大商品数目为 max(2, 3, 3, 3, 3, 3) = 3 。
示例 2：
输入：n = 7, quantities = [15,10,10]
输出：5
解释：一种最优方案为：
- 15 件种类为 0 的商品被分配到前 3 间商店，分配数目为：5，5，5 。
- 10 件种类为 1 的商品被分配到接下来 2 间商店，数目为：5，5 。
- 10 件种类为 2 的商品被分配到最后 2 间商店，数目为：5，5 。
分配给所有商店的最大商品数目为 max(5, 5, 5, 5, 5, 5, 5) = 5 。
示例 3：
输入：n = 1, quantities = [100000]
输出：100000
解释：唯一一种最优方案为：
- 所有 100000 件商品 0 都分配到唯一的商店中。
分配给所有商店的最大商品数目为 max(100000) = 100000 。
提示：
	m == quantities.length
	1 <= m <= n <= 10^5
	1 <= quantities[i] <= 10^5
https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/description/
"""

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        left, right = 1, max(quantities)
        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for x in quantities:
                cnt += (x - 1) // mid + 1

            if cnt <= n:
                right = mid - 1
            else:
                left = mid + 1

        return left


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        left, right = 1, max(quantities)
        while left <= right:
            mid = (left + right) // 2
            if sum((x - 1) // mid + 1 for x in quantities) <= n:
                right = mid - 1
            else:
                left = mid + 1

        return left


# s = Solution()
# s.minimizedMaximum(n = 7, quantities = [15,10,10])
"""1760. 袋子里最少数目的球 1940
给你一个整数数组nums，其中nums[i]表示第i个袋子里球的数目。
同时给你一个整数maxOperations。
你可以进行如下操作至多maxOperations次：
	选择任意一个袋子，并将袋子里的球分到2 个新的袋子中，每个袋子里都有 正整数个球。
		比方说，一个袋子里有5个球，你可以把它们分到两个新袋子里，分别有 1个和 4个球，或者分别有 2个和 3个球。
你的开销是单个袋子里球数目的 最大值，你想要 最小化开销。
请你返回进行上述操作后的最小开销。
示例 1：
输入：nums = [9], maxOperations = 2
输出：3
解释：
- 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
- 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
示例 2：
输入：nums = [2,4,8,2], maxOperations = 4
输出：2
解释：
- 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
示例 3：
输入：nums = [7,17], maxOperations = 2
输出：7
提示：
	1 <= nums.length <= 10^5
	1 <= maxOperations, nums[i] <= 10^9
https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/description/"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for x in nums:
                cnt += (x - 1) // mid
            if cnt <= maxOperations:
                right = mid - 1
            else:
                left = mid + 1
        return left

# s = Solution()
# s.minimumSize(nums = [431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26],
#               maxOperations = 80)

"""1631. 最小体力消耗路径 1948
你准备参加一场远足活动。
给你一个二维rows x columns的地图heights，其中heights[row][col]表示格子(row, col)的高度。一开始你在最左上角的格子(0, 0)，且你希望去最右下角的格子(rows-1, columns-1)（注意下标从 0 开始编号）。你每次可以往 上，下，左，右四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
一条路径耗费的 体力值是路径上相邻格子之间 高度差绝对值的 最大值决定的。
请你返回从左上角走到右下角的最小体力消耗值。
示例 1：
输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
示例 2：
输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
示例 3：
输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。
提示：
	rows == heights.length
	columns == heights[i].length
	1 <= rows, columns <= 100
	1 <= heights[i][j] <= 10^6
https://leetcode.cn/problems/path-with-minimum-effort/
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        if row == 1 and col == 1:
            return 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def check(m):
            deq = deque([(0, 0)])
            visited = set(deq)
            while deq:
                x, y = deq.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited and abs(heights[x][y] - heights[nx][ny]) <= m:
                        if nx == row - 1 and ny == col - 1:
                            return True
                        visited.add((nx, ny))
                        deq.append((nx, ny))
            return False

        left, right = 0, 10 ** 6
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# s = Solution()
# s.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]])
"""2439. 最小化数组中的最大值 1965
给你一个下标从 0开始的数组nums，它含有n个非负整数。
每一步操作中，你需要：
	选择一个满足1 <= i < n的整数 i，且nums[i] > 0。
	将nums[i]减 1 。
	将nums[i - 1]加 1 。
你可以对数组执行 任意次上述操作，请你返回可以得到的 nums数组中最大值最小 为多少。
示例 1：
输入：nums = [3,7,1,6]
输出：5
解释：
一串最优操作是：
1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。
2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。
3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。
nums 中最大值为 5 。无法得到比 5 更小的最大值。
所以我们返回 5 。
示例 2：
输入：nums = [10,1]
输出：10
解释：
最优解是不改动 nums ，10 是最大值，所以返回 10 。
提示：
	n == nums.length
	2 <= n <= 10^5
	0 <= nums[i] <= 10^9
https://leetcode.cn/problems/minimize-maximum-of-array/description/
"""
# 前缀和 ologn
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            res = max(res, (pre - 1) // (i + 1) + 1)
        return res

# 二分o nlogc
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(m):
            cnt = 0
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > m:
                    cnt += nums[i] - m
                else:
                    cnt = max(0, cnt - m + nums[i])
            return cnt == 0

        left, right = 0, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# s = Solution()
# s.minimizeArrayValue(nums = [3,7,1,6])
"""2560. 打家劫舍 IV 2081
沿街有一排连续的房屋。
每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。
由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。
小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。
给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。
另给你一个整数k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。
返回小偷的 最小 窃取能力。
示例 1：
输入：nums = [2,3,5,9], k = 2
输出：5
解释：
小偷窃取至少 2 间房屋，共有 3 种方式：
- 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
- 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
- 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
因此，返回 min(5, 9, 9) = 5 。
示例 2：
输入：nums = [2,7,9,3,1], k = 2
输出：2
解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。

提示：
	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^9
	1 <= k <= (nums.length + 1)/2
https://leetcode.cn/problems/house-robber-iv/description/
"""

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)
        n = len(nums)
        while left <= right:
            mid = (left + right) // 2
            i = cnt = 0
            while i < n:
                if nums[i] <= mid:
                    cnt += 1
                    i += 1
                i += 1
            if cnt >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

# s = Solution()
# s.minCapability(nums = [2,7,9,3,1], k = 2)
"""778. 水位上升的泳池中游泳 2097 相当于最小化路径最大值
在一个 n x n的整数矩阵grid 中，每一个方格的值 grid[i][j] 表示位置 (i, j) 的平台高度。
当开始下雨时，在时间为t时，水池中的水位为t。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
你从坐标方格的左上平台(0，0) 出发。返回 你到达坐标方格的右下平台(n-1, n-1)所需的最少时间 。
示例 1:
输入: grid = [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例 2:
输入: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释: 最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
提示:
	n == grid.length
	n == grid[i].length
	1 <= n <= 50
	0 <= grid[i][j] <n2
	grid[i][j]中每个值均无重复
https://leetcode.cn/problems/swim-in-rising-water/description/
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def check(m):
            deq = deque([(0, 0)])
            visited = set(deq)
            while deq:
                x, y = deq.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited and grid[nx][ny] <= m:
                        if nx == row - 1 and ny == col - 1:
                            return True
                        visited.add((nx, ny))
                        deq.append((nx, ny))
            return False

        left, right = grid[0][0], 50 * 50
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# s = Solution()
# s.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
"""2616. 最小化数对的最大差值 2155
给你一个下标从 0开始的整数数组nums和一个整数p。
请你从nums中找到p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的最大值最小。同时，你需要确保每个下标在这p个下标对中最多出现一次。
对于一个下标对i和j，这一对的差值为|nums[i] - nums[j]|，其中|x|表示 x的 绝对值。
请你返回 p个下标对对应数值 最大差值的 最小值。
示例 1：
输入：nums = [10,1,2,7,1,3], p = 2
输出：1
解释：第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
示例 2：
输入：nums = [4,2,1,2], p = 1
输出：0
解释：选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
提示：
	1 <= nums.length <= 10^5
	0 <= nums[i] <= 10^9
	0 <= p <= (nums.length)/2
https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/description/
"""

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        left, right = 0, max(nums)
        nums.sort()
        n = len(nums)
        while left <= right:
            mid = (left + right) // 2
            cnt = i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    cnt += 1
                    i += 1
                i += 1
            if cnt >= p:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 定义一个辅助函数 check，用于检查给定的差值 m 是否满足条件
        def check(m):
            # 初始化计数器 cnt 和索引 i
            cnt = i = 0
            # 遍历数组，查找满足条件的下标对
            while i < n - 1:
                # 如果当前元素与下一个元素的差值小于等于 m
                if nums[i + 1] - nums[i] <= m:
                    # 计数器加1
                    cnt += 1
                    # 索引 i 向后移动两位，跳过已经匹配的元素
                    i += 1
                # 索引 i 向后移动一位
                i += 1
            # 返回计数器是否大于等于 p
            return cnt >= p

        # 初始化左右边界，左边界为0，右边界为数组中的最大值
        left, right = 0, max(nums)
        # 对数组进行排序
        nums.sort()
        # 获取数组的长度
        n = len(nums)
        # 当左边界小于等于右边界时，进行二分查找
        while left <= right:
            # 计算中间值
            mid = (left + right) // 2
            # 如果中间值满足条件，缩小右边界
            if check(mid):
                right = mid - 1
            # 如果中间值不满足条件，增大左边界
            else:
                left = mid + 1
        # 返回左边界，即最小的最大差值
        return left



# s = Solution()
# s.minimizeMax(nums = [10,1,2,7,1,3], p = 2)
# s.minimizeMax(nums = [2,6,2,4,2,2,0,2], p = 4)
"""2513. 最小化两个数组中的最大值 2302
给你两个数组arr1 和arr2，它们一开始都是空的。
你需要往它们中添加正整数，使它们满足以下条件：
	arr1包含uniqueCnt1个互不相同的正整数，每个整数都不能 被divisor1整除。
	arr2包含uniqueCnt2个互不相同的正整数，每个整数都不能被divisor2整除。
	arr1 和arr2中的元素互不相同。
给你divisor1，divisor2，uniqueCnt1和uniqueCnt2，请你返回两个数组中最大元素的最小值。
示例 1：
输入：divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
输出：4
解释：
我们可以把前 4 个自然数划分到 arr1 和 arr2 中。
arr1 = [1] 和 arr2 = [2,3,4] 。
可以看出两个数组都满足条件。
最大值是 4 ，所以返回 4 。
示例 2：
输入：divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
输出：3
解释：
arr1 = [1,2] 和 arr2 = [3] 满足所有条件。
最大值是 3 ，所以返回 3 。
示例 3：
输入：divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
输出：15
解释：
最终数组为 arr1 = [1,3,5,7,9,11,13,15] 和 arr2 = [2,6] 。
上述方案是满足所有条件的最优解。
提示：
	2 <= divisor1, divisor2 <= 10^5
	1 <= uniqueCnt1, uniqueCnt2 < 10^9
	2 <= uniqueCnt1 + uniqueCnt2 <= 10^9
https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/
"""

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # 初始化左右边界，左边界为1，右边界为10的9次方乘以3
        left, right = 1, (uniqueCnt1 + uniqueCnt2) * 2
        # 当左边界小于等于右边界时，进行二分查找
        while left <= right:
            # 计算中间值
            mid = (left + right) // 2
            # 计算mid中能被divisor1整除的数的个数
            cnt1 = mid // divisor1
            # 计算mid中能被divisor2整除的数的个数
            cnt2 = mid // divisor2
            # 计算mid中能同时被divisor1和divisor2整除的数的个数
            cnt3 = mid // lcm(divisor1, divisor2)
            # 计算mid中既不能被divisor1整除也不能被divisor2整除的数的个数
            c3 = mid - cnt1 - cnt2 + cnt3
            # 计算mid中能被divisor1整除但不能被divisor2整除的数的个数
            c1 = mid - cnt1 - c3
            # 计算mid中能被divisor2整除但不能被divisor1整除的数的个数
            c2 = mid - cnt2 - c3
            # 如果既不能被divisor1整除也不能被divisor2整除的数的个数大于等于uniqueCnt1和uniqueCnt2中剩余需要的数的个数
            if c3 >= max(uniqueCnt1 - c1, 0) + max(uniqueCnt2 - c2, 0):
                # 缩小右边界
                right = mid - 1
            # 如果既不能被divisor1整除也不能被divisor2整除的数的个数小于uniqueCnt1和uniqueCnt2中剩余需要的数的个数
            else:
                # 增大左边界
                left = mid + 1
        # 返回左边界，即满足条件的最小整数
        return left


# s = Solution()
# s.minimizeSet(divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3)
"""LCP 12. 小张刷题计划
为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，编号从 0 到 n-1，并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。
在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。
我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。
示例 1：
输入：time = [1,2,3,3], m = 2
输出：3
解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。
示例 2：
输入：time = [999,999,999], m = 4
输出：0
解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。
限制：
	1 <= time.length <= 10^5
	1 <= time[i] <= 10000
	1 <= m <= 1000
https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/
"""


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        left, right = 0, sum(time)
        while left <= right:
            mid = (left + right) // 2
            s = mx = 0
            cnt = 1
            for t in time:
                mx = max(mx, t)
                s += t
                if s - mx > mid:
                    cnt += 1
                    mx = t
                    s = t
            if cnt <= m:
                right = mid - 1
            else:
                left = mid + 1
        return left


s = Solution()
s.minTime(time = [1,2,3,3], m = 2)




































