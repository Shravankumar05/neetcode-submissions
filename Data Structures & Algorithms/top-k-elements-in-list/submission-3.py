class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for _ in range(len(nums)+1)]

        x = Counter(nums)

        for key, count in x.items():
            counts[count].append(key)
        
        res = []
        count = 0
        for i in range(len(nums), -1, -1):
            if counts[i]:
                for num in counts[i]:
                    res.append(num)
                    count += 1
                    if count == k:
                        return res