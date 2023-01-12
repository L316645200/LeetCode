#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220321_653. 两数之和 IV - 输入 BST.py
# @Author: Lin
# @Date  : 2022/3/21 9:25

#
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 示例 1：
# 输入: root = [5,3,6,2,4,null,7], k = 9
# 输出: true
# 示例 2：
# 输入: root = [5,3,6,2,4,null,7], k = 28
# 输出: false
# 提示:
#
# 二叉树的节点个数的范围是  [1, 104].
# -104 <= Node.val <= 104
# root 为二叉搜索树
# -105 <= k <= 105
from typing import Optional


class Solution:
    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

