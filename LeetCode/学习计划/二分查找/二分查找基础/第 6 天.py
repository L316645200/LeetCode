#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天.py
# @Author: Lin
# @Date  : 2023/5/24 15:59

# 1898. 可移除字符的最大数目
# 给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
# 请你找出一个整数 k（0 <= k <= removable.length），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
# 返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
# 字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。
# 示例 1：
# 输入：s = "abcacb", p = "ab", removable = [3,1,0]
# 输出：2
# 解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
# "ab" 是 "accb" 的一个子序列。
# 如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
# 因此，最大的 k 是 2 。
# 示例 2：
# 输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
# 输出：1
# 解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
# "abcd" 是 "abcddddd" 的一个子序列。
# 示例 3：
# 输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
# 输出：0
# 解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
# 提示：
# 1 <= p.length <= s.length <= 105
# 0 <= removable.length < s.length
# 0 <= removable[i] < s.length
# p 是 s 的一个 子字符串
# s 和 p 都由小写英文字母组成
# removable 中的元素 互不相同
import bisect
from typing import List


#
# class Solution:
#     def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
#         ns, np = len(s), len(p)
#         n = len(removable)
#
#         # 辅助函数，用来判断移除 k 个下标后 p 是否是 s_k 的子序列
#         def check(k: int) -> bool:
#             state = [True] * ns  # s 中每个字符的状态
#             for i in range(k):
#                 state[removable[i]] = False
#             # 匹配 s_k 与 p
#             j = 0
#             for i in range(ns):
#                 # s[i] 未被删除且与 p[j] 相等时，匹配成功，增加 j
#                 if state[i] and s[i] == p[j]:
#                     j += 1
#                     if j == np:
#                         return True
#             return False
#
#         # 二分查找
#         l, r = 0, n + 1
#         while l < r:
#             mid = l + (r - l) // 2
#             if check(mid):
#                 l = mid + 1
#             else:
#                 r = mid
#         return l - 1


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)
        n = len(removable)
        left, right = 0, n
        res = 0
        def check(k):
            state = [True] * ns
            for i in range(k):
                state[removable[i]] = False
            j = 0
            for i in range(ns):
                if state[i] and s[i] == p[j]:

                    j += 1
                    if j == np:
                        return True
            return False

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        return res


s = Solution()
s.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4])

# s.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6])

# s.maximumRemovals(s = "qlevcvgzfpryiqlwy", p = "qlecfqlw", removable = [12,5])


# 1870. 准时到达的列车最小时速
# 给你一个浮点数 hour ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 n 趟列车。另给你一个长度为 n 的整数数组 dist ，其中 dist[i] 表示第 i 趟列车的行驶距离（单位是千米）。
# 每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
# 例如，第 1 趟列车需要 1.5 小时，那你必须再等待 0.5 小时，搭乘在第 2 小时发车的第 2 趟列车。
# 返回能满足你准时到达办公室所要求全部列车的 最小正整数 时速（单位：千米每小时），如果无法准时到达，则返回 -1 。
# 生成的测试用例保证答案不超过 107 ，且 hour 的 小数点后最多存在两位数字 。
# 示例 1：
# 输入：dist = [1,3,2], hour = 6
# 输出：1
# 解释：速度为 1 时：
# - 第 1 趟列车运行需要 1/1 = 1 小时。
# - 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。
# - 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。
# - 你将会恰好在第 6 小时到达。
# 示例 2：
# 输入：dist = [1,3,2], hour = 2.7
# 输出：3
# 解释：速度为 3 时：
# - 第 1 趟列车运行需要 1/3 = 0.33333 小时。
# - 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
# - 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
# - 你将会在第 2.66667 小时到达。
# 示例 3：
# 输入：dist = [1,3,2], hour = 1.9
# 输出：-1
# 解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。
# 提示：
# n == dist.length
# 1 <= n <= 105
# 1 <= dist[i] <= 105
# 1 <= hour <= 109
# hours 中，小数点后最多存在两位数字
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        left, right = 1, max(dist) * 100
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            hours = sum([math.ceil(dist[i] / mid) for i in range(n - 1)]) + dist[n-1] / mid

            if hours > hour:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
            print(mid, hours, left, right)
        return ans



s = Solution()
r = s.minSpeedOnTime(dist =[1,10000,2], hour = 3)
print(r)




























