class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []

        for op in operations:
            if op == '+':
                x.append(x[-1]+x[-2])
            elif op == 'D':
                x.append(x[-1]*2)
            elif op == 'C':
                x.pop()
            else:
                x.append(int(op))
        
        return sum(x)