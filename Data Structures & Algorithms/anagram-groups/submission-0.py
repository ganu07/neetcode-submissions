class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = dict()
        op = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in dict1:
                dict1[sorted_word].append(word)
            else:
                dict1[sorted_word] = [word]
        
        for key, values in dict1.items():
            op.append(values)
        
        return op
        
        