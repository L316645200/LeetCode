#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240606_2938. 区分黑球与白球.py
# @Author  ：Lin
# @Date    ：2024/6/6 10:33


"""桌子上有 n 个球，每个球的颜色不是黑色，就是白色。
给你一个长度为 n 、下标从 0 开始的二进制字符串 s，其中 1 和 0 分别代表黑色和白色的球。
在每一步中，你可以选择两个相邻的球并交换它们。
返回「将所有黑色球都移到右侧，所有白色球都移到左侧所需的 最小步数」。
示例 1：
输入：s = "101"
输出：1
解释：我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "011"。
最开始，1 没有都在右侧，需要至少 1 步将其移到右侧。
示例 2：
输入：s = "100"
输出：2
解释：我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "010"。
- 交换 s[1] 和 s[2]，s = "001"。
可以证明所需的最小步数为 2 。
示例 3：
输入：s = "0111"
输出：0
解释：所有黑色球都已经在右侧。
提示：
1 <= n == s.length <= 105
s[i] 不是 '0'，就是 '1'。"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        n, res = len(s), 0
        left, right = n-1, n-1
        while left >= 0:
            while right > 0 and arr[right] != '0':
                right -= 1
            while left >= 0 and arr[left] != '1':
                left -= 1

            if 0 <= left < right:
                res += right - left
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
            left -= 1
        return res


"""方法一：贪心
思路

交换完后的最终状态一定是形如 000011110000111100001111，
那么遍历字符串的时候每碰到一个 000 就贪心的将其往左交换直到它最终的位置。
在遍历到这个 000 时，因为它左边的 000 已经都交换到最终位置了，
所以它的左边是一串连续的 111，那么只要加上遍历时碰到 111 的个数即可。
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        res, total = 0, 0
        for i in s:
            if i == '1':
                total += 1
            else:
                res += total
        return res

s = Solution()
# s.minimumSteps(s = "100")

res = s.minimumSteps(s = "01010001")
print(res)