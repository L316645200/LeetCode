#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：3.4 原地修改.py
# @Author  ：Lin
# @Date    ：2024/11/23 17:12
"""27. 移除元素
26. 删除有序数组中的重复项
80. 删除有序数组中的重复项 II
283. 移动零
905. 按奇偶排序数组
922. 按奇偶排序数组 II
2460. 对数组执行操作
1089. 复写零"""
from typing import List

"""27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
用户评测：
评测机将使用以下代码测试您的解决方案：
int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。
int k = removeElement(nums, val); // 调用你的实现
assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            while left < right and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1

        while left >= 0 and nums[left] == val:
            left -= 1
        return left + 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


# s = Solution()
# r = s.removeElement(nums = [2,3,3], val = 3)
# print(r)

"""26. 删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:
系统会用下面的代码来测试你的题解:
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案
int k = removeDuplicates(nums); // 调用
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。
示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
提示：
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按 非严格递增 排列
"""


# 不改变nums数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        cur = -10 ** 5
        for i in range(len(nums)):
            if nums[i] > cur:
                cur = nums[i]
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k

# 改变nums数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
# s = Solution()
# s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])

"""80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
说明：
为什么返回数值是整数，但输出的答案是数组呢？
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
提示：
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        cur = -10 ** 5
        for i in range(len(nums)):
            if nums[i] >= cur:
                if nums[i] > cur:
                    cur = nums[i]
                elif nums[i] == cur:
                    cur += 0.5
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        return k


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k < 2 or nums[k-2] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

# s = Solution()
# s.removeDuplicates(nums = [1,1,1,2,2,3])

"""283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]
输出: [0]
提示:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
进阶：你能尽量减少完成的操作次数吗？
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1


# s = Solution()
# s.moveZeroes(nums = [0,1,0,3,12])

"""905. 按奇偶排序数组
给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
返回满足此条件的 任一数组 作为答案。
示例 1：
输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
示例 2：
输入：nums = [0]
输出：[0]
提示：
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums
# s = Solution()
# s.sortArrayByParity(nums = [3,1,2,4])

"""922. 按奇偶排序数组 II
给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
你可以返回 任何满足上述条件的数组作为答案 。
示例 1：
输入：nums = [4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
示例 2：
输入：nums = [2,3]
输出：[2,3]
提示：
2 <= nums.length <= 2 * 104
nums.length 是偶数
nums 中一半是偶数
0 <= nums[i] <= 1000
进阶：可以不使用额外空间解决问题吗？
"""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        n = len(nums)
        while left < n and right < n:
            while left < n and nums[left] % 2 == left % 2:
                left += 2
            while right < n and nums[right] % 2 == right % 2:
                right += 2
            if left < n and right < n:
                nums[left], nums[right] = nums[right], nums[left]
        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 1
        for i in range(0, n, 2):
            if nums[i] % 2 == i % 2:
                continue
            while j < n and nums[j] % 2 == j % 2:
                j += 2
            if j < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

# s = Solution()
# s.sortArrayByParityII(nums = [888,505,627,846])

"""2460. 对数组执行操作
给你一个下标从 0 开始的数组 nums ，数组大小为 n ，且由 非负 整数组成。
你需要对数组执行 n - 1 步操作，其中第 i 步操作（从 0 开始计数）要求对 nums 中第 i 个元素执行下述指令：
如果 nums[i] == nums[i + 1] ，则 nums[i] 的值变成原来的 2 倍，nums[i + 1] 的值变成 0 。否则，跳过这步操作。
在执行完 全部 操作后，将所有 0 移动 到数组的 末尾 。
例如，数组 [1,0,2,0,0,1] 将所有 0 移动到末尾后变为 [1,2,1,0,0,0] 。
返回结果数组。
注意 操作应当 依次有序 执行，而不是一次性全部执行。
示例 1：
输入：nums = [1,2,2,1,1,0]
输出：[1,4,2,0,0,0]
解释：执行以下操作：
- i = 0: nums[0] 和 nums[1] 不相等，跳过这步操作。
- i = 1: nums[1] 和 nums[2] 相等，nums[1] 的值变成原来的 2 倍，nums[2] 的值变成 0 。数组变成 [1,4,0,1,1,0] 。
- i = 2: nums[2] 和 nums[3] 不相等，所以跳过这步操作。
- i = 3: nums[3] 和 nums[4] 相等，nums[3] 的值变成原来的 2 倍，nums[4] 的值变成 0 。数组变成 [1,4,0,2,0,0] 。
- i = 4: nums[4] 和 nums[5] 相等，nums[4] 的值变成原来的 2 倍，nums[5] 的值变成 0 。数组变成 [1,4,0,2,0,0] 。
执行完所有操作后，将 0 全部移动到数组末尾，得到结果数组 [1,4,2,0,0,0] 。
示例 2：
输入：nums = [0,1]
输出：[1,0]
解释：无法执行任何操作，只需要将 0 移动到末尾。
提示：
2 <= nums.length <= 2000
0 <= nums[i] <= 1000
"""

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = nums[i] * 2, 0
                i += 1
            i += 1
        left = right = 0
        while left < n and right < n:
            while left < n and nums[left] != 0:
                left += 1
            right = left
            while right < n and nums[right] == 0:
                right += 1
            if left < n and right < n:
                nums[left], nums[right] = nums[right], nums[left]
        return nums

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        for i in range(n-1):
            if nums[i]:
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
                nums[j] = nums[i]
                j += 1

        if nums[-1]:
            nums[j] = nums[-1]
            j += 1
        for i in range(j, n):
            nums[i] = 0
        return nums


# s = Solution()
# s.applyOperations(nums = [1,2,2,1,1,0])
"""1089. 复写零
给你一个长度固定的整数数组 arr ，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：请不要在超过该数组长度的位置写入元素。请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
示例 1：
输入：arr = [1,0,2,3,0,4,5,0]
输出：[1,0,0,2,3,0,0,4]
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：
输入：arr = [1,2,3]
输出：[1,2,3]
解释：调用函数后，输入的数组将被修改为：[1,2,3]
提示：
1 <= arr.length <= 104
0 <= arr[i] <= 9
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        nums = [0] * n
        left, right = 0, 0
        while right < n:
            if arr[left] == 0:
                if right < n - 1:
                    nums[right + 1] = 0
                nums[right] = 0
                right += 1
            else:
                nums[right] = arr[left]
            left += 1
            right += 1
        arr[:] = nums

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = top = 0
        n = len(arr)
        while top < n:
            top += 1 if arr[i] else 2
            i += 1
        if top == n + 1:
            arr[n-1] = 0
            top -= 2
            i -= 1
        while i > 0:
            i -= 1
            top -= 1
            if arr[i] == 0:
                arr[top] = arr[top-1] = 0
                top -= 1
            else:
                arr[top] = arr[i]


s = Solution()
s.duplicateZeros(arr = [1,0,2,3,0,4,5,0])





































