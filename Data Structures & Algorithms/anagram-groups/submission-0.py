from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # mapping charcount to list of anagram, key: count; values: list of anagram
        for s in strs:
            count_list = [0] * 26
            for c in s: 
                count_list[ord(c) - ord("a")] += 1 # index of a = 0,b =1...
            res[tuple(count_list)].append(s)
        return list(res.values())
            
# m is the number of string, n is the avg of length for each string 
# 0 (m * n)
# O (m)