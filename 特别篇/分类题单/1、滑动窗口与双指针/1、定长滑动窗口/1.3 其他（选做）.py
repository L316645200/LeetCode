#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：1.3 其他（选做）.py
# @Author  ：Lin
# @Date    ：2024/9/19 16:38

"""2269. 找到一个数字的 K 美丽值 1280
一个整数 num 的 k 美丽值定义为 num 中符合以下条件的 子字符串 数目：
子字符串长度为 k 。
子字符串能整除 num 。
给你整数 num 和 k ，请你返回 num 的 k 美丽值。
注意：
允许有 前缀 0 。
0 不能整除任何值。
一个 子字符串 是一个字符串里的连续一段字符序列。
示例 1：
输入：num = 240, k = 2
输出：2
解释：以下是 num 里长度为 k 的子字符串：
- "240" 中的 "24" ：24 能整除 240 。
- "240" 中的 "40" ：40 能整除 240 。
所以，k 美丽值为 2 。
示例 2：
输入：num = 430043, k = 2
输出：2
解释：以下是 num 里长度为 k 的子字符串：
- "430043" 中的 "43" ：43 能整除 430043 。
- "430043" 中的 "30" ：30 不能整除 430043 。
- "430043" 中的 "00" ：0 不能整除 430043 。
- "430043" 中的 "04" ：4 不能整除 430043 。
- "430043" 中的 "43" ：43 能整除 430043 。
所以，k 美丽值为 2 。
提示：
1 <= num <= 109
1 <= k <= num.length （将 num 视为字符串）
"""
import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        res = 0
        for i in range(n-k+1):
            tmp = s[i:i+k]
            if tmp != 0 and num % int(tmp) == 0:
                res += 1
        return res


# s = Solution()
# s.divisorSubstrings(num = 240, k = 2)

"""1984. 学生分数的最小差值 1306
给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。

从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。

返回可能的 最小差值 。

 

示例 1：

输入：nums = [90], k = 1
输出：0
解释：选出 1 名学生的分数，仅有 1 种方法：
- [90] 最高分和最低分之间的差值是 90 - 90 = 0
可能的最小差值是 0
示例 2：

输入：nums = [9,4,1,7], k = 2
输出：2
解释：选出 2 名学生的分数，有 6 种方法：
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
- [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
可能的最小差值是 2
 

提示：

1 <= k <= nums.length <= 1000
0 <= nums[i] <= 105
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float("inf")
        l = len(nums)
        nums.sort()
        for i in range(l-k+1):
            res = min(res, nums[i+k-1] - nums[i])
        return res


"""220. 存在重复元素 III[hard]
给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。
找出满足下述条件的下标对 (i, j)：
i != j,
abs(i - j) <= indexDiff
abs(nums[i] - nums[j]) <= valueDiff
如果存在，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
输出：true
解释：可以找出 (i, j) = (0, 3) 。
满足下述 3 个条件：
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
示例 2：
输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
输出：false
解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。
提示：
2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
"""

# 滑动窗口 & 二分 nlog（indexDiff）
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        stack = SortedList()  # 有序数组

        for i, value in enumerate(nums):
            if i > indexDiff:
                stack.remove(nums[i-indexDiff-1])

            idx = bisect.bisect_left(stack, nums[i]-valueDiff)
            if idx < len(stack) and nums[i] + valueDiff >= stack[idx]:
                return True

            stack.add(value)
        return False


# s = Solution()
# r = s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3)
# print(r)


"""桶排序
上述解法无法做到线性的原因是：我们需要在大小为 k 的滑动窗口所在的「有序集合」中找到与 u 接近的数。
如果我们能够将 k 个数字分到 k 个桶的话，
那么我们就能 O(1) 的复杂度确定是否有 [u−t,u+t] 的数字（检查目标桶是否有元素）。
具体的做法为：令桶的大小为 size=t+1，根据 u 计算所在桶编号：
如果已经存在该桶，说明前面已有 [u−t,u+t] 范围的数字，返回 true
如果不存在该桶，则检查相邻两个桶的元素是有 [u−t,u+t] 范围的数字，如有 返回 true
建立目标桶，并删除下标范围不在 [max(0,i−k),i) 内的桶
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def getIdx(u):
            return u // size  # 将 k 个数字分到 k 个桶

        mp = {}
        size = valueDiff + 1
        for i, value in enumerate(nums):
            u = getIdx(value)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if u in mp:
                return True
            if u - 1 in mp and abs(value - mp[u-1]) <= valueDiff:
                return True
            if u + 1 in mp and abs(value - mp[u+1]) <= valueDiff:
                return True
            mp[u] = value
            # # 维护个数为k
            if i >= indexDiff:
                mp.pop(getIdx(nums[i-indexDiff]))
        return False


s = Solution()
# r = s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3)

r = s.containsNearbyAlmostDuplicate(nums = [2,0,-2,2], indexDiff = 2, valueDiff = 1)

print(r)


























