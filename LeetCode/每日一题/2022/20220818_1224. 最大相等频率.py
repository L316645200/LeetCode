#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220818_1224. 最大相等频率.py
# @Author: Lin
# @Date  : 2022/8/18 10:07

# 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
# 示例 1：
# 输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
# 示例 2：
# 输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
# 提示：
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 105
from collections import Counter
from typing import List


# 自作 倒序更快
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        nums.append(0)
        cnt = Counter(nums)
        n = len(nums)-1
        def isEqual(cnt):
            cnt2 = Counter(cnt.values())
            if len(cnt2) == 2:
                c = sorted(cnt2.items(), key=lambda x: x[1])
                if c[0][1] == 1 and (c[0][0] == 1 or c[0][0] - c[1][0] == 1):
                    return True
            # elif len(cnt2) == 1 and cnt2.get(1):
            #     return True
            return False

        for i in range(n, 1, -1):
            cnt[nums[i]] -= 1
            if cnt[nums[i]] == 0:
                del cnt[nums[i]]

            if isEqual(cnt):
                return i
        return n


# 官解
# 方法一：哈希表
# 使用哈希表 \textit{count}count 记录数 xx 出现的次数 \textit{count}[x]count[x]，\textit{freq}freq 记录出现次数为 ff 的数的数目为 \textit{freq}[f]freq[f]，\textit{maxFreq}maxFreq 表示最大出现次数。
# 依次遍历数组，假设当前访问的数为 \textit{nums}[i]nums[i]，对应地更新 \textit{count}count，\textit{freq}freq 以及 \textit{maxFreq}maxFreq。以 \textit{nums}[i]nums[i] 结尾的数组前缀符合要求的充要条件为满足以下三个条件之一：
# 最大出现次数 \textit{maxFreq} = 1maxFreq=1：那么所有数的出现次数都是一次，随意删除一个数既可符合要求。
# 所有数的出现次数都是 \textit{maxFreq}maxFreq 或 \textit{maxFreq} - 1maxFreq−1，并且最大出现次数的数只有一个：删除一个最大出现次数的数，那么所有数的出现次数都是 \textit{maxFreq} - 1maxFreq−1。
# 除开一个数，其他所有数的出现次数都是 \textit{maxFreq}maxFreq，并且该数的出现次数为 11：直接删除出现次数为 11 的数，那么所有数的出现次数都是 \textit{maxFreq}maxFreq。

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or \
               freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or \
               freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans


s = Solution()
s.maxEqualFreq([0])