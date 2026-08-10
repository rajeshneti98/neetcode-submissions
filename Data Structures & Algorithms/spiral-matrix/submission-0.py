class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        curr = 0
        res = []
        while left<=right and top<=bottom:
            if curr == 0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            elif curr == 1:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right-=1
            elif curr == 2:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            else:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            curr = (curr+1)%4
        return res