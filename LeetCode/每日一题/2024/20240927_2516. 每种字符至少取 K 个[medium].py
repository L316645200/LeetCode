#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240927_2516. 每种字符至少取 K 个[medium].py
# @Author  ：Lin
# @Date    ：2024/9/27 11:04


"""给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
示例 1：
输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
示例 2：
输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
提示：
1 <= s.length <= 105
s 仅由字母 'a'、'b'、'c' 组成
0 <= k <= s.length"""
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        cnt = Counter()
        n = len(s)
        is_k = left = 0
        right = n
        # 正序每个字符至少取k个
        for i in range(n-1, -1, -1):
            cnt[s[i]] += 1
            if cnt[s[i]] == k:
                is_k += 1
                if is_k == 3:
                    left = i
                    break
        if is_k < 3:
            return -1
        res = right - left

        for j in range(n, n + res):
            while is_k == 3 and left <= n:
                print(j, left)
                res = min(res, j - left)

                cnt[s[left % n]] -= 1
                if cnt[s[left % n]] == k - 1:
                    is_k -= 1
                left += 1
            cnt[s[j % n]] += 1
            if cnt[s[j % n]] == k:
                is_k += 1
                res = min(res, j - left + 1)
        return res


"""思路

按照题意所述，从最左和最右侧取走后，原字符串还剩下一个连续的区间，
那么可以转化为求一个最长的子区间，使得区间两边的所有字符加起来满足题目要求。
当满足题意要求时，显然区间长度越长，取得的字符就越少。所以当右端点 r 固定时，
最优的情况是找到一个最小的左端点 l 使得取走的字符最少，并且随着左端点 r 右移动，
满足要求的 l 也会往右移动。针对这种情况，可以采用双指针的做法，
先扫一遍使得每个字符都进行计数然后存到 cnt 数组中，如果不满足题意要求直接返回 −1 即可。
左右指针一开始都从 0 开始，优先移动右指针 r，
每移动一次 r 表示把这个字符添加到最后还剩下的集合中，所以应该在计数中减去。
如果此时计数数组 cnt 中每一个元素都大于等于 k，则表示满足题目要求直接更新答案。
如果 cnt 中存在一个元素小于 k，则移动左指针 l，表示要拿掉这个字符。
所以应该计数添加到 cnt 中，持续移动左指针直到满足题目要求。
"""
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        n = len(s)
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        if cnt[0] >= k and cnt[1] >= k and cnt[2] >= k:
            res = n
        else:
            return -1

        j = 0
        for i, c in enumerate(s):
            cnt[ord(c) - ord('a')] -= 1
            while cnt[0] < k or cnt[1] < k or cnt[2] < k:
                cnt[ord(s[j]) - ord('a')] += 1
                j += 1
            if cnt[0] >= k and cnt[1] >= k and cnt[2] >= k:
                res = min(res, n - i - 1 + j)
        return res




s = Solution()
# r = s.takeCharacters(s = "aabaaaacaabc", k = 2)

r = s.takeCharacters(s = "bcbaab", k = 1)
print(r)
