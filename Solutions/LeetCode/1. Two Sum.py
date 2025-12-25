from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [Problem]: Two Sum
        [Link]: https://leetcode.com/problems/two-sum/

        [Approach]:
        I used a Hash Map to solve this problem in One-pass.
        We iterate through the array and check if the complement exists in the hash map.
        If found, we return the indices immediately.

        [Complexity]:
        - Time Complexity: O(N) because we traverse the list exactly once.
        - Space Complexity: O(N) to store up to N elements in the hash map.
        """

        # {num: index}
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i