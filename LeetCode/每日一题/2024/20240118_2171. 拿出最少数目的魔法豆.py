#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240118_2171. 拿出最少数目的魔法豆.py
# @Author  ：Lin
# @Date    ：2024/1/18 11:58


"""给定一个 正整数 数组 beans ，其中每个整数表示一个袋子里装的魔法豆的数目。

请你从每个袋子中 拿出 一些豆子（也可以 不拿出），使得剩下的 非空 袋子中（即 至少还有一颗 魔法豆的袋子）魔法豆的数目 相等。一旦把魔法豆从袋子中取出，你不能再将它放到任何袋子中。

请返回你需要拿出魔法豆的 最少数目。



示例 1：

输入：beans = [4,1,6,5]
输出：4
解释：
- 我们从有 1 个魔法豆的袋子中拿出 1 颗魔法豆。
  剩下袋子中魔法豆的数目为：[4,0,6,5]
- 然后我们从有 6 个魔法豆的袋子中拿出 2 个魔法豆。
  剩下袋子中魔法豆的数目为：[4,0,4,5]
- 然后我们从有 5 个魔法豆的袋子中拿出 1 个魔法豆。
  剩下袋子中魔法豆的数目为：[4,0,4,4]
总共拿出了 1 + 2 + 1 = 4 个魔法豆，剩下非空袋子中魔法豆的数目相等。
没有比取出 4 个魔法豆更少的方案。
示例 2：

输入：beans = [2,10,3,2]
输出：7
解释：
- 我们从有 2 个魔法豆的其中一个袋子中拿出 2 个魔法豆。
  剩下袋子中魔法豆的数目为：[0,10,3,2]
- 然后我们从另一个有 2 个魔法豆的袋子中拿出 2 个魔法豆。
  剩下袋子中魔法豆的数目为：[0,10,3,0]
- 然后我们从有 3 个魔法豆的袋子中拿出 3 个魔法豆。
  剩下袋子中魔法豆的数目为：[0,10,0,0]
总共拿出了 2 + 2 + 3 = 7 个魔法豆，剩下非空袋子中魔法豆的数目相等。
没有比取出 7 个魔法豆更少的方案。


提示：

1 <= beans.length <= 105
1 <= beans[i] <= 105"""
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n, ans = len(beans), float('inf')
        # 构造前缀和
        prefix = [beans[0]] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + beans[i]
        """由题意，袋子里的魔法豆要么全部拿空，要么拿出至与某一个袋子的魔法豆相同，
        可以先对数组排序，遍历数组，计算遍历当前袋子初始魔法豆数目作为相等魔法豆要去除魔法豆的数组，
        取最小值即为最终答案。
        
        每次遍历时，左边的魔法豆全部拿出，右边的魔法豆拿出至与当前袋子的魔法豆相同即可。
        
        """
        for i in range(n):
            left = prefix[i-1] if i > 0 else 0
            right = (prefix[n-1] - left) - beans[i] * (n - i)
            ans = min(ans, left + right)
        return ans

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        n, ans = len(beans), total
        """由题意，袋子里的魔法豆要么全部拿空，要么拿出至与某一个袋子的魔法豆相同，
        可以先对数组排序，遍历数组，计算遍历当前袋子初始魔法豆数目作为相等魔法豆要去除魔法豆的数组，
        取最小值即为最终答案。

        每次遍历时，左边的魔法豆全部拿出，右边的魔法豆拿出至与当前袋子的魔法豆相同即可。

        """
        for i in range(n):
            ans = min(ans, total - beans[i] * (n - i))
        return ans


s = Solution()
s.minimumRemoval(beans = [4,1,6,5])