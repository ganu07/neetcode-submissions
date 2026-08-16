class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(strs[i])
            else:
                hashmap[sorted_word] = [strs[i]]

        
        for key, value in hashmap.items():
            output.append(value)
        
        return output


        
        