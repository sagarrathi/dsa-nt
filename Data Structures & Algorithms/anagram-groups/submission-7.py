class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        score_table={}

        # def scorer(val: str) -> int:
        #     score = 0
        #     for c in val:
        #         score+=ord(c)
        #     return score


        for val in strs:
            score = "".join(sorted((val)))

            if score not in score_table:
                score_table[score] = [val]
            else: 
                score_table[score].append(val)

        return list(score_table.values())