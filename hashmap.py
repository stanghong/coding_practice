# 1. Two Sum
dic={}
for i, val in enumerate(nums):
    remain=target-val
    
    if remain in dic:
        return [dic[remain], i]
    else:
        dic[val] = i
#O(n) time

#36 valid suduku: learning defaultdict(set) no raise missing key error, tricks of i//3, i//3 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #data store in array board[i][j]
        #check repetition in row and columns
        # check repetition in 3x3 board[i][j] for _ in range(0, 9): for i etc.
        row= collections.defaultdict(set) #store all elements as collection of sets
        col= collections.defaultdict(set) #store all elements as collection of sets
        matrix= collections.defaultdict(set) #store all elements as collection of sets
        for i in range(0, 9): # check 3x3
            for j in range(0, 9): 
                if board[i][j] != '.':
                    if board[i][j] in matrix[(i//3, j//3)] \
                    or board[i][j] in row[i] \
                    or board[i][j] in col[j]:
                        return False
                    matrix[(i//3, j//3)].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])

        return True
