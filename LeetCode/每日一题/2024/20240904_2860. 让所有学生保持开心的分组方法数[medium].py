#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240904_2860. 让所有学生保持开心的分组方法数[medium].py
# @Author  ：Lin
# @Date    ：2024/9/4 10:37


"""给你一个下标从 0 开始、长度为 n 的整数数组 nums ，其中 n 是班级中学生的总数。班主任希望能够在让所有学生保持开心的情况下选出一组学生：
如果能够满足下述两个条件之一，则认为第 i 位学生将会保持开心：
这位学生被选中，并且被选中的学生人数 严格大于 nums[i] 。
这位学生没有被选中，并且被选中的学生人数 严格小于 nums[i] 。
返回能够满足让所有学生保持开心的分组方法的数目。
示例 1：
输入：nums = [1,1]
输出：2
解释：
有两种可行的方法：
班主任没有选中学生。
班主任选中所有学生形成一组。
如果班主任仅选中一个学生来完成分组，那么两个学生都无法保持开心。因此，仅存在两种可行的方法。
示例 2：
输入：nums = [6,0,3,3,6,7,2,7]
输出：3
解释：
存在三种可行的方法：
班主任选中下标为 1 的学生形成一组。
班主任选中下标为 1、2、3、6 的学生形成一组。
班主任选中所有学生形成一组。
提示：
1 <= nums.length <= 105
0 <= nums[i] < nums.length"""
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        # 排序
        nums.sort()
        # 全不选和全选
        res = 2
        # 如果有0则全不选不可行
        if nums[0] == 0:
            res -= 1
        for i in range(n - 1):
            # i + 1人数， 如果两个条件都满足，则答案+1
            if nums[i] < i + 1 < nums[i + 1]:
                res += 1
        return res


s = Solution()
# s.countWays(nums = [6,0,3,3,6,7,2,7])

s.countWays(nums = [2,2,7,1,2,2,4,7])
