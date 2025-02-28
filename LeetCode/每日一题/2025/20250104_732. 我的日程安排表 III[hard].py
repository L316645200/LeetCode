#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250104_732. 我的日程安排表 III[hard].py
# @Author  ：Lin
# @Date    ：2025/1/4 9:25

"""当 k 个日程存在一些非空交集时（即, k 个日程包含了一些相同时间），就会产生 k 次预订。
给你一些日程安排 [startTime, endTime) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
MyCalendarThree() 初始化对象。
int book(int startTime, int endTime) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。
示例：
输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]
解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
提示：
0 <= startTime < endTime <= 109
每个测试用例，调用 book 函数最多不超过 400次"""
from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.cnt[startTime] = self.cnt.get(startTime, 0) + 1
        self.cnt[endTime] = self.cnt.get(endTime, 0) - 1
        res = max_book = 0
        for freq in self.cnt.values():
            max_book += freq
            res = max(res, max_book)
        return res


m = MyCalendarThree()
for s,e in [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]:
    m.book(s, e)
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

