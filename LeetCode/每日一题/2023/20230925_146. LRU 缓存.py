#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230925_146. LRU 缓存.py
# @Author: Lin
# @Date  : 2023/9/25 10:34

"""请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put"""
import collections
from collections import OrderedDict

# OrderedDict有序字典
class LRUCache():

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# class LRUCache(collections.OrderedDict):
#
#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity
#
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)



class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if not self.cache.get(key):
            # 创建节点
            node = DLinkedNode(key, value)
            self.cache[key] = node

            # 添加节点到头部
            self.add_to_head(node)

            self.size += 1
            # 超出容量则删除队尾
            if self.size > self.capacity:
                self.cache.pop(self.tail.prev.key)
                # self.tail.prev.prev.next = self.tail
                # self.tail.prev = self.tail.prev.prev
                self.remove_node(self.tail.prev)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def move_to_head(self, node):
        # 移除node
        self.remove_node(node)
        # 添加到头部
        self.add_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lur = LRUCache(2)
f = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
v = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

for i in range(1, len(f)):
    func = getattr(lur, f[i])
    if f[i] == 'get':
        r = func(v[i][0])
    else:
        r = func(v[i][0], v[i][1])
    print(r)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


