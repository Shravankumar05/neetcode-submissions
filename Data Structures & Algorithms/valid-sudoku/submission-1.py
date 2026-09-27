class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(len(board)):
            seen = set()
            for digit in board[i]:
                if digit == ".":
                    continue
                else:
                    curr = int(digit)
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)

        # columns
        for i in range(len(board)): # boards are square so its fine
            seen = set()
            # we need to iterate through the board[0...9][i]
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    curr = int(board[j][i])
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)

        # 3x3 boxes
        i = 0
        while i < 9: # vertical iteration
            j = 0
            while j < 9:
                # work
                seen = set()
                for y in range(3):
                    for x in range(3):
                        curr = board[i+y][j+x]
                        if curr == ".":
                            continue
                        else:
                            if curr in seen:
                                return False
                            else:
                                seen.add(curr)
                j += 3
            i += 3
        
        return True