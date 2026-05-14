class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        op = []

        for n in nums:
            dict1[n] = dict1.get(n, 0) + 1
        
        # {key, count}

        sorted_value = sorted(dict1.items(), key =lambda x: x[1], reverse=True)
        for key, value in sorted_value[:k]:
            op.append(key)

        return op
        