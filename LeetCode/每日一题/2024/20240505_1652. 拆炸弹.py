#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240505_1652. 拆炸弹.py
# @Author  ：Lin
# @Date    ：2024/5/7 14:48

"""你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
如果 k == 0 ，将第 i 个数字用 0 替换。
由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！



示例 1：

输入：code = [5,7,1,4], k = 3
输出：[12,10,16,13]
解释：每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。注意到数组是循环连接的。
示例 2：

输入：code = [1,2,3,4], k = 0
输出：[0,0,0,0]
解释：当 k 为 0 时，所有数字都被 0 替换。
示例 3：

输入：code = [2,4,9,3], k = -2
输出：[12,5,6,13]
解释：解密后的密码为 [3+9, 2+3, 4+2, 9+4] 。注意到数组是循环连接的。如果 k 是负数，那么和为 之前 的数字。


提示：

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1"""
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        # 0直接返回
        if k == 0:
            return ans
        direct = 1 if k > 0 else -1
        left, right = (direct + n) % n, (k + n) % n

        if left > right:
            left, right = right, left
        # 初始数字之和
        pre = sum(code[left: right+1])
        # 滑动数字之和
        for i in range(n):
            ans[i] = pre
            right = (right + 1) % n
            pre = pre + code[right] - code[left]
            left = (left + 1) % n
        return ans

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         if k == 0:
#             return [0] * len(code)
#         res = []
#         n = len(code)
#         code += code
#         if k > 0:
#             l, r = 1, k
#         else:
#             l, r = n + k, n - 1
#         w = sum(code[l:r+1])
#         for i in range(n):
#             res.append(w)
#             w -= code[l]
#             w += code[r + 1]
#             l, r = l + 1, r + 1
#         return res


s = Solution()
# s.decrypt(code = [5,7,1,4], k = 3)

s.decrypt(code = [2,4,9,3], k = -2)
