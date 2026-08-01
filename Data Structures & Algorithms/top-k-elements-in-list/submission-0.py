class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(10001)]
        counter = {}
        
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for key, values in counter.items():
            frequencies[values].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            j = 0
            while j < len(frequencies[i]):
                if len(res) == k:
                    return res
                res.append(frequencies[i][j])
                j += 1
        
        return res