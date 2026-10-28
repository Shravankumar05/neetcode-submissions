class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        res = 0

        for customer in customers:
            curr_time = max(curr_time, customer[0]) + customer[1]
            res += (curr_time-customer[0])
        
        return res/len(customers)