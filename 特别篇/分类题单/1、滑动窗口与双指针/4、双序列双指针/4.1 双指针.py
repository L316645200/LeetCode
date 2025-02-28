#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：4.1 双指针.py
# @Author  ：Lin
# @Date    ：2024/11/29 11:39
"""2540. 最小公共值 做到 O(n+m)
88. 合并两个有序数组 做到 O(n+m)
2570. 合并两个二维数组 - 求和法 做到 O(n+m)
LCP 18. 早餐组合
1855. 下标对中的最大距离 1515
1385. 两个数组间的距离值
925. 长按键入 做到 O(n+m)
809. 情感丰富的文字 1605
2337. 移动片段得到字符串 1693
777. 在 LR 字符串中交换相邻字符 同 2337 题
844. 比较含退格的字符串 做到 O(1) 额外空间
986. 区间列表的交集 做到 O(n+m)
面试题 16.06. 最小差
1537. 最大得分 1961
244. 最短单词距离 II（会员题）
2838. 英雄可以获得的最大金币数（会员题）
1229. 安排会议日程（会员题）
1570. 两个稀疏向量的点积（会员题）
1868. 两个行程编码数组的积（会员题）
"""

"""2540. 最小公共值 做到 O(n+m)
给你两个整数数组 nums1 和 nums2 ，它们已经按非降序排序，请你返回两个数组的 最小公共整数 。如果两个数组 nums1 和 nums2 没有公共整数，请你返回 -1 。

如果一个整数在两个数组中都 至少出现一次 ，那么这个整数是数组 nums1 和 nums2 公共 的。



示例 1：

输入：nums1 = [1,2,3], nums2 = [2,4]
输出：2
解释：两个数组的最小公共元素是 2 ，所以我们返回 2 。
示例 2：

输入：nums1 = [1,2,3,6], nums2 = [2,3,4,5]
输出：2
解释：两个数组中的公共元素是 2 和 3 ，2 是较小值，所以返回 2 。


提示：

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
nums1 和 nums2 都是 非降序 的。
"""
import bisect
from collections import Counter
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while left < n1 and right < n2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1
        return -1

# s = Solution()
# s.getCommon(nums1 = [1,2,3], nums2 = [2,4])

"""88. 合并两个有序数组 做到 O(n+m)
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = m - 1, n - 1
        while left + right + 1 >= 0:
            if left >= 0 and right >= 0:
                if nums1[left] >= nums2[right]:
                    nums1[left + right + 1] = nums1[left]
                    left -= 1
                else:
                    nums1[left + right + 1] = nums2[right]
                    right -= 1
            elif left >= 0:
                nums1[left + right + 1] = nums1[left]
                left -= 1
            else:
                nums1[left + right + 1] = nums2[right]
                right -= 1


# s = Solution()
# s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)


"""2570. 合并两个二维数组 - 求和法 做到 O(n+m)
给你两个 二维 整数数组 nums1 和 nums2.
nums1[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
nums2[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
每个数组都包含 互不相同 的 id ，并按 id 以 递增 顺序排列。
请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：
只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。
每个 id 在结果数组中 只能出现一次 ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 0 。
返回结果数组。返回的数组需要按 id 以递增顺序排列。
示例 1：
输入：nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
输出：[[1,6],[2,3],[3,2],[4,6]]
解释：结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于5 + 1 = 6 。
示例 2：
输入：nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
输出：[[1,3],[2,4],[3,6],[4,3],[5,5]]
解释：不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
提示：
1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
数组中的 id 互不相同
数据均按 id 以严格递增顺序排列
"""


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        i = j = 0
        res = []
        while i < n or j < m:
            if i < n and j < m:
                if nums1[i][0] == nums2[j][0]:
                    res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    j += 1
                    i += 1
                elif nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            elif i < n:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        return res


# s = Solution()
# s.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])

"""LCP 18. 早餐组合
小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
示例 1：
输入：staple = [10,20,5], drinks = [5,5,2], x = 15
输出：6
解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是： 第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15； 第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15； 第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12； 第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10； 第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10； 第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。
示例 2：
输入：staple = [2,1,1], drinks = [8,9,5,1], x = 9
输出：8
解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是： 第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7； 第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3； 第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9； 第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6； 第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2； 第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9； 第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6； 第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；
提示：
1 <= staple.length <= 10^5
1 <= drinks.length <= 10^5
1 <= staple[i],drinks[i] <= 10^5
1 <= x <= 2*10^5
"""

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        m, n = len(staple), len(drinks)
        j = n - 1
        res = 0
        for i in range(m):
            while j >= 0 and staple[i] + drinks[j] > x:
                j -= 1
            if j < 0:
                break
            res += j + 1
        return res % (10 ** 9 + 7)

# s = Solution()
# s.breakfastNumber(staple = [10,20,5], drinks = [5,5,2], x = 15)
"""1385. 两个数组间的距离值
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
示例 1：
输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
输出：2
解释：
对于 arr1[0]=4 我们有：
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
所以 arr1[0]=4 符合距离要求
对于 arr1[1]=5 我们有：
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
所以 arr1[1]=5 也符合距离要求
对于 arr1[2]=8 我们有：
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
存在距离小于等于 2 的情况，不符合距离要求 
故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
示例 2：
输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
输出：2
示例 3：
输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
输出：1
提示：
1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = Counter(arr1)
        arr1 = sorted(set(arr1))
        arr2 = sorted(set(arr2))
        res = j = 0
        m, n = len(arr1), len(arr2)
        for i in range(m):
            while j < n - 1 and abs(arr1[i] - arr2[j+1]) < abs(arr1[i] - arr2[j]):
                j += 1
            res += cnt[arr1[i]] if abs(arr1[i] - arr2[j]) > d else 0
        return res


# s = Solution()
# s.findTheDistanceValue(arr1 =[-3,10,2,8,0,10], arr2 = [-9,-1,-4,-9,-8], d = 9)

"""1855. 下标对中的最大距离 1515
给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。
下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​
返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。
一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。
示例 1：
输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
输出：2
解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
最大距离是 2 ，对应下标对 (2,4) 。
示例 2：
输入：nums1 = [2,2,2], nums2 = [10,10,1]
输出：1
解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
最大距离是 1 ，对应下标对 (0,1) 。
示例 3：
输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
输出：2
解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
最大距离是 2 ，对应下标对 (2,4) 。
提示：
1 <= nums1.length <= 105
1 <= nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
nums1 和 nums2 都是 非递增 数组
"""

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        k = 1
        n = len(nums2)
        for i in range(len(nums1)):
            while i + k < n and nums1[i] <= nums2[i+k]:
                k += 1
        return k - 1

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        j = 0
        res = 0
        for i in range(len(nums1)):
            while j < n and nums1[i] <= nums2[j]:
                j += 1
            res = max(res, j - i - 1)
        return res

# s = Solution()
# s.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5])
"""925. 长按键入 做到 O(n+m)
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
提示：
1 <= name.length, typed.length <= 1000
name 和 typed 的字符都是小写字母
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        j = 0
        for i in range(n):
            print(i,j)
            if j == m or name[j] != typed[i]:
                if i == 0 or typed[i] != typed[i-1]:
                    return False
                continue
            if j < m and typed[i] == name[j]:
                j += 1
        return j == m

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        j = 0
        for i in range(n):
            print(i,j)
            if j < m and typed[i] == name[j]:
                j += 1
            elif j == m or name[j] != typed[i] and (i == 0 or typed[i] != typed[i-1]):
                return False

        return j == m
# s = Solution()
# s.isLongPressedName(name = "zlexya", typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya")

"""809. 情感丰富的文字 1605
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。
对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。
例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 s = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = s。
输入一组查询单词，输出其中可扩张的单词数量。
示例：
输入： 
s = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。
提示：
1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s 和所有在 words 中的单词都只由小写字母组成。
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        n = len(s)
        res = 0
        for i, word in enumerate(words):  # 遍历数组
            l1 = l2 = r1 = r2 = 0  # 初始化双指针，两个字符串各维护一组双指针
            m = len(word)
            while l1 < n and l2 < m and s[l1] == word[l2]:
                # 当是连续相同字符时
                while r1 < n and s[l1] == s[r1]:
                    r1 += 1
                while r2 < m and word[l2] == word[r2]:
                    r2 += 1
                # print(i, l1,r1,l2,r2)
                # 扩张字母相同数不能大于原字符相同字母数，(r1 - l1) + (r2 - l2) == 3 是排除字母组长度小于3的情况(2和1)
                if (r1 - l1) + (r2 - l2) == 3 or r1 - l1 < r2 - l2:
                    break
                l1, l2 = r1, r2
            # print(l1, l2)
            if l1 == n and l2 == m:
                res += 1
        return res

# s = Solution()
# s.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"])
"""2337. 移动片段得到字符串 1693
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。
示例 1：
输入：start = "_L__R__R_", target = "L______RR"
输出：true
解释：可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
- 将第二个片段向右移动三步，字符串现在变为 "L______RR" 。
可以从字符串 start 得到 target ，所以返回 true 。
示例 2：
输入：start = "R_L_", target = "__LR"
输出：false
解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。
但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。
示例 3：
输入：start = "_R", target = "R_"
输出：false
解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。
提示：
n == start.length == target.length
1 <= n <= 105
start 和 target 由字符 'L'、'R' 和 '_' 组成
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        left, right = 0, 0
        while left < n and right < n:
            while left < n and start[left] == '_':
                left += 1
            while right < n and target[right] == '_':
                right += 1

            if left < n and right < n:
                if start[left] != target[right]:
                    return False
                elif start[left] == 'L' and left < right:
                    return False
                elif start[left] == 'R' and left > right:
                    return False
                left += 1
                right += 1
        while left < n and start[left] == '_':
            left += 1
        while right < n and target[right] == '_':
            right += 1
        return left == right == n

# s = Solution()
# s.canChange(start = "_L__R__R_", target = "L______RR")

"""777. 在 LR 字符串中交换相邻字符 同 2337 题
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个 "LX" 替换一个 "XL"，或者用一个 "XR" 替换一个 "RX"。现给定起始字符串 start 和结束字符串 result，请编写代码，当且仅当存在一系列移动操作使得 start 可以转换成 result 时， 返回 True。
示例 1：
输入：start = "RXXLRXRXL", result = "XRLXXRRLX"
输出：true
解释：通过以下步骤我们可以将 start 转化为 result：
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
示例 2：
输入：start = "X", result = "L"
输出：false
提示：
1 <= start.length <= 104
start.length == result.length
start 和 result 都只包含 'L', 'R' 或 'X'。
"""

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        left, right = 0, 0
        while left < n and right < n:
            while left < n and start[left] == 'X':
                left += 1
            while right < n and result[right] == 'X':
                right += 1

            if left < n and right < n:
                if start[left] != result[right]:
                    return False
                elif start[left] == 'L' and left < right:
                    return False
                elif start[left] == 'R' and left > right:
                    return False
                left += 1
                right += 1
        while left < n and start[left] == 'X':
            left += 1
        while right < n and result[right] == 'X':
            right += 1
        return left == right == n

"""844. 比较含退格的字符串 做到 O(1) 额外空间
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
示例 1：
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：
输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
提示：
1 <= s.length, t.length <= 200
s 和 t 只含有小写字母以及字符 '#'
进阶：
你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left, right = len(s) - 1, len(t) - 1
        k1 = k2 = 0
        while left >= 0 or right >= 0:

            while left >= 0 and (k1 > 0 or s[left] == '#'):
                if s[left] == '#':
                    k1 += 1
                elif k1 > 0:
                    k1 -= 1
                left -= 1
            while right >= 0 and (k2 > 0 or t[right] == '#'):
                if t[right] == '#':
                    k2 += 1
                elif k2 > 0:
                    k2 -= 1
                right -= 1

            if left >= 0 and right >= 0:
                if s[left] != t[right]:
                    return False
                left -= 1
                right -= 1

        while left >= 0 and (k1 > 0 or s[left] == '#'):
            if s[left] == '#':
                k1 += 1
            elif k1 > 0:
                k1 -= 1
            left -= 1
        while right >= 0 and (k2 > 0 or t[right] == '#'):
            if t[right] == '#':
                k2 += 1
            elif k2 > 0:
                k2 -= 1
            right -= 1

        return left == right == -1


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left, right = len(s) - 1, len(t) - 1
        k1 = k2 = 0
        while left >= 0 or right >= 0:

            while left >= 0:
                if s[left] == '#':
                    k1 += 1
                    left -= 1
                elif k1 > 0:
                    k1 -= 1
                    left -= 1
                else:
                    break

            while right >= 0 and (k2 > 0 or t[right] == '#'):
                if t[right] == '#':
                    k2 += 1
                    right -= 1
                elif k2 > 0:
                    k2 -= 1
                    right -= 1
                else:
                    break
            if left >= 0 and right >= 0:
                if s[left] != t[right]:
                    return False
                left -= 1
                right -= 1
            elif left >= 0 or right >= 0:
                return False
        return True

# s = Solution()
# r = s.backspaceCompare(s = "nzp#o#g", t = "b#nzp#o#g")
# print(r)

"""986. 区间列表的交集 做到 O(n+m)
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
返回这 两个区间列表的交集 。
形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
示例 1：
输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
示例 2：
输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
示例 3：
输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]
示例 4：
输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]
提示：
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        res = []
        if m == 0 or n == 0:
            return res

        l = r = 0
        while l < m and r < n:
            lo, hi = max(firstList[l][0], secondList[r][0]), min(firstList[l][1], secondList[r][1])
            if hi >= lo:
                res.append([lo, hi])
            if firstList[l][1] <= secondList[r][1]:
                l += 1
            else:
                r += 1
        return res

# s = Solution()
# s.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])

"""面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
示例：
输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)
提示：
1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间 [0, 2147483647] 内
"""

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        m, n = len(a), len(b)
        l = r = 0
        res = 2147483647
        while l < m and r < n:
            res = min(res, abs(a[l] - b[r]))
            if a[l] <= b[r]:
                l += 1
            else:
                r += 1
        return res

# s = Solution()
# s.smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])

"""1537. 最大得分 1961
你有两个 有序 且数组内元素互不相同的数组 nums1 和 nums2 。
一条 合法路径 定义如下：
选择数组 nums1 或者 nums2 开始遍历（从下标 0 处开始）。
从左到右遍历当前数组。
如果你遇到了 nums1 和 nums2 中都存在的值，那么你可以切换路径到另一个数组对应数字处继续遍历（但在合法路径中重复数字只会被统计一次）。
得分 定义为合法路径中不同数字的和。
请你返回 所有可能 合法路径 中的最大得分。由于答案可能很大，请你将它对 10^9 + 7 取余后返回。
示例 1：
输入：nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
输出：30
解释：合法路径包括：
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],（从 nums1 开始遍历）
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]  （从 nums2 开始遍历）
最大得分为上图中的绿色路径 [2,4,6,8,10] 。
示例 2：
输入：nums1 = [1,3,5,7,9], nums2 = [3,5,100]
输出：109
解释：最大得分由路径 [1,3,5,100] 得到。
示例 3：
输入：nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
输出：40
解释：nums1 和 nums2 之间无相同数字。
最大得分由路径[6,7,8,9,10]得到。
提示：
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 107
nums1 和 nums2 都是严格递增的数组。
"""

"""
思路：先取出所有相同的值，设相同的值数目为k,
通过这些值将两个数组各分为k+1段数组，
比较两个数组每段数组和的大小，选择较大的那段数组和加入结果，
所有k段数组和相加取余后即为答案
"""


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        l = r = 0
        same = []  # 相同值数组

        while l < m and r < n:  # 双指针得到相同值数组
            if nums1[l] == nums2[r]:
                same.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        if not same:  # 如果没有相同值，那么就不能切换数组，则返回两个数组和较大的那个
            return max(sum(nums1), sum(nums2))

        l = r = 0
        res = 0  # 答案
        for v in same:
            s1 = s2 = 0  # 每段数组和
            while l < m and nums1[l] <= v:
                s1 += nums1[l]
                l += 1
            while r < n and nums2[r] <= v:
                s2 += nums2[r]
                r += 1
            res += max(s1, s2)
        res += max(sum(nums1[l: m]), sum(nums2[r: n]))  # 最后一段数组和
        return res % (10 ** 9 + 7)


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        l = r = 0
        best1 = best2 = 0
        while l < m or r < n:
            if l < m and r < n:
                if nums1[l] < nums2[r]:
                    best1 += nums1[l]
                    l += 1
                elif nums1[l] > nums2[r]:
                    best2 += nums2[r]
                    r += 1
                else:
                    best1 += nums1[l]
                    best2 += nums2[r]
                    best1 = best2 = max(best1, best2)
                    l += 1
                    r += 1
            elif l < m:
                best1 += nums1[l]
                l += 1
            elif r < n:
                best2 += nums2[r]
                r += 1
        return max(best1, best2) % (10 ** 9 + 7)

s = Solution()
s.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])


































































