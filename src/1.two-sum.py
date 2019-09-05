#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/

# algorithms
# Easy (44.49%)
# Likes:    11735
# Dislikes: 406
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#

from typing import List, Optional, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        nums_index: List[Tuple[int, int]] = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin: int = 0
        end: int = len(nums) - 1
        while begin < end:
            current = nums_index[begin][0] + nums_index[end][0]
            if current == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif current < target:
                begin += 1
            else:
                end -= 1
        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
