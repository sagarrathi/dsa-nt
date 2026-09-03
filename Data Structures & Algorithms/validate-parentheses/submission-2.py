class Solution:
    def isValid(self, s: str) -> bool:
        my_hash={
            ")" : "(",
            "}" : "{",
            "]" : "[",
            }
        
        stack =[]
        for char in s:
            if char in my_hash: 
                if stack and stack[-1] == my_hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not len(stack) else False


        
        