#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：2、二分答案：求最小.py
# @Author  ：Lin
# @Date    ：2025/1/11 15:03
"""1283. 使结果不超过阈值的最小除数 1542
给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
题目保证一定有解。
示例 1：
输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
示例 2：
输入：nums = [2,3,5,7,11], threshold = 11
输出：3
示例 3：
输入：nums = [19], threshold = 5
输出：4
提示：
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""
import bisect
import heapq
import math
from collections import Counter, defaultdict
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if sum((num + mid - 1) // mid for num in nums) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        k = bisect.bisect_left(list(range(1, max(nums) + 1)), -threshold, key=lambda x: -sum((num + x - 1) // x for num in nums))
        return k + 1

# s = Solution()
# s.smallestDivisor(nums = [1,2,5,9], threshold = 6)
# s.smallestDivisor(nums = [2,3,5,7,11], threshold = 11)

# s.smallestDivisor(nums = [44,22,33,11,1], threshold = 5)
"""2187. 完成旅途的最少时间 1641
给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。
每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。
给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。
示例 1：
输入：time = [1,2,3], totalTrips = 5
输出：3
解释：
- 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。
  已完成的总旅途数为 1 + 0 + 0 = 1 。
- 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。
  已完成的总旅途数为 2 + 1 + 0 = 3 。
- 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。
  已完成的总旅途数为 3 + 1 + 1 = 5 。
所以总共完成至少 5 趟旅途的最少时间为 3 。
示例 2：
输入：time = [2], totalTrips = 1
输出：2
解释：
只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。
所以完成 1 趟旅途的最少时间为 2 。
提示：
1 <= time.length <= 105
1 <= time[i], totalTrips <= 107
"""
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            if sum((mid // t) for t in time) < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return bisect.bisect_left(range(1, max(time) * totalTrips), totalTrips, key=lambda x: sum((x // t) for t in time)) + 1

# s = Solution()
# s.minimumTime(time = [1,2,3], totalTrips = 5)
"""1870. 准时到达的列车最小时速 1676
给你一个浮点数 hour ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 n 趟列车。另给你一个长度为 n 的整数数组 dist ，其中 dist[i] 表示第 i 趟列车的行驶距离（单位是千米）。
每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
例如，第 1 趟列车需要 1.5 小时，那你必须再等待 0.5 小时，搭乘在第 2 小时发车的第 2 趟列车。
返回能满足你在时限前到达办公室所要求全部列车的 最小正整数 时速（单位：千米每小时），如果无法准时到达，则返回 -1 。
生成的测试用例保证答案不超过 107 ，且 hour 的 小数点后最多存在两位数字 。
示例 1：
输入：dist = [1,3,2], hour = 6
输出：1
解释：速度为 1 时：
- 第 1 趟列车运行需要 1/1 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。
- 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。
- 你将会恰好在第 6 小时到达。
示例 2：
输入：dist = [1,3,2], hour = 2.7
输出：3
解释：速度为 3 时：
- 第 1 趟列车运行需要 1/3 = 0.33333 小时。
- 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
- 你将会在第 2.66667 小时到达。
示例 3：
输入：dist = [1,3,2], hour = 1.9
输出：-1
解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。
提示：
n == dist.length
1 <= n <= 105
1 <= dist[i] <= 105
1 <= hour <= 109
hours 中，小数点后最多存在两位数字
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1:
            return -1
        left, right = 1, max(dist) * 100
        while left <= right:
            mid = left + (right - left) // 2
            if sum((math.ceil(d/mid) for d in dist[:-1])) + dist[-1] / mid <= hour:
                right = mid - 1
            else:
                left = mid + 1
        return left

# s = Solution()
# s.minSpeedOnTime([1,1,100000], 2.01)
"""1011. 在 D 天内送达包裹的能力 1725
传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
示例 1：
输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
示例 2：
输入：weights = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：
输入：weights = [1,2,3,1,1], days = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
提示：
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            day = 1
            cur = capacity
            for w in weights:
                if cur < w:
                    cur = capacity
                    day += 1
                cur -= w
            return day
        # 确定二分边界
        left = max(weights)
        right = max(weights) * (len(weights) // days + 1)
        while left <= right:
            mid = (left + right) // 2
            # 如果当前运载重量可以在days天内完成
            if check(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left


# s = Solution()
# s.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)
"""875. 爱吃香蕉的珂珂 1766
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。
示例 1：
输入：piles = [3,6,7,11], h = 8
输出：4
示例 2：
输入：piles = [30,11,23,4,20], h = 5
输出：30
示例 3：
输入：piles = [30,11,23,4,20], h = 6
输出：23
提示：
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if sum((pile - 1) // mid + 1 for pile in piles) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        return bisect.bisect_left(range(max(piles)), -h, 1, key=lambda x: -sum((pile - 1) // x + 1 for pile in piles))


# s = Solution()
# s.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
"""3296. 移山所需的最少秒数 注：由于有其他做法，难度分会低一些，二分做法估计 1850
给你一个整数 mountainHeight 表示山的高度。
同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。
工人们需要 同时 进行工作以 降低 山的高度。对于工人 i :
山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 秒。例如：
山的高度降低 1，需要 workerTimes[i] 秒。
山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。
返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。
示例 1：
输入： mountainHeight = 4, workerTimes = [2,1,1]
输出： 3
解释：
将山的高度降低到 0 的一种方式是：
工人 0 将高度降低 1，花费 workerTimes[0] = 2 秒。
工人 1 将高度降低 2，花费 workerTimes[1] + workerTimes[1] * 2 = 3 秒。
工人 2 将高度降低 1，花费 workerTimes[2] = 1 秒。
因为工人同时工作，所需的最少时间为 max(2, 3, 1) = 3 秒。
示例 2：
输入： mountainHeight = 10, workerTimes = [3,2,2,4]
输出： 12
解释：
工人 0 将高度降低 2，花费 workerTimes[0] + workerTimes[0] * 2 = 9 秒。
工人 1 将高度降低 3，花费 workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 秒。
工人 2 将高度降低 3，花费 workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 秒。
工人 3 将高度降低 2，花费 workerTimes[3] + workerTimes[3] * 2 = 12 秒。
所需的最少时间为 max(9, 12, 12, 12) = 12 秒。
示例 3：
输入： mountainHeight = 5, workerTimes = [1]
输出： 15
解释：
这个示例中只有一个工人，所以答案是 workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15 秒。
提示：
1 <= mountainHeight <= 105
1 <= workerTimes.length <= 104
1 <= workerTimes[i] <= 106
"""
# 堆
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        res = 0
        # 初始化最小堆
        workerTimes = [(t, 2, t) for t in workerTimes]
        heapq.heapify(workerTimes)
        # 当山还有高度时
        for _ in range(mountainHeight):
            # 弹出最少秒数的工人数据
            res, j, init = heapq.heappop(workerTimes)
            # 更新结果
            # 当前工人降低多1点高度所需要花费的总时间(i * (i + 1)) // 2
            heapq.heappush(workerTimes, (init * (j * (j + 1)) // 2, j + 1, init))
        return res

# 二分
"""
设t为workerTimes[i],所有工人中最大花费为m,
则 t * (x + (x + 1)//2 <= m
==   (x + (x + 1)//2 <= m//t = k
==   (x  + 1//2) ** 2 = 根号(2k+1//4)
==   x = (根号(1+8k) - 1) //2
"""
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left, right = 1, min(workerTimes) * (mountainHeight * (mountainHeight + 1)) // 2
        while left <= right:
            mid = (left + right) // 2
            if sum([(math.sqrt(1+8*(mid//t)) - 1) // 2 for t in workerTimes]) < mountainHeight:
                left = mid + 1
            else:
                right = mid - 1
        return left

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        min_t = max(workerTimes)
        h = (mountainHeight * (mountainHeight + 1)) // 2
        return bisect.bisect_left(range(min_t*h), mountainHeight, 1, key=lambda x: sum([(math.sqrt(1+8*(x//t)) - 1) // 2 for t in workerTimes]))

# s = Solution()
# s.minNumberOfSeconds(mountainHeight = 4, workerTimes = [2,1,1])

# s.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1,7])
"""475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
在加热器的加热半径范围内的每个房屋都可以获得供暖。
现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
注意：所有供暖器 heaters 都遵循你的半径标准，加热的半径也一样。
示例 1:
输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
示例 2:
输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。
示例 3：
输入：houses = [1,5], heaters = [2]
输出：3
提示：
1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(radius):
            i = j = 0
            while i < len(houses) and j < len(heaters):
                if houses[i] < heaters[j] - radius:
                    return False
                elif houses[i] > heaters[j] + radius:
                    j += 1
                else:
                    i += 1
            return i == len(houses)

        houses.sort()
        heaters.sort()
        left, right = 0, max(houses) + max(heaters)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# s = Solution()
# s.findRadius(houses = [1,2,3], heaters = [2])
# r = s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
#                  [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])
"""2594. 修车的最少时间 1915
给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
同时给你一个整数 cars ，表示总共需要修理的汽车数目。
请你返回修理所有汽车 最少 需要多少时间。
注意：所有机械工可以同时修理汽车。
示例 1：
输入：ranks = [4,2,3,1], cars = 10
输出：16
解释：
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。
示例 2：
输入：ranks = [5,1,8], cars = 6
输出：16
解释：
- 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
- 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
- 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
16 分钟时修理完所有车需要的最少时间。
提示：
1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
"""

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars ** 2
        while left <= right:
            mid = (left + right) // 2
            if sum([int(math.sqrt(mid//r)) for r in ranks]) < cars:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        k = min(ranks) * cars ** 2
        f = lambda x: sum([int(math.sqrt(x//r)) for r in ranks])
        return bisect.bisect_left(range(k), cars, 1, key=f)

"""优化
能力值相同的人，在 t 分钟内修好的车的个数是一样的。
根据数据范围，ranks 中至多有 100 个不同的数字，我们可以统计 ranks 中每个数字的出现次数，
这样每次二分至多循环 100 次。
"""

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        cnt = Counter(ranks)
        left, right = 1, min(ranks) * cars ** 2
        while left <= right:
            mid = (left + right) // 2
            if sum([int(math.sqrt(mid//r)) * c for r, c in cnt.items()]) < cars:
                left = mid + 1
            else:
                right = mid - 1
        return left

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        k = min(ranks) * cars ** 2
        cnt = Counter(ranks)
        f = lambda x: sum([int(math.sqrt(x//r)) * c for r, c in cnt.items()])
        return bisect.bisect_left(range(k), cars, 1, key=f)

# s = Solution()
# s.repairCars(ranks = [4,2,3,1], cars = 10)
"""1482. 制作 m 束花所需的最少天数 1946
给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。
示例 1：
输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
输出：3
解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
现在需要制作 3 束花，每束只需要 1 朵。
1 天后：[x, _, _, _, _]   // 只能制作 1 束花
2 天后：[x, _, _, _, x]   // 只能制作 2 束花
3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
示例 2：
输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
输出：-1
解释：要制作 3 束花，每束需要 2 朵花，也就是一共需要 6 朵花。而花园中只有 5 朵花，无法满足制作要求，返回 -1 。
示例 3：
输入：bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
输出：12
解释：要制作 2 束花，每束需要 3 朵。
花园在 7 天后和 12 天后的情况如下：
7 天后：[x, x, x, x, _, x, x]
可以用前 3 朵盛开的花制作第一束花。但不能使用后 3 朵盛开的花，因为它们不相邻。
12 天后：[x, x, x, x, x, x, x]
显然，我们可以用不同的方式制作两束花。
示例 4：
输入：bloomDay = [1000000000,1000000000], m = 1, k = 1
输出：1000000000
解释：需要等 1000000000 天才能采到花来制作花束
示例 5：
输入：bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
输出：9
提示：
bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            cnt = cur = 0
            for day in bloomDay:
                if mid >= day:
                    cur += 1
                    if cur == k:
                        cnt += 1
                        cur = 0
                else:
                    cur = 0
            if cnt < m:
                left = mid + 1
            else:
                right = mid - 1
        return left


# s = Solution()
# s.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)
"""3048. 标记所有下标的最早秒数 I 2263
给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。
一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。
从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ：
选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。
如果 nums[changeIndices[s]] 等于 0 ，标记 下标 changeIndices[s] 。
什么也不做。
请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。
示例 1：
输入：nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]
输出：8
解释：这个例子中，我们总共有 8 秒。按照以下操作标记所有下标：
第 1 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [1,2,0] 。
第 2 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,2,0] 。
第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,1,0] 。
第 4 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,0,0] 。
第 5 秒，标​​​​​记 changeIndices[5] ，也就是标记下标 3 ，因为 nums[3] 等于 0 。
第 6 秒，标​​​​​记 changeIndices[6] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。
第 7 秒，什么也不做。
第 8 秒，标记 changeIndices[8] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。
现在所有下标已被标记。
最早可以在第 8 秒标记所有下标。
所以答案是 8 。
示例 2：
输入：nums = [1,3], changeIndices = [1,1,1,2,1,1,1]
输出：6
解释：这个例子中，我们总共有 7 秒。按照以下操作标记所有下标：
第 1 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,2] 。
第 2 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,1] 。
第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,0] 。
第 4 秒：标​​​​​记 changeIndices[4] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。
第 5 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,0] 。
第 6 秒：标​​​​​记 changeIndices[6] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。
现在所有下标已被标记。
最早可以在第 6 秒标记所有下标。
所以答案是 6 。
示例 3：
Input: nums = [0,1], changeIndices = [2,2,2]
Output: -1
Explanation: 这个例子中，无法标记所有下标，因为下标 1 不在 changeIndices 中。
所以答案是 -1 。
提示：
1 <= n == nums.length <= 2000
0 <= nums[i] <= 109
1 <= m == changeIndices.length <= 2000
1 <= changeIndices[i] <= n
"""

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        left, right = 0, m
        # 二分答案
        while left <= right:
            mid = (left + right) // 2
            mp = defaultdict(int)
            cnt = 0
            cur = False
            # 记录最早秒数前的所有整数的最晚下标
            for i in range(mid):
                mp[changeIndices[i]] = i
            # 所有下标都包含才有可能
            if len(mp) == n:
                cur = True
                for i in range(mid):
                    # print(mid, i, cnt)
                    # 还没到最晚下标，可以用来标记或者什么也不做
                    if mp[changeIndices[i]] > i:
                        cnt += 1
                    else:
                        # 最晚下标，必须将之前的记录全部标记掉
                        cnt -= nums[changeIndices[i]-1]
                        # 如果不够标记，则不可能
                        if cnt < 0:
                            cur = False
                            break
            # print(mp, left, right, mid, cnt, cur)
            if cur:
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= m else -1


s = Solution()
# s.earliestSecondToMarkIndices(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1])

# s.earliestSecondToMarkIndices(nums = [1,3], changeIndices = [1,1,1,2,1,1,1])


s.earliestSecondToMarkIndices(nums = [0,2,3,0], changeIndices = [2,4,1,3,3,3,3,3,3,2,1])
















































































