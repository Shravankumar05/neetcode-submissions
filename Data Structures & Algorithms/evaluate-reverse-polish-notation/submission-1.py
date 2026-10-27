class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = []

        for t in tokens:
            if t in ('+', '-', '*', '/'):
                b = x.pop()
                a = x.pop()

                if t == '+':
                    x.append(a + b)
                elif t == '-':
                    x.append(a - b)
                elif t == '*':
                    x.append(a * b)
                elif t == '/':
                    result = abs(a) // abs(b)
                    if (a < 0) != (b < 0):
                        result = -result
                    x.append(result)
            else:
                x.append(int(t))

        return x[-1]