 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 50. Pow(x, n).py
# @Author: Lin
# @Date  : 2022/4/13 16:07
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
# 提示：
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickmul(num):
            if num == 0:
                return 1
            y = quickmul(num//2)
            return y * y if num % 2 == 0 else y * y * x
        return quickmul(n) if n > 0 else 1 / quickmul(-n)


s = Solution()
s.myPow(2,10)