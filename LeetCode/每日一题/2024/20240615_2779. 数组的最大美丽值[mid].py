#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240615_2779. 数组的最大美丽值[mid].py
# @Author  ：Lin
# @Date    ：2024/6/15 10:28


"""给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。

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
0 <= nums[i], k <= 105"""
import bisect
from typing import List

# 排序+二分
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for i in range(min(nums), max(nums)+1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k)
            res = max(res, r - l)
        return res


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        return max([bisect.bisect_right(nums, i + k) - bisect.bisect_left(nums, i - k) for i in range(min(nums), max(nums)+1)])

# 排序+双指针
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        res = 0
        for i in range(len(nums)):
            while j < i and nums[i] - nums[j] > k * 2:
                j += 1
            res = max(res, i - j + 1)
        return res


# 方法二：差分数组
# 对于数组的某一元素 xxx，经过操作后，
# 它可以被替换成区间 [x−k,x+k] 内的任一整数。
# 因此我们可以使用差分数组 diff维护能够被替换成某一整数 y的数组元素数目。
#

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        m = max(nums)
        diff = [0] * (m + 2)

        # 对于元素x, 可以替换成[x−k,x+k] 内的任一整数，因此可以在x-k处计数+1，
        # 并在x+k+1处计数-1
        for x in nums:
            diff[max(x-k, 0)] += 1
            diff[min(x+k+1, m+1)] -= 1
        count = 0
        res = 0
        for i in diff:
            count += i
            res = max(res, count)
        return res


s = Solution()
s.maximumBeauty(nums = [1,1,1,1], k = 10)

# s.maximumBeauty(nums = [49,26], k = 12)
