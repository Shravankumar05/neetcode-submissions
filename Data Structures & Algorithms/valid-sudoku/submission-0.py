class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]

        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == ".":
                    j += 1
                    continue
                if board[i][j] in cols[i]:
                    return False
                cols[i].add(board[i][j])
                j += 1
            i += 1

        rows = [set() for _ in range(9)]
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == ".":
                    j += 1
                    continue
                if board[i][j] in rows[j]:
                    return False
                rows[j].add(board[i][j])
                j += 1
            i += 1

        row = 0
        while row < 9:
            col = 0
            while col < 9:
                values = set()
                i = row
                while i < row + 3:
                    j = col
                    while j < col + 3:
                        if board[i][j] != ".":
                            if board[i][j] in values:
                                return False
                            values.add(board[i][j])
                        j += 1
                    i += 1
                col += 3
            row += 3

        return True