#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250127_45. 跳跃游戏 II[medium].py
# @Author  ：Lin
# @Date    ：2025/1/27 9:58

"""给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。



示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2


提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_num, next_num, step = 0, nums[0], 0
        for i in range(n):
            if i > max_num:
                max_num = next_num
                step += 1
            next_num = max(next_num, i + nums[i])
            if max_num >= n - 1:
                return step




s = Solution()
s.jump(nums = [3,2,1])
