#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220103_1185. 一周中的第几天.py
# @Author: Lin
# @Date  : 2022/1/3 11:08
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
#  
#
# 示例 1：
#
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
# 示例 2：
#
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
# 示例 3：
#
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#  
#
# 提示：
#
# 给出的日期一定是在 1971 到 2100 年之间的有效日期。


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

        if self.is_leap(year):
            month_days[1] += 1
        days = sum(month_days[:month-1]) + day

        # for i in range(1971, year):
        #     if self.is_leap(i):
        #         days += 366
        #     else:
        #         days += 365
        days += 365 * (year - 1971) + (year - 1969) // 4
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return week[(days+4) % 7]

    def is_leap(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)



s = Solution()
s.dayOfTheWeek(31,8,2019)
s.dayOfTheWeek(15,8,1993)