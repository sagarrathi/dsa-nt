class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_dict={}

        n= len(s)
        if (n!= len(t)):
            return False

        for i in range(n):
            ch=s[i] 
            if(ch in char_dict):
                char_dict[ch]+=1
            else:
                char_dict[ch]=1
            
            cha=t[i]
            if(cha in char_dict):
                char_dict[cha]-=1
            else:
                char_dict[cha]=-1
        result=list(char_dict.values())

        return not any(result)

