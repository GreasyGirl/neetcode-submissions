class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
         #[ 6, 1, 2,3, 4, 5,6 ]
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # left ascending or right ascending 
            if nums[m] >= nums[l]: # left ascending 
                if nums[l] <= target<= nums[m]: # go left
                    r = m - 1
                else: #right
                    l = m + 1
            else: #right ascending 
                if nums[m] <= target<= nums[r]: #right
                    l = m + 1
                else: 
                    r = m - 1

        return -1



            
        