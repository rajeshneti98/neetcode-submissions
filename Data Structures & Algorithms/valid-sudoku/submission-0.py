class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            mp = defaultdict(int)
            for j in range(9):
                num = board[i][j]
                if num!='.' and num in mp:
                    return False
                mp[num] = 1
        for j in range(9):
            mp = defaultdict(int)
            for i in range(9):
                num = board[i][j]
                if num!='.' and num in mp:
                    return False
                mp[num] = 1
        for hgrid in range(0,3):
            for vgrid in range(0,3):
                mp = defaultdict(int)
                for i in range(0,3):
                    for j in range(0,3):
                        num = board[3*hgrid+i][3*vgrid+j]
                        if num!='.' and num in mp:
                            return False
                        mp[num] = 1
        return True

        