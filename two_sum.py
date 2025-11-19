LeetCode 1 – Two Sum
Brute force approach


##Problem 


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


## My Solution 

class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

## 🔍 Problem Explanation:

Given an array of integers (nums) and a target value,
return the indices of the two numbers that add up to the target.


## Example:
nums = [2, 7, 11, 15], target = 9
output: [0, 1] → because nums[0] + nums[1] = 2 + 7 = 9


##  How This Code Works:

Loop through each pair of elements using two nested loops
For each pair (i, j), check if nums[i] + nums[j] == target
If it matches, return the indices [i, j]


# Learnings:

Practiced using nested loops to compare all combinations of two elements
Understood the brute force approach (try all possibilities)
Gained familiarity with index access and return values in Python



# Time Complexity: O(n^2)

Since we are checking every possible pair, this is not the most efficient method,
but it's a great way to understand the problem before optimizing it.
