def duplicateExists(values:List[str]) -> bool:
    hashset = set()
    for s in values:
        if s in hashset:
            if s == ".":
                continue
            return True
        hashset.add(s)
    return False 

class Solution:
   

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i=0
        while i<9:
            if(duplicateExists(board[i])):
                return False
            i+=1
        i=0
        while i<9:
            column = []
            j=0
            while j<9:
                column.append(board[j][i])
                j+=1
            if(duplicateExists(column)):
                return False
            i+=1
        BoxesRow=3
        BoxesColumn=3
        
        for c in range(BoxesColumn):
            for g in range(BoxesRow):
                box = []
                for rowElement in range(3):
                    for columnElement in range(3):
                        box.append(board[g*3+rowElement][c*3+columnElement])
                if(duplicateExists(box)):
                    return False
        return True
