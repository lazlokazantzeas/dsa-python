"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Hash Map

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Time:
Space:
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

