#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：10、栈.py
# @Author  ：Lin
# @Date    ：2024/7/18 10:25


"""20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
示例 1：
输入：s = "()"
输出：true
示例 2：
输入：s = "()[]{}"
输出：true
示例 3：
输入：s = "(]"
输出：false
提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""
import heapq
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        deq = []
        mp = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mp:
                if deq and deq[-1] == mp[char]:
                    deq.pop()
                else:
                    return False
            else:
                deq.append(char)
        return len(deq) == 0


# s = Solution()
# s.isValid(s = "()[]{}")

"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
 

示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：

-231 <= val <= 231 - 1
pop、top 和 getMin 操作总是在 非空栈 上调用
push, pop, top, and getMin最多被调用 3 * 104 次
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
提示：
1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入。
s 中所有整数的取值范围为 [1, 300] 
"""

# 栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res, multi = '', 0
        for char in s:

            if char.isdigit():
                multi = multi * 10 + int(char)
            elif char == '[':
                stack.append((res, multi))
                res, multi = '', 0
            elif char == ']':
                last_res, last_multi = stack.pop()
                res = last_res + last_multi * res

            else:
                res += char

        return res

# 回溯
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = '', 0
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res = res + tmp * multi
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


# s = Solution()
# r = s.decodeString(s = "2[abc]3[cd]ef")
# print(r)

"""
739. 每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
提示：
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, stack = len(temperatures), []
        res = [0] * n
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, stack = len(temperatures), []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx

            stack.append(i)
        return res

s = Solution()
s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])


"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2
输入： heights = [2,4]
输出： 4
提示：
1 <= heights.length <=105
0 <= heights[i] <= 104
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n
        res = 0

        for i in range(n):
            if i == 0 or heights[i] > heights[i-1]:
                left[i] = i - 1
            else:
                t = i - 1
                while t >= 0 and heights[i] <= heights[t]:
                    t = left[t]
                left[i] = t

        for i in range(n-1, -1, -1):
            if i == n - 1 or heights[i] > heights[i+1]:
                right[i] = i + 1
            else:
                t = i + 1
                while t < n and heights[i] <= heights[t]:
                    t = right[t]
                right[i] = t
            res = max(res, (right[i] - left[i] - 1) * heights[i])
        return res
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        st = []
        for i, x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        right = [n] * n
        st.clear()
        for i in range(n - 1, -1, -1):
            x = heights[i]
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans



s = Solution()
# s.largestRectangleArea(heights = [2,1,5,6,2,3])
s.largestRectangleArea(heights = [1,1])



































