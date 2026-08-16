class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        op = []

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        # {1:1, 2:2, 3:3}
        sorted_value = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        for key, value in sorted_value[:k]:
            op.append(key)
        
        return op


        