#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：1.2 进阶（选做）.py
# @Author  ：Lin
# @Date    ：2024/9/14 11:02

"""2134. 最少交换次数来组合所有的 1 II 1748
交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
示例 1：
输入：nums = [0,1,0,1,1,0,0]
输出：1
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[0,0,1,1,1,0,0] 交换 1 次。
[0,1,1,1,0,0,0] 交换 1 次。
[1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 1 。
示例 2：
输入：nums = [0,1,1,1,0,0,1,1,0]
输出：2
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
[1,1,1,1,1,0,0,0,0] 交换 2 次。
无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 2 。
示例 3：
输入：nums = [1,1,0,0,1]
输出：0
解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
因此，需要的最少交换次数为 0 。
提示：
1 <= nums.length <= 105
nums[i] 为 0 或者 1
"""
from collections import Counter
from typing import List

"""
先统计出数组1的个数，记为total，这个数值即为我们要维护的滑动窗口的长度
该长度内有多少个0即为我们要交换的次数，维护这个次数的最小值
因为是环形数组，所有我们要从[0,total-1]滑动到[n-1,n+total-1]
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        if total <= 1:
            return 0
        n = len(nums)
        cnt, res = 0, n
        for i in range(n+total):
            if nums[i % n] == 0:
                cnt += 1
            if i >= total - 1:
                res = min(res, cnt)
                if nums[(i-total+1) % n] == 0:
                    cnt -= 1
        return res


# s = Solution()
# s.minSwaps(nums = [1,1,0,0,1])
# s.minSwaps([0,0,1])


"""1888. 使二进制字符串字符交替的最少反转次数 2006
给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：
类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。
我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。
比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
示例 1：
输入：s = "111000"
输出：2
解释：执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
示例 2：
输入：s = "010"
输出：0
解释：字符串已经是交替的。
示例 3：
输入：s = "1110"
输出：1
解释：对第二个字符执行第二种操作，得到 s = "1010" 。
提示：
1 <= s.length <= 105
s[i] 要么是 '0' ，要么是 '1' 。
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        """①当字符串长度为偶数时,交替字符串是010101或者是101010，
        
        ②当字符串长度是奇数时，交替字符串是1010101或者是0101010，
        因为在类型1的操作下
        s可以是 01...010|01...01的形式，或者是10...10|01...010的形式，
        通过类型1的操作可以得到交替字符串
        """
        _s = "10" * (n // 2) + "1" * (n % 2)
        cnt = 0
        for i in range(n):
            if s[i] == _s[i]:
                cnt += 1
        if n % 2 == 0:
            return min(cnt, n - cnt)

        res = cnt
        for c in s:
            """在类型1的操作下，如果第一个字符是1，那么1移动到字符串结尾是相同的
            那么与交替字符串相同字符的数量是 (n-1)-(cnt-1)+1=n-cnt+1。
            如果第一个字符是0，(n-1)-(cnt-1)-1=n-cnt-1            
            """
            if c == '1':
                cnt = n - cnt + 1
            else:
                cnt = n - cnt - 1
            res = min(res, cnt, n - cnt)
        return res

# s = Solution()
# s.minFlips(s = "1110001")


"""567. 字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。
示例 1：
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：
输入：s1= "ab" s2 = "eidboaoo"
输出：false
提示：
1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 计数数组
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(len(s1)):
            cnt1[ord(s1[i])-97] += 1
        n1 = len(s1)
        for i in range(len(s2)):
            cnt2[ord(s2[i]) - 97] += 1
            if i >= n1 - 1:
                if cnt1 == cnt2:
                    return True
                cnt2[ord(s2[i-n1+1]) - 97] -= 1
        return False


s = Solution()
s.checkInclusion(s1 = "ab", s2 = "eidbaooo")


"""438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:
1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 计数数组
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(len(p)):
            cnt1[ord(p[i])-97] += 1

        n = len(p)
        ans = []
        for i in range(len(s)):
            cnt2[ord(s[i]) - 97] += 1
            if i >= n - 1:
                if cnt1 == cnt2:
                    ans.append(i-n+1)
                cnt2[ord(s[i-n+1]) - 97] -= 1

        return ans
# s = Solution()
# s.findAnagrams(s = "cbaebabacd", p = "abc")


"""30. 串联所有单词的子串
给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
 s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
示例 1：
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
示例 2：
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。
示例 3：
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
提示：
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 和 s 由小写英文字母组成
"""


"""思路：
记s的长度为m，words的长度为n，words中每个单词的长度为k。
首先需要将 s 划分为单词组，每个单词的大小均为 k （首尾除外）。
这样的划分方法有 k 种，即先删去前 i （i=0∼k−1）个字母后，
将剩下的字母进行划分，如果末尾有不到 k 个字母也删去。
对这 k 种划分得到的单词数组分别使用滑动窗口对 words 进行类似于「字母异位词」的搜寻。

划分成单词组后，一个窗口包含 s 中前 k 个单词，
用一个哈希表 differ 表示窗口中单词频次和 words 中单词频次之差。
初始化 differ 时，出现在窗口中的单词，每出现一次，相应的值增加 1，出现在 words 中的单词，
每出现一次，相应的值减少 1。然后将窗口右移，右侧会加入一个单词，左侧会移出一个单词，
并对 differ 做相应的更新。窗口移动时，若出现 differ 中值不为 0 的键的数量为 0，
则表示这个窗口中的单词频次和 words 中单词频次相同，窗口的左端点是一个待求的起始位置。
划分的方法有 k 种，做 k 次滑动窗口后，即可找到所有的起始位置。

"""
# 哈希
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt1 = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        wl = k * n
        res = []
        #
        for i in range(k):
            cnt2 = Counter()

            for j in range(i, m, k):
                end = j + k
                cnt2[s[j:end]] += 1

                if end - i >= wl:
                    if cnt1 == cnt2:
                        res.append(end - wl)
                    word = s[end - wl: end - wl + k]
                    cnt2[word] -= 1
                    if cnt2[word] == 0:
                        del cnt2[word]
        return res


# s = Solution()
# s.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
# s.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"])
# s.findSubstring(s = "aaa", words = ["a","a"])


"""2953. 统计完全子字符串 2449
给你一个字符串 word 和一个整数 k 。
如果 word 的一个子字符串 s 满足以下条件，我们称它是 完全字符串：
s 中每个字符 恰好 出现 k 次。
相邻字符在字母表中的顺序 至多 相差 2 。也就是说，s 中两个相邻字符 c1 和 c2 ，它们在字母表中的位置相差 至多 为 2 。
请你返回 word 中 完全 子字符串的数目。
子字符串 指的是一个字符串中一段连续 非空 的字符序列。
示例 1：
输入：word = "igigee", k = 2
输出：3
解释：完全子字符串需要满足每个字符恰好出现 2 次，且相邻字符相差至多为 2 ：igigee, igigee, igigee 。
示例 2：
输入：word = "aaabbbccc", k = 3
输出：6
解释：完全子字符串需要满足每个字符恰好出现 3 次，且相邻字符相差至多为 2 ：aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc 。
提示：
1 <= word.length <= 105
word 只包含小写英文字母。
1 <= k <= word.length
"""


"""「相邻字母相差至多为 2」这个约束把 word 划分成了多个子串 s，每个子串分别处理。
可以用 分组循环 找到每个子串 s。

对于每个子串，由于每个字符恰好出现 k 次，我们可以枚举有 m 种字符，这样问题就变成了：

长度固定为 m⋅k 的滑动窗口，判断每种字符是否都出现了恰好 k 次。"""
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:

        def f(s: str):
            res = 0
            for m in range(1, 27):
                if m * k > len(s):
                    break
                cnt = Counter()

                for j in range(len(s)):
                    cnt[s[j]] += 1

                    if j + 1 >= m * k:
                        res += all([i == 0 or i == k for i in cnt.values()])
                        cnt[s[j+1-m*k]] -= 1
            return res

        n = len(word)

        ans = i = 0
        while i < n:
            st = i
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i-1])) <= 2:
                i += 1
            ans += f(word[st: i])
        return ans


s = Solution()
s.countCompleteSubstrings(word = "igigee", k = 2)


# s.countCompleteSubstrings(word = "aaabbbccc", k = 3)
# s.countCompleteSubstrings(word = "aaa", k = 1)









































