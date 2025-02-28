#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241130_3232. 判断是否可以赢得数字游戏[easy].py
# @Author  ：Lin
# @Date    ：2024/11/30 9:43

"""给你一个 正整数 数组 nums。

Alice 和 Bob 正在玩游戏。在游戏中，Alice 可以从 nums 中选择所有个位数 或 所有两位数，剩余的数字归 Bob 所有。如果 Alice 所选数字之和 严格大于 Bob 的数字之和，则 Alice 获胜。

如果 Alice 能赢得这场游戏，返回 true；否则，返回 false。



示例 1：

输入：nums = [1,2,3,4,10]

输出：false

解释：

Alice 不管选个位数还是两位数都无法赢得比赛。

示例 2：

输入：nums = [1,2,3,4,5,14]

输出：true

解释：

Alice 选择个位数可以赢得比赛，所选数字之和为 15。

示例 3：

输入：nums = [5,5,5,25]

输出：true

解释：

Alice 选择两位数可以赢得比赛，所选数字之和为 25。



提示：

1 <= nums.length <= 100
1 <= nums[i] <= 99"""
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = s2 = 0
        for num in nums:
            if num < 10:
                s1 += num
            else:
                s2 += num
        return s1 != s2