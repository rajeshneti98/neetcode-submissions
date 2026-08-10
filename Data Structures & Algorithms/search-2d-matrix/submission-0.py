class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols =  len(matrix), len(matrix[0])
        lr, hr = 0, rows-1
        while lr <=hr:
            mr = lr + (hr-lr)//2
            if matrix[mr][0]<=target and matrix[mr][cols-1] >=target:
                lc, hc = 0, cols-1
                while lc<=hc:
                    mc = lc + (hc-lc) // 2
                    if matrix[mr][mc] == target:
                        return True
                    elif matrix[mr][mc] < target:
                        lc = mc + 1
                    else:
                        hc = mc - 1
                return False
            elif matrix[mr][0] > target:
                hr = mr -1
            else:
                lr = mr +1

        return False
        