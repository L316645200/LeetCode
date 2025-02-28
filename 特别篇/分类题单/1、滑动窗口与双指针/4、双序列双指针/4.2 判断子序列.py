#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：4.2 判断子序列.py
# @Author  ：Lin
# @Date    ：2024/12/9 15:21
"""
392. 判断子序列
524. 通过删除字母匹配到字典里最长单词
2486. 追加字符以获得子序列 1363
2825. 循环增长使字符串子序列等于另一个字符串 1415
1023. 驼峰式匹配 1537
3132. 找出与数组相加的整数 II 1620
522. 最长特殊序列 II ~1700
"""
from typing import List

"""392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
致谢：
特别感谢 @pbrother 添加此问题并且创建所有测试用例。
示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false
提示：
0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。"""


# 双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        l = r = 0
        while l < n and r < m:
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        return l == n


"""方法二：动态规划
思路及算法
考虑前面的双指针的做法，我们注意到我们有大量的时间用于在 t 中找到下一个匹配字符。
这样我们可以预处理出对于 t 的每一个位置，从该位置开始往后每一个字符第一次出现的位置。
我们可以使用动态规划的方法实现预处理，令 f[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。在进行状态转移时，如果 t 中位置 i 的字符就是 j，那么 f[i][j]=i，否则 j 出现在位置 i+1 开始往后，即 f[i][j]=f[i+1][j]，因此我们要倒过来进行动态规划，从后往前枚举 i。
这样我们可以写出状态转移方程：
 
假定下标从 0 开始，那么 f[i][j] 中有 0≤i≤m−1 ，对于边界状态 f[m−1][..]，我们置 f[m][..] 为 m，让 f[m−1][..] 正常进行转移。这样如果 f[i][j]=m，则表示从位置 i 开始往后不存在字符 j。
这样，我们可以利用 f 数组，每次 O(1) 地跳转到下一个位置，直到位置变为 m 或 s 中的每一个字符都匹配成功。
同时我们注意到，该解法中对 t 的处理与 s 无关，且预处理完成后，可以利用预处理数组的信息，线性地算出任意一个字符串 s 是否为 t 的子串。这样我们就可以解决「后续挑战」啦。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == (j + ord('a')) else f[i+1][j]
        add = 0

        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        return True

# s = Solution()
# s.isSubsequence(s = "abc", t = "ahbgdc")

"""524. 通过删除字母匹配到字典里最长单词
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
示例 1：
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
示例 2：
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
提示：
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s 和 dictionary[i] 仅由小写英文字母组成
"""

# 双指针
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        res = ''
        for char in dictionary:
            m = len(char)
            l = r = 0
            while l < n and r < m:
                if s[l] == char[r]:
                    r += 1
                l += 1
            # (r > len(res) or (r == len(res) and char < res)) 可以 改为对dictionary排序处理
            if r == m and (r > len(res) or (r == len(res) and char < res)):
                res = char
        return res


# 动态规划(预处理原字符串)
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        dictionary.sort(key=lambda x: (-len(x), x))

        f = [[0] * 26 for _ in range(n)]
        f.append([n] * 26)

        for i in range(n-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(s[i]) == (j + ord('a')) else f[i+1][j]

        res = ''
        for char in dictionary:
            add = 0
            for i, c in enumerate(char):
                if f[add][ord(c) - ord('a')] == n:
                    break
                add = f[add][ord(c) - ord('a')] + 1
                if i == len(char) - 1:
                    res = char
                    return res
        return res


# s = Solution()
# s.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"])
# s.findLongestWord(s = "abce", dictionary = ["abe","abc",])

"""2486. 追加字符以获得子序列 1363
给你两个仅由小写英文字母组成的字符串 s 和 t 。
现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。
子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。
示例 1：
输入：s = "coaching", t = "coding"
输出：4
解释：向 s 末尾追加字符串 "ding" ，s = "coachingding" 。
现在，t 是 s ("coachingding") 的一个子序列。
可以证明向 s 末尾追加任何 3 个字符都无法使 t 成为 s 的一个子序列。
示例 2：
输入：s = "abcde", t = "a"
输出：0
解释：t 已经是 s ("abcde") 的一个子序列。
示例 3：
输入：s = "z", t = "abcde"
输出：5
解释：向 s 末尾追加字符串 "abcde" ，s = "zabcde" 。
现在，t 是 s ("zabcde") 的一个子序列。 
可以证明向 s 末尾追加任何 4 个字符都无法使 t 成为 s 的一个子序列。
提示：
1 <= s.length, t.length <= 105
s 和 t 仅由小写英文字母组成
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        l = r = 0
        while l < m and r < n:
            if s[l] == t[r]:
                r += 1
            l += 1
        return n - r + 1

# s = Solution()
# s.appendCharacters(s = "coaching", t = "coding")

"""2825. 循环增长使字符串子序列等于另一个字符串 1415
给你一个下标从 0 开始的字符串 str1 和 str2 。
一次操作中，你选择 str1 中的若干下标。对于选中的每一个下标 i ，你将 str1[i] 循环 递增，变成下一个字符。也就是说 'a' 变成 'b' ，'b' 变成 'c' ，以此类推，'z' 变成 'a' 。
如果执行以上操作 至多一次 ，可以让 str2 成为 str1 的子序列，请你返回 true ，否则返回 false 。
注意：一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。
示例 1：
输入：str1 = "abc", str2 = "ad"
输出：true
解释：选择 str1 中的下标 2 。
将 str1[2] 循环递增，得到 'd' 。
因此，str1 变成 "abd" 且 str2 现在是一个子序列。所以返回 true 。
示例 2：
输入：str1 = "zc", str2 = "ad"
输出：true
解释：选择 str1 中的下标 0 和 1 。
将 str1[0] 循环递增得到 'a' 。
将 str1[1] 循环递增得到 'd' 。
因此，str1 变成 "ad" 且 str2 现在是一个子序列。所以返回 true 。
示例 3：
输入：str1 = "ab", str2 = "d"
输出：false
解释：这个例子中，没法在执行一次操作的前提下，将 str2 变为 str1 的子序列。
所以返回 false 。
提示：
1 <= str1.length <= 105
1 <= str2.length <= 105
str1 和 str2 只包含小写英文字母。
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        j = 0
        for i in range(m):
            if str1[i] == str2[j] or ord(str1[i]) == ((ord(str2[j]) - ord('a') - 1) % 26 + ord('a')):
                j += 1
                if j == n:
                    return True
        return False
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        j = 0
        for b in str1:
            c = chr(ord(b) + 1) if b != 'z' else 'a'
            if str2[j] == b or str2[j] == c:
                j += 1
                if j == n:
                    return True
        return False

# s = Solution()
# s.canMakeSubsequence(str1 = "abc", str2 = "ad")

"""1023. 驼峰式匹配 1537
给你一个字符串数组 queries，和一个表示模式的字符串 pattern，请你返回一个布尔数组 answer 。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。
如果可以将小写字母插入模式串 pattern 得到待查询项 queries[i]，那么待查询项与给定模式串匹配。可以在任何位置插入每个字符，也可以不插入字符。
示例 1：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
示例 2：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
示例 3：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输出：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
提示：
1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] 和 pattern 由英文字母组成
"""


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(pattern)
        # 初始化结果列表
        res = []
        # 遍历查询字符串列表
        for char in queries:
            # 获取当前查询字符串的长度
            m = len(char)
            # 初始化查询字符串和模式字符串的索引
            i, j = 0, 0
            # 当查询字符串和模式字符串的索引都未超出各自的长度时
            while i < m and j < n:
                if char[i] == pattern[j]:
                    i += 1
                    j += 1
                # 如果当前字符不匹配，且查询字符串的字符是大写字母
                elif char[i].isupper():
                    break
                # 如果当前字符不匹配，且查询字符串的字符是小写字母
                else:
                    i += 1
            # 当查询字符串的索引未超出其长度时
            while i < m and char[i].islower():
                i += 1
            # 将当前查询字符串是否与模式字符串完全匹配的结果添加到结果列表中
            res.append(i == m and j == n)
        # 返回结果列表
        return res
# s = Solution()
# s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB")

# s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT")

"""3132. 找出与数组相加的整数 II 1620
给你两个整数数组 nums1 和 nums2。
从 nums1 中移除两个元素，并且所有其他元素都与变量 x 所表示的整数相加。如果 x 为负数，则表现为元素值的减少。
执行上述操作后，nums1 和 nums2 相等 。当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。
返回能够实现数组相等的 最小 整数 x 。
示例 1:
输入：nums1 = [4,20,16,12,8], nums2 = [14,18,10]
输出：-2
解释：
移除 nums1 中下标为 [0,4] 的两个元素，并且每个元素与 -2 相加后，nums1 变为 [18,14,10] ，与 nums2 相等。
示例 2:
输入：nums1 = [3,5,5,3], nums2 = [7,7]
输出：2
解释：
移除 nums1 中下标为 [0,3] 的两个元素，并且每个元素与 2 相加后，nums1 变为 [7,7] ，与 nums2 相等。
提示：
3 <= nums1.length <= 200
nums2.length == nums1.length - 2
0 <= nums1[i], nums2[i] <= 1000
测试用例以这样的方式生成：存在一个整数 x，nums1 中的每个元素都与 x 相加后，再移除两个元素，nums1 可以与 nums2 相等。
"""


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        m, n = len(nums1), len(nums2)
        for k in range(2, -1, -1):
            i, j = 0, 0
            x = nums2[j] - nums1[i + k]
            while i + k < m and j < n:
                if nums1[i + k] + x == nums2[j]:
                    j += 1
                i += 1
            if j == n:
                return x


# s = Solution()
# s.minimumAddedInteger(nums1 = [7,2,6,8,7], nums2 = [7,6,5])

"""522. 最长特殊序列 II ~1700
给定字符串列表 strs ，返回其中 最长的特殊序列 的长度。如果最长特殊序列不存在，返回 -1 。
特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 s 的 子序列可以通过删去字符串 s 中的某些字符实现。
例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
示例 1：
输入: strs = ["aba","cdc","eae"]
输出: 3
示例 2:
输入: strs = ["aaa","aaa","aa"]
输出: -1
提示:
2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] 只包含小写英文字母
"""

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            sub_i, sub_j = 0, 0
            while sub_i < len(s) and sub_j < len(t):
                if s[sub_i] == t[sub_j]:
                    sub_j += 1
                sub_i += 1
            return sub_j == len(t)

        strs.sort(key=lambda x: len(x), reverse=True)

        for i, t in enumerate(strs):
            check = False
            for j, s in enumerate(strs):
                if i == j:
                    continue
                elif len(t) > len(s):
                    break
                if is_subseq(s, t):
                    check = True
            if not check:
                return len(t)
        return -1


# s = Solution()
# s.findLUSlength(strs = ["aba","cdc","eae"])

"""1898. 可移除字符的最大数目 1913
给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
请你找出一个整数 k（0 <= k <= removable.length），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。
示例 1：
输入：s = "abcacb", p = "ab", removable = [3,1,0]
输出：2
解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
"ab" 是 "accb" 的一个子序列。
如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
因此，最大的 k 是 2 。
示例 2：
输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
输出：1
解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
"abcd" 是 "abcddddd" 的一个子序列。
示例 3：
输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
输出：0
解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
提示：
1 <= p.length <= s.length <= 105
0 <= removable.length < s.length
0 <= removable[i] < s.length
p 是 s 的一个 子字符串
s 和 p 都由小写英文字母组成
removable 中的元素 互不相同
"""


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subseq(s: str, p: str) -> bool:
            sub_i, sub_j = 0, 0
            while sub_i < len(s) and sub_j < len(p):
                if s[sub_i] == p[sub_j]:
                    sub_j += 1
                sub_i += 1
            return sub_j == len(p)

        n = len(removable)
        s_arr = list(s)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            m_remove = set(removable[:mid+1])
            char = ''.join([c for i, c in enumerate(s_arr) if i not in m_remove])
            if is_subseq(char, p):
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)

        def check(k):
            state = [True] * ns
            for i in range(k+1):
                state[removable[i]] = False
            sub_i, sub_j = 0, 0
            while sub_i < ns and sub_j < np:
                if state[sub_i] and s[sub_i] == p[sub_j]:
                    sub_j += 1
                sub_i += 1
            return sub_j == np

        n = len(removable)

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


s = Solution()
s.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0])





# TODO

"""
2565. 最少得分子序列 2432
3302. 字典序最小的合法序列 2474"""


































