
"""给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：

2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
0，如果上述条件全部不满足
返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。



示例 1：

输入：nums = [1,2,3]
输出：2
解释：对于每个符合范围 1 <= i <= 1 的下标 i :
- nums[1] 的美丽值等于 2
示例 2：

输入：nums = [2,4,6,4]
输出：1
解释：对于每个符合范围 1 <= i <= 2 的下标 i :
- nums[1] 的美丽值等于 1
- nums[2] 的美丽值等于 0
示例 3：

输入：nums = [3,2,1]
输出：0
解释：对于每个符合范围 1 <= i <= 1 的下标 i :
- nums[1] 的美丽值等于 0


提示：

3 <= nums.length <= 105
1 <= nums[i] <= 105"""
from typing import List

# 前缀最大值+后缀最小值
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        suffix = [nums[-1]] * n
        for i in range(n-2, 0, -1):
            suffix[i] = min(nums[i], suffix[i+1])
        pre = nums[0]
        for i in range(1, n - 1):
            if pre < nums[i] < suffix[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            pre = max(pre, nums[i])
        return res

s = Solution()
r = s.sumOfBeauties([55,36,68,97,1,20,5,50,53,21,15,66,93,12,31,14,13,3,24,97,30,14,28,4,67,86,60,59,40,69,83,49,28,88,98,27,94,56,55,66,3,75,76,7,54,68,75,24,13,85,62,47,3,67,16,79,47,38,89,48,40,3,88,53,13,14,40,26,100,87,3,58,8,53,82,63,60,27,76,79,10,1,37,4,48,40,93,10,29,97])
print(r)