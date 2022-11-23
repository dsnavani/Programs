import os
from termcolor import colored
os.system("color")
os.system("color 0")

#FUNCTIONS

#FUNCTIONS TO PRINT THE CHESS BOARD WITH PIECES
def printboard():  
    os.system("cls")
    top = '\t\t\t\t\t\t\t==========================================================================='
    bet1 = '\t\t\t\t\t\t\t|__|____|_______|_______|_______|_______|_______|_______|_______|_______|__|'
    bet2 = '\t\t\t\t\t\t\t|  |\t|\t|\t|\t|\t|\t|\t|\t|\t|  |'
    print(top)
    for i in range(10):
        print('\t\t\t\t\t\t\t', end='')
        for j in range(10):
            while(board[i][j] not in range(9)):
                #print(board[i][j])
                if(len(board[i][j]) > 1 and board[i][j][0] == 'B'):
                    board[i][j] = colored(board[i][j], 'green')
                    break
                elif(len(board[i][j]) > 1 and board[i][j][0] == 'W'):
                    board[i][j] = colored(board[i][j], 'yellow')
                    break
                else:
                    break
                
            print('/',board[i][j],end="")
            if(j==0):
                print(end='|\t')
            elif(j==9):
                print(end='|\t')
            else:
                print(end='\t')
                
        if(i!=9):
            print("\n"+bet1+"\n"+bet2)
    print('\n'+top)

#FINDING THE VALID MOVE
def valid(move):
    while(len(move) != 4):
        print("invalid move")
        move = input()
    while(move[0] not in ['a','b','c','d','e','f','g','h']):
        print('first alphabet not valid')
        move = input()
    while(move[1] not in ['1','2','3','4','5','6','7','8']):
        print('first numeral not valid')
        move = input()
    while(move[2] not in ['a','b','c','d','e','f','g','h']):
        print('second alphabet not valid')
        move = input()
    while(move[3] not in ['1','2','3','4','5','6','7','8']):
        print('second numeral not valid')
        move = input()
    return move

#GETTING INPUT FROM THE USER
def getinput():
    move = input()
    move = valid(move)
    findex = [9-int(move[1]) , abs(ord(move[0])-96)]
    tindex = [9-int(move[3]) , abs(ord(move[2])-96)]
    print(findex,tindex)
    return findex,tindex
    
#CHECKING WHETHER THE SELECTED PIECE IS WHITE
def checkwhitepiece(findex, tindex):
    while(board[findex[0]][findex[1]] == 0):
        print('not a piece')
        findex, tindex = getinput()
    while(board[findex[0]][findex[1]][5+0] != 'W'):
        print('select white piece')
        findex, tindex = getinput()
    return findex, tindex
    
    
#CHECKING WHETHER THE SELECTED PIECE IS WHITE
def checkblackpiece(findex, tindex):
    while(board[findex[0]][findex[1]] == 0):
        print('not a piece')
        findex, tindex = getinput()
    while(board[findex[0]][findex[1]][5+0] != 'B'):
        print('select black piece')
        findex, tindex = getinput()
    return findex, tindex
    
    

#FUNCTION FOR PAWN MOVEMENT
def movepawn():
    while(True):
        if(board[findex[0]][findex[1]][5+0] == 'W'):
            if(tindex[0] >= 7 or findex[0] < tindex[0]):
                print("Pawn is not moved ahead")
                return 1
                break
            if(findex[0] == 7):
                if(findex[0] - tindex[0] > 2):
                    print("provide a valid move")
                    return 1
                    break
            else:   
                if(findex[0] - tindex[0] > 1):
                    print("provide a valid move")
                    return 1
                    break
            if(abs(findex[1] - tindex[1]) > 1):
                print("Not a valid move")
                return 1
                break
            if(abs(findex[1] - tindex[1]) == 1):
                if(findex[0] - tindex[0] != 1):
                    print('not a valid move')
                    return 1
                    break
                if(board[tindex[0]][tindex[1]][5+0] == 'W' or board[tindex[0]][tindex[1]] == 0):
                    print('not a valid move')
                    return 1
                    break
                if(board[tindex[0]][tindex[1]][5+0] == 'W'):
                    print('not a valid move')
                    return 1
                    break
            if(abs(findex[1] - tindex[1]) == 0):
                if(board[tindex[0]][tindex[1]] != 0):
                    print('not a valid move')
                    return 1
                    break
            if(tindex[0] == 1):
                print('select 1 for Rook')
                print('select 2 for Knight')
                print('select 3 for Bishop')
                print('select 4 for Queen')
                pp = input()
                if(len(pp) != 1):
                    print('not valid')
                    return 1
                if( pp not in ['1', '2', '3', '4']):
                    print('not valid')
                    return 1
                promote = int(pp)
                if(promote == 1):
                    board[findex[0]][findex[1]] = 'WR'
                if(promote == 2):
                    board[findex[0]][findex[1]] = 'WK'
                if(promote == 3):
                    board[findex[0]][findex[1]] = 'WB'
                if(promote == 4):
                    board[findex[0]][findex[1]] = 'WQ'
                
            return 0
            break
            
            
        if(board[findex[0]][findex[1]][5+0] == 'B'):
            if(tindex[0] <= 2 or findex[0] > tindex[0]):
                print("Pawn is not moved ahead")
                return 1
                break
            if(findex[0] == 2):
                if(tindex[0] - findex[0] > 2):
                    print("provide a valid move")
                    return 1
                    break
            else:   
                if(tindex[0] - findex[0] > 1):
                    print("provide a valid move")
                    return 1
                    break
            if(abs(findex[1] - tindex[1]) > 1):
                print("Not a valid move")
                return 1
                break
            if(abs(findex[1] - tindex[1]) == 1):
                if(tindex[0] - findex[0] != 1):
                    print('not a valid move')
                    return 1
                    break
                if( board[tindex[0]][tindex[1]] == 0):
                    print('not a valid move')
                    return 1
                    break
                if(board[tindex[0]][tindex[1]][5+0] == 'B'):
                    print('not a valid move')
                    return 1
                    break
            if(abs(findex[1] - tindex[1]) == 0):
                if(board[tindex[0]][tindex[1]] != 0):
                    print('not a valid move')
                    return 1
                    break
                    
            if(tindex[0] == 8):
                print('select 1 for Rook')
                print('select 2 for Knight')
                print('select 3 for Bishop')
                print('select 4 for Queen')
                pp = input()
                if(len(pp) != 1):
                    print('not valid')
                    return 1
                if( pp not in ['1', '2', '3', '4']):
                    print('not valid')
                    return 1
                promote = int(pp)
                if(promote == 1):
                   board[findex[0]][findex[1]] = 'WR'
                if(promote == 2):
                    board[findex[0]][findex[1]] = 'WK'
                if(promote == 3):
                    board[findex[0]][findex[1]] = 'WB'
                if(promote == 4):
                    board[findex[0]][findex[1]] = 'WQ'
            return 0
            break
        
        
#FUNCTION FOR ROOK MOVEMENT
def moverook():
    while(True):
        key = 0
        if(tindex == findex):
            print('Piece not moved')
            return 1
            break
        if(tindex[0] == findex[0]):
            if(tindex[1] > findex[1]):
                for i in range(findex[1]+1, tindex[1]):
                    if(board[tindex[0]][i] != 0):
                        key =1
                        break
            elif(tindex[1] < findex[1]):
                for i in range(tindex[1]+1, findex[1]):
                    if(board[tindex[0]][i] != 0):
                        key = 1
                        break
                        
        elif(tindex[1] == findex[1]):
            if(tindex[0] > findex[0]):
                for i in range(findex[0]+1, tindex[0]):
                    if(board[i][tindex[1]] != 0):
                        key =1
                        break
            elif(tindex[0] < findex[0]):
                for i in range(tindex[0]+1, findex[0]):
                    if(board[i][tindex[1]] != 0):
                        key =1
                        break
        else:
            print("Not valid")
            return 1
            break
        if(key):
            print("not valid")
            return 1
            break
        if(board[tindex[0]][tindex[1]] !=0):
            if(board[tindex[0]][tindex[1]][5+0] == board[findex[0]][findex[1]][5+0]):
                print("It's your comrade")
                return 1 
                break
                
        return 0
        break


#FUNCTION FOR KNIGHT MOVEMENT
def moveknight():
    while(True):
        if(tindex == findex):
            print('knight not moved')
            return 1
            break
        if(abs(findex[0] - tindex[0]) == 2):
            if(abs(findex[1] - tindex[1]) != 1):
                print("Invalid move")
                return 1
                break
        if(abs(findex[1] - tindex[1]) == 2):
            if(abs(findex[0] - tindex[0]) != 1):
                print("Invalid move")
                return 1
                break
        if(abs(findex[0] - tindex[0]) == 1):
            if(abs(findex[1] - tindex[1]) != 2):
                print("Invalid move")
                return 1
                break
        if(abs(findex[1] - tindex[1]) == 1):
            if(abs(findex[0] - tindex[0]) != 2):
                print("Invalid move")
                return 1
                break
                
        
        if(board[tindex[0]][tindex[1]] !=0):
            if(board[tindex[0]][tindex[1]][5+0] == board[findex[0]][findex[1]][5+0]):
                print("It's your comrade")
                return 1 
                break
        return 0
        break


#FUNCTION FOR BISHOP MOVEMENT
def movebishop():
    while(True):
        key = 0
        if(tindex == findex):
            print('Piece not moved')
            return 1
            break
        if(abs(findex[0] - tindex[0]) != abs(findex[1] - tindex[1])):
            print('invalid move')
            return 1
            break
        else:
            temp = abs(findex[0] - tindex[0])
            if(tindex[0] > findex[0]):
                if(tindex[1] > findex[1]):
                    for i in range(1,temp):
                        if(board[findex[0]+i][findex[1]+i] != 0):
                            key = 1
                if(tindex[1] < findex[1]):
                    for i in range(1,temp):
                        if(board[findex[0]+i][findex[1]-i] != 0):
                            key = 1
            elif(tindex[0] < findex[0]):
                if(tindex[1] > findex[1]):
                    for i in range(1,temp):
                        if(board[findex[0]-i][findex[1]+i] != 0):
                            key = 1
                if(tindex[1] < findex[1]):
                    for i in range(1,temp):
                        if(board[findex[0]-i][findex[1]-i] != 0):
                            key = 1
        if(key):
            print("Invalid move")
            return 1
            break
        if(board[tindex[0]][tindex[1]] !=0):
            if(board[tindex[0]][tindex[1]][5+0] == board[findex[0]][findex[1]][5+0]):
                print("It's your comrade")
                return 1 
                break
                
        return 0
        break
    

#FUNCTION FOR BISHOP MOVEMENT
def moveking():
    while(True):
        if(tindex == findex):
            print('King not moved')
            return 1
            break
        if(abs(findex[0] - tindex[0]) > 1):
            print('Invalid move')
            return 1
            break
        if(abs(findex[1] - tindex[1]) > 1):
            print('Invalid move')
            return 1
            break
            
        if(board[tindex[0]][tindex[1]] !=0):
            if(board[tindex[0]][tindex[1]][5+0] == board[findex[0]][findex[1]][5+0]):
                print("It's your man")
                return 1 
                break
    
        return 0
        break

#FUNCTION FOR CHECK
def check():
    for i in range(10):
        for j in range(10):
            if(board[i][j][5] == 'B'):
                if(board[i][j][6] == 'P'):
                    if(board[i+1][j+1]):
                        pass
                        

            
#MAIN PROGRAM STARTS HERE

#DEFINING THE BOARD WITH PIECES
board = [[],[],[],[],[],[],[],[],[],[]]          #LIST FOR BOARD
index = [0,0]       #LIST FOR THE POSITION OF PIECE
takenpieces = set()    #LIST TO COLLECT TAKEN PIECES

board[0] = [0,'a','b','c','d','e','f','g','h',0]
board[1] = [8,'BR1','BN1','BB1','BK','BQ','BB2','BN2','BR2',8]
board[2] = [7,'BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8',7]
for i in range(3,7):
    board[i] = [9-i,0,0,0,0,0,0,0,0,9-i]
board[7] = [2,'WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8',2]
board[8] = [1,'WR1','WN1','WB1','WQ','WK','WB2','WN2','WR2',1]
board[9] = [0,'a','b','c','d','e','f','g','h',0]

printboard()
p1print1 = colored("PLAYER 1 -- Enter White King's Name : ",'yellow')
p2print1 = colored("PLAYER 2 -- Enter Black King's Name : ",'green')
print(p1print1,end='')
player1 = input()
player1 = colored(player1,'yellow')
print(p2print1,end='')
player2 = input()
player2 = colored(player2,'green')
print("LET'S BEGIN THE WAR")
os.system("Timeout -1")
key=0
key1 = 0
while(True):
    #WHITE'S TURN
    while(key%2 == 0):
        key1 = 0
        printboard()
        p1print2 = colored(" : Provide your move without space",'yellow')
        print(player1,p1print2,takenpieces)
        findex, tindex = getinput()
        findex, tindex = checkwhitepiece(findex, tindex)
        
        
        #IF THE SELECTED PIECE IS PAWN
        if(board[findex[0]][findex[1]][5+1] == 'P'):
            while(movepawn()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS ROOK
        elif(board[findex[0]][findex[1]][5+1] == 'R'):
            while(moverook()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS KNIGHT
        elif(board[findex[0]][findex[1]][5+1] == 'N'):
            while(moveknight()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS BISHOP
        elif(board[findex[0]][findex[1]][5+1] == 'B'):
            while(movebishop()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            #IF THE SELECTED PIECE IS QUEEN
        elif(board[findex[0]][findex[1]][5+1] == 'Q'):
            while(movebishop() and moverook()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
         
            
            #IF THE SELECTED PIECE IS KING
        elif(board[findex[0]][findex[1]][5+1] == 'K'):
            while(moveking()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
        key += 1
        
        
    #BLACK'S TURN
    while(key%2 == 1):
        key1 = 0
        printboard()
        p2print2 = colored(" : Provide your move without space",'green')
        print(player2,p2print2,takenpieces)
        findex, tindex = getinput()
        findex, tindex = checkblackpiece(findex, tindex)
        
        
        #IF THE SELECTED PIECE IS PAWN
        if(board[findex[0]][findex[1]][5+1] == 'P'):
            while(movepawn()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS ROOK
        elif(board[findex[0]][findex[1]][5+1] == 'R'):
            while(moverook()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS KNIGHT
        elif(board[findex[0]][findex[1]][5+1] == 'N'):
            while(moveknight()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS BISHOP
        elif(board[findex[0]][findex[1]][5+1] == 'B'):
            while(movebishop()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS QUEEN
        elif(board[findex[0]][findex[1]][5+1] == 'Q'):
            while(movebishop() and moverook()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
            
            
        #IF THE SELECTED PIECE IS KING
        elif(board[findex[0]][findex[1]][5+1] == 'K'):
            while(moveking()):
                key1 = 1
                break
            if(key1):
                print("NOT VALID")
                os.system("Timeout -1")
                continue
                
            if(board[tindex[0]][tindex[1]]):
                board[tindex[0]][tindex[1]] = colored(board[tindex[0]][tindex[1]])
                takenpieces.add(board[tindex[0]][tindex[1]])
            board[tindex[0]][tindex[1]] = board[findex[0]][findex[1]]
            board[findex[0]][findex[1]] = 0
            findex, tindex = [0,0]
        key += 1
