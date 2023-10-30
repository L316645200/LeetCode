#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230918_337. 打家劫舍 III.py
# @Author: Lin
# @Date  : 2023/9/18 10:31


"""小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。



示例 1:



输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
示例 2:



输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9


提示：

树的节点数在 [1, 104] 范围内
0 <= Node.val <= 104"""


"""当 ooo 被选中时，ooo 的左右孩子都不能被选中，
故 ooo 被选中情况下子树上被选中点的最大权值和为 lll 和 rrr 不被选中的最大权值和相加，
即 f(o)=o.val+g(l)+g(r)。

当 ooo 不被选中时，ooo 的左右孩子可以被选中，也可以不被选中。
对于 ooo 的某个具体的孩子 xxx，
它对 ooo 的贡献是 xxx 被选中和不被选中情况下权值和的较大值。
故 g(o)=max{f(l),g(l)}+max{f(r),g(r)}。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g.get(node.left, 0) + g.get(node.right, 0)
            g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + max(f.get(node.right, 0), g.get(node.right, 0))

        f, g = dict(), dict()
        dfs(root)
        return max(f.get(root, 0), g.get(root, 0))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            selected = node.val + l[1] + r[1]
            notselected = max(l[0], l[1]) + max(r[0], r[1])
            return [selected, notselected]

        root_status = dfs(root)
        return max(root_status)

s = Solution()
s.rob(root = [3,2,3,None,3,None,1])