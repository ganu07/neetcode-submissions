class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        op = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap.get(sorted_word, []).append(word)
            else:
                hashmap[sorted_word] = [word]
        

        for key, value in hashmap.items():
            op.append(value)
        
        return op
        
        