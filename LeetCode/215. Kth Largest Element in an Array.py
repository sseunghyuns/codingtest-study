'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = sorted(nums, reverse=True)
#         return nums[k-1]
    
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)