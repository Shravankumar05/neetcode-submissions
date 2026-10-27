class Solution:
    def isValid(self, s: str) -> bool:
        x = []

        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                x.append(bracket)
            elif bracket == ']':
                if not x:
                    return False
                top = x.pop()
                if top != '[':
                    return False
            elif bracket == '}':
                if not x:
                    return False
                top = x.pop()
                if top != '{':
                    return False
            elif bracket == ')':
                if not x:
                    return False
                top = x.pop()
                if top != '(':
                    return False

        return not x