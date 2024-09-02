import collections
from typing import List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107"""


# Way harder than initially thought

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        sub_sum_dict = {0: 1}
        count = 0
        cont_sum = 0

        for num in nums:
            cont_sum += num
            if cont_sum - k in sub_sum_dict:
                count += sub_sum_dict[cont_sum - k]
            if cont_sum not in sub_sum_dict:
                sub_sum_dict[cont_sum] = 1
            else:
                sub_sum_dict[cont_sum] += 1

        return count


if __name__ == '__main__':
    sol = Solution()

    print(sol.subarraySum([1,1,1,1,1,1,1], 2))
    print(sol.subarraySum([1], 1))
