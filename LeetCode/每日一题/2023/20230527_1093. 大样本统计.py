#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230527_1093. 大样本统计.py
# @Author: Lin
# @Date  : 2023/5/27 11:00

# 我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 在样本中出现的次数。
# 计算以下统计数据:
# minimum ：样本中的最小元素。
# maximum ：样品中的最大元素。
# mean ：样本的平均值，计算为所有元素的总和除以元素总数。
# median ：
# 如果样本的元素个数是奇数，那么一旦样本排序后，中位数 median 就是中间的元素。
# 如果样本中有偶数个元素，那么中位数median 就是样本排序后中间两个元素的平均值。
# mode ：样本中出现次数最多的数字。保众数是 唯一 的。
# 以浮点数数组的形式返回样本的统计信息 [minimum, maximum, mean, median, mode] 。与真实答案误差在 10-5 内的答案都可以通过。
# 示例 1：
#
# 输入：count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 输出：[1.00000,3.00000,2.37500,2.50000,3.00000]
# 解释：用count表示的样本为[1,2,2,2,3,3,3,3]。
# 最小值和最大值分别为1和3。
# 均值是(1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375。
# 因为样本的大小是偶数，所以中位数是中间两个元素2和3的平均值，也就是2.5。
# 众数为3，因为它在样本中出现的次数最多。
# 示例 2：
#
# 输入：count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 输出：[1.00000,4.00000,2.18182,2.00000,1.00000]
# 解释：用count表示的样本为[1,1,1,1,2,2,3,3,3,4,4]。
# 最小值为1，最大值为4。
# 平均数是(1+1+1+1+2+2+2+3+3+4+4)/ 11 = 24 / 11 = 2.18181818…(为了显示，输出显示了整数2.18182)。
# 因为样本的大小是奇数，所以中值是中间元素2。
# 众数为1，因为它在样本中出现的次数最多。
# 提示：
#
# count.length == 256
# 0 <= count[i] <= 109
# 1 <= sum(count) <= 109
#  count 的众数是 唯一 的
from statistics import mean, median, mode
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum, maximum = 255, 0
        c_sum, cnt, mode, max_i = 0, 0, 0, 0
        for c, i in enumerate(count):
            if i > 0:
                minimum = min(minimum, c)
                maximum = c
                c_sum += i * c
                cnt += i
                if i > max_i:
                    max_i = i
                    mode = c
        c_cnt = 0
        median = 0

        left = (cnt + 1) // 2
        right = (cnt + 2) // 2
        for c, i in enumerate(count):
            if c_cnt < right and c_cnt + i >= right:
                median += c
            if c_cnt < left and c_cnt + i >= left:
                median += c
            c_cnt += i
        return [minimum, maximum, c_sum / cnt, median / 2, mode]


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum, maximum = 255, 0
        c_sum, cnt, mode, max_i = 0, sum(count), 0, 0
        c_cnt = 0
        median = 0

        left = (cnt + 1) // 2
        right = (cnt + 2) // 2
        for c, i in enumerate(count):
            if i > 0:
                minimum = min(minimum, c)
                maximum = c
                c_sum += i * c
                if i > max_i:
                    max_i = i
                    mode = c
            if c_cnt < right and c_cnt + i >= right:
                median += c
            if c_cnt < left and c_cnt + i >= left:
                median += c
            c_cnt += i
        return [minimum, maximum, c_sum / cnt, median / 2, mode]
s = Solution()
s.sampleStats([0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])