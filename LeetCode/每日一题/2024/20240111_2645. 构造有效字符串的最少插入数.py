#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240111_2645. 构造有效字符串的最少插入数.py
# @Author  ：Lin
# @Date    ：2024/1/11 15:07

""""给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。

如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。



示例 1：

输入：word = "b"
输出：2
解释：在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "abc" 。
示例 2：

输入：word = "aaa"
输出：6
解释：在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "abcabcabc" 。
示例 3：

输入：word = "abc"
输出：0
解释：word 已经是有效字符串，不需要进行修改。


提示：

1 <= word.length <= 50
word 仅由字母 "a"、"b" 和 "c" 组成。"""


class Solution:
    def addMinimum(self, word: str) -> int:
        mp = {'a': 1, 'b': 2, 'c': 3}
        res = mp[word[0]] - mp[word[-1]] + 2
        for i in range(1, len(word)):
            res += (mp[word[i]] - 1 - mp[word[i-1]]) % 3

        return res


"""方法三：计算组数
思路与算法

方法二中提到，如果当前字符小于等于前面字符说明它们一定不在同一组中，反之则一定在同一组中。
因此如果我们知道了最终的组数，就可以直接计算需要添加的字符数量。
而最终的组数，就等于所有满足后者字符小于等于前者字符的情况数再加1。
"""


class Solution:
    def addMinimum(self, word: str) -> int:
        n, cnt = len(word), 1
        for i in range(1, n):
            if word[i] <= word[i - 1]:
                cnt += 1
        return cnt * 3 - n


s = Solution()
s.addMinimum(word = "aaa")
