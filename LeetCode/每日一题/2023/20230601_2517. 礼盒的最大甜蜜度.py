#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230601_2517. 礼盒的最大甜蜜度.py
# @Author: Lin
# @Date  : 2023/6/1 10:06

# 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
# 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
# 返回礼盒的 最大 甜蜜度。
# 示例 1：
# 输入：price = [13,5,1,8,21,2], k = 3
# 输出：8
# 解释：选出价格分别为 [13,5,21] 的三类糖果。
# 礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
# 可以证明能够取得的最大甜蜜度就是 8 。
# 示例 2：
# 输入：price = [1,3,1], k = 2
# 输出：2
# 解释：选出价格分别为 [1,3] 的两类糖果。
# 礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
# 可以证明能够取得的最大甜蜜度就是 2 。
# 示例 3：
# 输入：price = [7,7,7,7], k = 2
# 输出：0
# 解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
# 提示：
# 1 <= price.length <= 105
# 1 <= price[i] <= 109
# 2 <= k <= price.length
import bisect
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        left, right = 0, price[n - 1] - price[0]
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            current = price[0]
            cnt = 1
            for i in range(1, n):
                if price[i] - current >= mid:
                    current = price[i]
                    cnt += 1
            if cnt < k:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        def check(mid):
            current = price[0]
            cnt = 1
            for i in range(1, n):
                if price[i] - current >= mid:
                    current = price[i]
                    cnt += 1
            return cnt < k

        return bisect.bisect_left(range(0, price[n - 1] - price[0] + 1), True, key=check) - 1


s = Solution()
res = s.maximumTastiness(price = [13,5,1,8,21,2], k = 3)
print(res)
`