#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240426_1146. 快照数组.py
# @Author  ：Lin
# @Date    ：2024/4/26 10:23


"""实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。


示例：

输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5


提示：

1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9"""

# 内存溢出
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_mp = []
        self.snapshot = {}
        self.cnt = -1

    def set(self, index: int, val: int) -> None:
        self.snapshot[index] = val

    def snap(self) -> int:
        self.cnt += 1
        self.snap_mp.append(self.snapshot.copy())
        return self.cnt

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_mp[snap_id].get(index, 0)

# 二分
class SnapshotArray:

    def __init__(self, length: int):
        self.cnt = 0
        self.data = [[] for _ in range(length)]
        print(self.data)

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.cnt, val))

    def snap(self) -> int:
        ans = self.cnt
        self.cnt += 1
        return ans

    def get(self, index: int, snap_id: int) -> int:
        x = bisect.bisect_right(self.data[index], (snap_id+1, -1))
        return 0 if x == 0 else self.data[index][x-1][1]


s = SnapshotArray(10)


["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
[[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
























