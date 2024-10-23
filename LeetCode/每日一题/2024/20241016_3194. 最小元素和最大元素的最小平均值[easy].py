#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241016_3194. 最小元素和最大元素的最小平均值[easy].py
# @Author  ：Lin
# @Date    ：2024/10/16 11:19

"""你有一个初始为空的浮点数数组 averages。另给你一个包含 n 个整数的数组 nums，其中 n 为偶数。
你需要重复以下步骤 n / 2 次：
从 nums 中移除 最小 的元素 minElement 和 最大 的元素 maxElement。
将 (minElement + maxElement) / 2 加入到 averages 中。
返回 averages 中的 最小 元素。
示例 1：
输入： nums = [7,8,3,4,15,13,4,1]
输出： 5.5
解释：
步骤	nums	averages
0	[7,8,3,4,15,13,4,1]	[]
1	[7,8,3,4,13,4]	[8]
2	[7,8,4,4]	[8,8]
3	[7,4]	[8,8,6]
4	[]	[8,8,6,5.5]
返回 averages 中最小的元素，即 5.5。
示例 2：
输入： nums = [1,9,8,3,10,5]
输出： 5.5
解释：
步骤	nums	averages
0	[1,9,8,3,10,5]	[]
1	[9,8,3,5]	[5.5]
2	[8,5]	[5.5,6]
3	[]	[5.5,6,6.5]
示例 3：
输入： nums = [1,2,3,7,8,9]
输出： 5.0
解释：
步骤	nums	averages
0	[1,2,3,7,8,9]	[]
1	[2,3,7,8]	[5]
2	[3,7]	[5,5]
3	[]	[5,5,5]
提示：
2 <= n == nums.length <= 50
n 为偶数。
1 <= nums[i] <= 50"""
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 50
        while left < right:
            ans = min(ans, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return ans


s = Solution()
s.minimumAverage(nums = [7,8,3,4,15,13,4,1])