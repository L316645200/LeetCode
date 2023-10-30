#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20231008_2034. 股票价格波动.py
# @Author: Lin
# @Date  : 2023/10/8 10:29

"""给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。

不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正 前一条错误的记录。

请你设计一个算法，实现：

更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。
找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。
找到当前记录里股票的 最高价格 。
找到当前记录里股票的 最低价格 。
请你实现 StockPrice 类：

StockPrice() 初始化对象，当前无股票价格记录。
void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。
int current() 返回股票 最新价格 。
int maximum() 返回股票 最高价格 。
int minimum() 返回股票 最低价格 。


示例 1：

输入：
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
输出：
[null, null, null, 5, 10, null, 5, null, 2]

解释：
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
                          // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。


提示：

1 <= timestamp, price <= 109
update，current，maximum 和 minimum 总 调用次数不超过 105 。
current，maximum 和 minimum 被调用时，update 操作 至少 已经被调用过 一次 。"""
from heapq import heappush, heappop

from sortedcontainers import SortedList
# 方法一：哈希表 + 有序集合
"""初始化时创建一个有序集合price(存储有序的股票价格)
创建一个字典time_price_map(存储对应时间戳的股票价格)
max_timestamp 存储最新价格"""
class StockPrice:

    def __init__(self):

        self.price = SortedList()
        self.time_price_map = {}
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        # 当时间戳对应的价格存在时，有序集合需要先删除该价格再增加新价格
        old_price = self.time_price_map.get(timestamp, 0)
        if old_price != 0:
            self.price.remove(old_price)
        self.price.add(price)
        self.max_timestamp = max(self.max_timestamp, timestamp)
        self.time_price_map[timestamp] = price

    def current(self) -> int:
        return self.time_price_map[self.max_timestamp]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# 方法二：哈希表 + 两个优先队列
class StockPrice:

    def __init__(self):
        self.maxPrice = []
        self.minPrice = []
        self.time_price_map = {}
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        # 用大根堆和小跟对维护最高最低价格队列
        heappush(self.maxPrice, (-price, timestamp))
        heappush(self.minPrice, (price, timestamp))
        self.max_timestamp = max(self.max_timestamp, timestamp)
        self.time_price_map[timestamp] = price

    def current(self) -> int:
        return self.time_price_map[self.max_timestamp]

    # 取出大根堆或小根堆的队首元素，当最高或最低价格不存在时，
    # 说明价格被更新过，即为过期价格，将队首元素删除，重复该过程，直到不为过期价格，返回该价格
    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxPrice[0]
            if -price == self.time_price_map[timestamp]:
                return -price
            heappop(self.maxPrice)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minPrice[0]
            if price == self.time_price_map[timestamp]:
                return price
            heappop(self.minPrice)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()











