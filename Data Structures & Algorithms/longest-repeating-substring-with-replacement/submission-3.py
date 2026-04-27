from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxCount = 0
        count = defaultdict(int)
        for r in range(len(s)):
            
            count[s[r]] += 1 # hashmap
            windowSize = r - l + 1#w size
            maxCount = max(maxCount, count[s[r]])

            if windowSize - maxCount <= k: #valid w
                res = max(res, windowSize)
            else: #invalid 
                count[s[l]] -= 1 
                l += 1
                
        return res
            




                

        