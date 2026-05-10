class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range (9):
            for c in range (9):
                val = board[r][c]
                if val == '.':
                    continue
                box_id = (r//3) *3 + (c//3)
                if val in row[r] or val in col[c] or val in box[box_id]:
                    return False
                row[r].add(val)
                col[c].add(val)
                box[box_id].add(val)
        return True
