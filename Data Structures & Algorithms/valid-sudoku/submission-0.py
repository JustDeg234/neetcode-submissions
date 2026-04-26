class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create row, col, and square dictionaries with items as a set of populated numbers
        row = defaultdict(set) #key: index, value: set of elements within the row specified by index
        cols = defaultdict(set)
        square = defaultdict(set) #key: row_index // 3, cols_index //3, value: set of elements

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if (board[i][j] in row[i] or #check value on board with the row element at the specific row
                    board[i][j] in cols[j] or
                    board[i][j] in square[(i//3, j//3)]): return False #duplicate, validation check
                row[i].add(board[i][j]) #update row val
                cols[j].add(board[i][j])
                square[(i // 3, j // 3)].add(board[i][j]) #add due to set nature, append is array without carrying for duplicates
        return True