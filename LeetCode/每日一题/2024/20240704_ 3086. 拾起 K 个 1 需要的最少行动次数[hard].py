#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240704_ 3086. 拾起 K 个 1 需要的最少行动次数[hard].py
# @Author  ：Lin
# @Date    ：2024/7/4 10:09


"""给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。
Alice 在玩一个游戏，游戏的目标是让 Alice 使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。游戏开始时，Alice 可以选择数组 [0, n - 1] 范围内的任何索引 aliceIndex 站立。如果 nums[aliceIndex] == 1 ，Alice 会拾起一个 1 ，并且 nums[aliceIndex] 变成0（这 不算 作一次行动）。之后，Alice 可以执行 任意数量 的 行动（包括零次），在每次行动中 Alice 必须 恰好 执行以下动作之一：
选择任意一个下标 j != aliceIndex 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行 maxChanges 次。
选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，然后交换它们的值（将 nums[y] = 1 和 nums[x] = 0）。如果 y == aliceIndex，在这次行动后 Alice 拾起一个 1 ，并且 nums[y] 变成 0 。
返回 Alice 拾起 恰好 k 个 1 所需的 最少 行动次数。
示例 1：
输入：nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1
输出：3
解释：如果游戏开始时 Alice 在 aliceIndex == 1 的位置上，按照以下步骤执行每个动作，他可以利用 3 次行动拾取 3 个 1 ：
游戏开始时 Alice 拾取了一个 1 ，nums[1] 变成了 0。此时 nums 变为 [1,1,1,0,0,1,1,0,0,1] 。
选择 j == 2 并执行第一种类型的动作。nums 变为 [1,0,1,0,0,1,1,0,0,1]
选择 x == 2 和 y == 1 ，并执行第二种类型的动作。nums 变为 [1,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为  [1,0,0,0,0,1,1,0,0,1] 。
选择 x == 0 和 y == 1 ，并执行第二种类型的动作。nums 变为 [0,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为  [0,0,0,0,0,1,1,0,0,1] 。
请注意，Alice 也可能执行其他的 3 次行动序列达成拾取 3 个 1 。
示例 2：
输入：nums = [0,0,0,0], k = 2, maxChanges = 3
输出：4
解释：如果游戏开始时 Alice 在 aliceIndex == 0 的位置上，按照以下步骤执行每个动作，他可以利用 4 次行动拾取 2 个 1 ：
选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于 y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
再次选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
再次选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
提示：
2 <= n <= 105
0 <= nums[i] <= 1
1 <= k <= 105
0 <= maxChanges <= 105
maxChanges + sum(nums) >= k"""
from math import inf
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        res = inf

        def f(i: int) -> int:
            return sum(nums[max(i - 1, 0):min(i + 2, n)])
        left, right = 0, -1
        left_cnt, right_cnt = 0, 0
        left_sum, right_sum = 0, 0
        for i in range(n):
            if f(i) + maxChanges >= k:
                if k <= f(i):
                    res = min(res, k - nums[i])
                else:
                    res = min(res, k * 2 - f(i) - nums[i])
            if k <= maxChanges:
                continue
            while right + 1 < n and (right - i < i - left or left_cnt + right_cnt + maxChanges < k):
                if nums[right + 1] == 1:
                    right_cnt += 1
                    right_sum += right + 1
                right += 1
            while left_cnt + right_cnt + maxChanges > k:
                if right - i < i - left or (right - i == i - left and nums[left] == 1):
                    if nums[left] == 1:
                        left_cnt -= 1
                        left_sum -= left
                    left += 1
                else:
                    if nums[right] == 1:
                        right_cnt -= 1
                        right_sum -= right
                    right -= 1
            res = min(res, left_cnt * i - left_sum + right_sum - right_cnt * i + 2 * maxChanges)
            if nums[i] == 1:
                left_cnt += 1
                left_sum += i
                right_cnt -= 1
                right_sum -= i
        print(res)
        return res



s = Solution()
s.minimumMoves(nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1)
# s.minimumMoves(nums = [1,0,1,0,1], k = 3, maxChanges = 0)
# s.minimumMoves(nums = [0,1], k = 1, maxChanges = 2)
























