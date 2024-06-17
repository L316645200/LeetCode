#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240609_第 401 场周赛.py
# @Author  ：Lin
# @Date    ：2024/6/15 14:34

"""3178. 找出 K 秒后拿着球的孩子 显示英文描述
通过的用户数2444
尝试过的用户数2505
用户总通过次数2483
用户总提交次数3735
题目难度Easy
给你两个 正整数 n 和 k。有 n 个编号从 0 到 n - 1 的孩子按顺序从左到右站成一队。

最初，编号为 0 的孩子拿着一个球，并且向右传球。每过一秒，拿着球的孩子就会将球传给他旁边的孩子。一旦球到达队列的 任一端 ，即编号为 0 的孩子或编号为 n - 1 的孩子处，传球方向就会 反转 。

返回 k 秒后接到球的孩子的编号。
示例 1：

输入：n = 3, k = 5

输出：1

解释：

经过的时间	孩子队列
0	[0, 1, 2]
1	[0, 1, 2]
2	[0, 1, 2]
3	[0, 1, 2]
4	[0, 1, 2]
5	[0, 1, 2]
示例 2：

输入：n = 5, k = 6

输出：2

解释：

经过的时间	孩子队列
0	[0, 1, 2, 3, 4]
1	[0, 1, 2, 3, 4]
2	[0, 1, 2, 3, 4]
3	[0, 1, 2, 3, 4]
4	[0, 1, 2, 3, 4]
5	[0, 1, 2, 3, 4]
6	[0, 1, 2, 3, 4]
示例 3：

输入：n = 4, k = 2

输出：2

解释：

经过的时间	孩子队列
0	[0, 1, 2, 3]
1	[0, 1, 2, 3]
2	[0, 1, 2, 3]


提示：

2 <= n <= 50
1 <= k <= 50"""
import bisect
from math import comb
from typing import List


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        remainder = k % ((n-1) * 2)
        print(remainder)
        return remainder if remainder < n else (2 * (n-1)) - remainder

"""3179. K 秒后第 N 个元素的值 显示英文描述 
通过的用户数2209
尝试过的用户数2338
用户总通过次数2266
用户总提交次数4215
题目难度Medium
给你两个整数 n 和 k。

最初，你有一个长度为 n 的整数数组 a，对所有 0 <= i <= n - 1，都有 a[i] = 1 。每过一秒，你会同时更新每个元素为其前面所有元素的和加上该元素本身。例如，一秒后，a[0] 保持不变，a[1] 变为 a[0] + a[1]，a[2] 变为 a[0] + a[1] + a[2]，以此类推。

返回 k 秒后 a[n - 1] 的值。

由于答案可能非常大，返回其对 109 + 7 取余 后的结果。

 

示例 1：

输入：n = 4, k = 5

输出：56

解释：

时间（秒）	数组状态
0	[1,1,1,1]
1	[1,2,3,4]
2	[1,3,6,10]
3	[1,4,10,20]
4	[1,5,15,35]
5	[1,6,21,56]
示例 2：

输入：n = 5, k = 3

输出：35

解释：

时间（秒）	数组状态
0	[1,1,1,1,1]
1	[1,2,3,4,5]
2	[1,3,6,10,15]
3	[1,4,10,20,35]
 

提示：

1 <= n, k <= 1000"""
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        dp = [1] * n
        mod = 10 ** 9 + 7
        for i in range(k):
            for j in range(1, n):
                dp[j] = (dp[j] + dp[j-1]) % mod
        return dp[-1]
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return comb(n + k - 1, k) % 1_000_000_007


"""3180. 执行操作可获得的最大总奖励 I
已解答
中等
相关标签
相关企业
提示
给你一个整数数组 rewardValues，长度为 n，代表奖励的值。

最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：

从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
以整数形式返回执行最优操作能够获得的 最大 总奖励。

 

示例 1：

输入：rewardValues = [1,1,3,3]

输出：4

解释：

依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。

示例 2：

输入：rewardValues = [1,6,4,3,2]

输出：11

解释：

依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。

 

提示：

1 <= rewardValues.length <= 2000
1 <= rewardValues[i] <= 2000"""
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(list(set(rewardValues)))
        n = len(rewardValues)
        dp = [0] * (max(rewardValues) * 2)
        dp[0] = 1
        res = 0
        for i in range(n):
            for j in range(rewardValues[i]):
                if dp[j] == 1:
                    dp[rewardValues[i] + j] = 1
                    res = max(res, rewardValues[i] + j)
        return res


s = Solution()
s.maxTotalReward( [1,6,4,3,2,9])


