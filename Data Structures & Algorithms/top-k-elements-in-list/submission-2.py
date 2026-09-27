class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)
        res = []
        counter = 0
        
        # number - frequency pairs
        for key, value in counts.items():
            buckets[value].append(key) # buckets now gives values which appeared with idx freq

        for i in range(len(nums), -1, -1):
            if buckets[i]:
                for number in buckets[i]:
                    res.append(number)
                    counter += 1
                    if counter == k:
                        return res
        
        return res