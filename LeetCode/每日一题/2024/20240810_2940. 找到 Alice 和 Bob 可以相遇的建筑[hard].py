#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240810_2940. 找到 Alice 和 Bob 可以相遇的建筑[hard].py
# @Author  ：Lin
# @Date    ：2024/8/10 9:45


"""给你一个下标从 0 开始的正整数数组 heights ，其中 heights[i] 表示第 i 栋建筑的高度。

如果一个人在建筑 i ，且存在 i < j 的建筑 j 满足 heights[i] < heights[j] ，那么这个人可以移动到建筑 j 。

给你另外一个数组 queries ，其中 queries[i] = [ai, bi] 。第 i 个查询中，Alice 在建筑 ai ，Bob 在建筑 bi 。

请你能返回一个数组 ans ，其中 ans[i] 是第 i 个查询中，Alice 和 Bob 可以相遇的 最左边的建筑 。如果对于查询 i ，Alice 和 Bob 不能相遇，令 ans[i] 为 -1 。



示例 1：

输入：heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
输出：[2,5,-1,5,2]
解释：第一个查询中，Alice 和 Bob 可以移动到建筑 2 ，因为 heights[0] < heights[2] 且 heights[1] < heights[2] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[0] < heights[5] 且 heights[3] < heights[5] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Alice 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[3] < heights[5] 且 heights[4] < heights[5] 。
第五个查询中，Alice 和 Bob 已经在同一栋建筑中。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
示例 2：

输入：heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
输出：[7,6,-1,4,6]
解释：第一个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[0] < heights[7] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 6 ，因为 heights[3] < heights[6] 且 heights[5] < heights[6] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Bob 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 4 ，因为 heights[3] < heights[4] 且 heights[0] < heights[4] 。
第五个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[1] < heights[6] 。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。


提示：

1 <= heights.length <= 5 * 104
1 <= heights[i] <= 109
1 <= queries.length <= 5 * 104
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1"""
import bisect
from collections import deque
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(heights), len(queries)
        stack, res = deque(), []
        for i, v in enumerate(queries):
            if v[0] > v[1]:
                queries[i] = [v[1], v[0]]
        queries_copy = sorted(queries, key=lambda x: x[1], reverse=True)
        j = n - 1
        mp = {}
        for a, b in queries_copy:
            while j >= b:
                while stack and heights[stack[0]] < heights[j]:
                    stack.popleft()
                stack.appendleft(j)
                j -= 1
            if a == b or heights[a] < heights[b]:
                mp[tuple([a, b])] = b
            else:
                larger = max(heights[a], heights[b])
                k = bisect.bisect_right(stack, larger, key=(lambda x: heights[x]))
                if k == 0 and heights[a] == heights[b]:
                    k += 1
                mp[tuple([a, b])] = stack[k] if k < len(stack) else -1

        for i in range(q):
            res.append(mp[tuple(queries[i])])
        return res


s = Solution()
s.leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]])


# s.leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]])
