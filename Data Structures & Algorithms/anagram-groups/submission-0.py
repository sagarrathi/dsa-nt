def createHash2(s):
    ar=[0]*26
    for char in s:
        ar[ord(char) - ord('a')]+=1
        
    return str(ar)    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_dict={}
    
        for s in strs:
            s_hash=createHash2(s)
            if(s_hash) not in hash_dict:
                hash_dict[s_hash] = [s]
            else:
                hash_dict[s_hash].append(s)
        
        ans=list(hash_dict.values())

        return ans
        