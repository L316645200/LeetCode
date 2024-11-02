#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：AC自动机.py
# @Author  ：Lin
# @Date    ：2024/10/26 15:21
from collections import deque


# 节点类
class node:
    def __init__(self, ch):
        self.ch = ch    # 节点值
        self.fail = None  # Fail指针
        self.tail = 0   # 尾标志：标志为i 表示第i个模式串串尾
        self.child = []  # 子节点
        self.childvalue = []  # 子节点的值


# AC自动机类
class acmation:
    def __init__(self):
        self.root = node("")  #初始化根节点类
        self.count = 0  # 模式串个数

    # 第一步：模式串建树
    def insert(self, strkey):
        # 插入模式串种，模式串数量加+1
        self.count += 1
        p = self.root
        for i in strkey:
            #如字符不存在，添加子节点
            if i not in p.childvalue:
                child = node(i)
                p.child.append(child)
                p.childvalue.append(i)
                p = child
            # 否则，转到子节点
            else:
                p = p.child[p.childvalue.index(i)]
        p.tail = self.count # 修改尾节点


    #第二步：修改Fail指针
    def ac_automation(self):
        queuelist = deque([self.root])
        #用BFS遍历字典树
        while len(queuelist):
            #取出队首元素
            temp = queuelist.popleft()
            for i in temp.child:
                # 根的子节点Fail指向根自己
                if temp == self.root:
                    i.fail = self.root
                else:
                    # 转到Fail指针
                    p = temp.fail
                    while p:
                        if i.ch in p.childvalue:
                            #若节点值在该节点的子节点种，则将Fail指向该节点的对应子节点
                            i.fail = p.child[p.childvalue.index(i.ch)]
                            break
                        # 否则，转到Fail指针继续回溯
                        p = p.fail
                    if not p:
                        # 若p==None,表示当前节点值在之前都没出现过，则其Fail指向根节点
                        i.fail = self.root
                # 将当前节点的所有子节点加到队列中
                queuelist.append(i)

    # 第三步：模式匹配
    def runkmp(self, strmode):
        p = self.root
        cnt = {}  # 使用字典记录成功匹配的状态

        for i in strmode:  # 遍历目标串
            while i not in p.childvalue and p is not self.root:
                p = p.fail
            if i in p.childvalue:
                # 若找到匹配成功的字符节点，则指向那个节点，否则指向根节点
                p = p.child[p.childvalue.index(i)]
            else:
                p = self.root
            temp = p
            while temp is not self.root:
                if temp.tail:  # 尾标志为0不处理
                    if temp.tail not in cnt:
                        cnt[temp.tail] = 1
                    else:
                        cnt[temp.tail] += 1
                temp = temp.fail
        # 返回匹配状态
        return cnt
        # 如果只需要知道是否匹配成功，则return bool(cnt)即可
        # 如果需要知道成功匹配的模式串种数，则 return len(cnt)即可


if __name__ == '__main__':
    # acmation 实现
    ac = acmation()
    dic = ['anyway', 'fantastic', 'however']
    for i in dic:
        ac.insert(i)
    ac.ac_automation()
    result = ac.runkmp('however, anyway just fantastic however')

    print(result)











