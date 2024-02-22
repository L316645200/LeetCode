#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231125_1410. HTML 实体解析器.py
# @Author  ：Lin
# @Date    ：2023/11/25 11:27


"""「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。

HTML 里这些特殊字符和它们对应的字符实体包括：

双引号：字符实体为 &quot; ，对应的字符是 " 。
单引号：字符实体为 &apos; ，对应的字符是 ' 。
与符号：字符实体为 &amp; ，对应对的字符是 & 。
大于号：字符实体为 &gt; ，对应的字符是 > 。
小于号：字符实体为 &lt; ，对应的字符是 < 。
斜线号：字符实体为 &frasl; ，对应的字符是 / 。
给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。



示例 1：

输入：text = "&amp; is an HTML entity but &ambassador; is not."
输出："& is an HTML entity but &ambassador; is not."
解释：解析器把字符实体 &amp; 用 & 替换
示例 2：

输入：text = "and I quote: &quot;...&quot;"
输出："and I quote: \"...\""
示例 3：

输入：text = "Stay home! Practice on Leetcode :)"
输出："Stay home! Practice on Leetcode :)"
示例 4：

输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
输出："x > y && x < y is always false"
示例 5：

输入：text = "leetcode.com&frasl;problemset&frasl;all"
输出："leetcode.com/problemset/all"


提示：

1 <= text.length <= 10^5
字符串可能包含 256 个ASCII 字符中的任意字符。"""


class Solution:
    def entityParser(self, text: str) -> str:
        parser = {'&quot;': '"',
                  '&apos;': "'",
                  "&amp;": "&",
                  "&gt;": ">",
                  "&lt;": "<",
                  "&frasl;": "/"}
        i = 0
        n = len(text)
        res = ""
        while i < n:
            is_valid = True
            if text[i] == "&":
                s = "&"
                while is_valid:
                    i += 1
                    if i == n or text[i] == "&":
                        is_valid = False
                    else:
                        s += text[i]
                        if s in parser:
                            s = parser[s]
                            i += 1
                            is_valid = False
                res += s
            else:
                res += text[i]
                i += 1
        return res
# 官解
# class Solution:
#     def entityParser(self, text: str) -> str:
#         entityMap = {
#             '&quot;': '"',
#             '&apos;': "'",
#             '&gt;': '>',
#             '&lt;': '<',
#             '&frasl;': '/',
#             '&amp;': '&',
#         }
#
#         i = 0
#         n = len(text)
#         res = []
#         while i < n:
#             isEntity = False
#             if text[i] == '&':
#                 for e in entityMap:
#                     if text[i:i + len(e)] == e:
#                         res.append(entityMap[e])
#                         isEntity = True
#                         i += len(e)
#                         break
#             if not isEntity:
#                 res.append(text[i])
#                 i += 1
#         return ''.join(res)

s = Solution()
s.entityParser(text = "&&gt;")