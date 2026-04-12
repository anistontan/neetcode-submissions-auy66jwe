class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        keep 3 "memory sets"
        - rows[r] = digits already seen in row r 
        - cols[c] = digits already seen in col c
        - boxes[b] = digits already seen in box b 
        then scan every cell once : 
        - if the digit is already in row set OR col set OR box set --> invalid 
        - else add it to all 3 sets 
        '''
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue 
                
                b=(r//3) * 3 + (c//3)
                #this tells you which 3x3 box the cell belongs to 
                # r//3 = which "box row"
                # c//3 = which "box column"
                # then (r//3)*3 jumps to the correct box row (0,3 or 6 )
                # + (c//3) shifts within that row (0,1,2)
                '''
                Cell at r=4, c=7:
                r // 3 = 1
                c // 3 = 2
                b = 1*3 + 2 = 5 ✅ (middle-right box)
                '''
                
                if cur in rows[r] or cur in cols[c] or cur in boxes[b]:
                    return False
                
                rows[r].add(cur)
                cols[c].add(cur)
                boxes[b].add(cur) 

        return True


    