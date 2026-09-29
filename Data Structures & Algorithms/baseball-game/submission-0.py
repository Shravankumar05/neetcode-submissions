class Solution:
    def calPoints(self, operations: List[str]) -> int:
        curr_stack = []
        
        for i in range(len(operations)):
            if operations[i] == '+':
                curr_stack.append(curr_stack[-1] + curr_stack[-2])
            elif operations[i] == 'D':
                curr_stack.append(2*curr_stack[-1])
            elif operations[i] == 'C':
                curr_stack.pop()
            else:
                curr_stack.append(int(operations[i]))
        
        return sum(curr_stack)