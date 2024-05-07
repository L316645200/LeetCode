#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240321_2671. 频率跟踪器.py
# @Author  ：Lin
# @Date    ：2024/3/21 11:46

"""请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。
实现 FrequencyTracker 类：
FrequencyTracker()：使用一个空数组初始化 FrequencyTracker 对象。
void add(int number)：添加一个 number 到数据结构中。
void deleteOne(int number)：从数据结构中删除一个 number 。数据结构 可能不包含 number ，在这种情况下不删除任何内容。
bool hasFrequency(int frequency): 如果数据结构中存在出现 frequency 次的数字，则返回 true，否则返回 false。
示例 1：
输入
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
输出
[null, null, null, true]
解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.add(3); // 数据结构现在包含 [3, 3]
frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现 2 次
示例 2：
输入
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
输出
[null, null, null, false]
解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // 数据结构现在包含 [1]
frequencyTracker.deleteOne(1); // 数据结构现在为空 []
frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结构为空
示例 3：
输入
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
输出
[null, false, null, true]
解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结构为空
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现 1 次
提示：
1 <= number <= 105
1 <= frequency <= 105
最多调用 add、deleteOne 和 hasFrequency 共计 2 * 105 次"""

from collections import defaultdict, Counter

class FrequencyTracker:
    def __init__(self):
        self.nums = {}
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        if number not in self.nums:
            self.nums[number] = 1
            self.cnt[1] += 1
        else:
            k = self.nums[number]
            self.cnt[k] -= 1
            if self.cnt[k] == 0:
                self.cnt.pop(k)
            self.nums[number] += 1
            self.cnt[self.nums[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.nums:
            k = self.nums[number]
            self.cnt[k] -= 1
            if self.cnt[k] == 0:
                self.cnt.pop(k)
            if k - 1 > 0:
                self.cnt[k-1] += 1
            self.nums[number] -= 1
            if self.nums[number] == 0:
                self.nums.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return self.cnt.get(frequency, 0) > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
class FrequencyTracker:
    def __init__(self):
        self.nums = defaultdict(int)
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        self.cnt[self.nums[number]] -= 1
        self.nums[number] += 1
        self.cnt[self.nums[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.nums[number] > 0:
            self.cnt[self.nums[number]] -= 1
            self.nums[number] -= 1
            self.cnt[self.nums[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.cnt.get(frequency, 0) > 0



f = FrequencyTracker()
lis = ["hasFrequency","add","hasFrequency","hasFrequency","add","add","add","deleteOne","deleteOne","hasFrequency","add","hasFrequency","hasFrequency"]
l = [[1],[3],[1],[1],[6],[2],[6],[6],[6],[2],[2],[2],[1]]
for i, n in zip(lis, [j[0] for j in l]):
    getattr(f, i)
    method = getattr(f, i)
    method(n)
    print(i, n, f.freq, f.freq_cnt)
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)