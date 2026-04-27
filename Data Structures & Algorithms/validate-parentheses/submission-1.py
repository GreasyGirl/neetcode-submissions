class Solution:
    def isValid(self, s: str) -> bool:
        # 
        pairs ={')':'(', '}': '{', ']':'['}
        stack = []
        for c in s: 
            if c in pairs: # closing bracket 
                if stack and stack[-1] == pairs[c]: #closing bracket 
                    stack.pop()
                else: #opening bracket 
                    return False 
            else: # opening bracket 
                stack.append(c)
        return len(stack) == 0

       
                

