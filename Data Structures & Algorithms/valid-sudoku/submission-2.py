class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        # if a row has a matching value
        while i < len(board):
            j = 0
            seen = set()
            while j < len(board[i]):
                if board[i][j] == '.':
                    j += 1
                    continue
                else:
                    curr = int(board[i][j])
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)
                j += 1
            i += 1

        # if column has a matching value
        j = 0
        while j < len(board):
            i = 0
            seen = set()
            while i < len(board):
                if board[i][j] == '.':
                    i += 1
                    continue
                else:
                    curr = int(board[i][j])
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)
                i += 1
            j += 1

        i, j = 0, 0
        while i < len(board):
            j = 0
            while j < len(board):
                # check square
                seen = set()
                curr = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                for val in curr:
                    if val == '.':
                        continue
                    else:
                        x = int(val)
                        if x in seen:
                            return False
                        else:
                            seen.add(x)

                j += 3
            i += 3
        
        return True