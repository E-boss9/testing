def check_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    

board = [[None, None, None], 
         [None, None, None], 
         [None, None, None]]

turn = 'X'

running = True
winner = None
while running:
    for i, row in enumerate(board):
        for j, pos in  enumerate(row):
            print(f" [ {pos} ] ".center(len("----------|") - 1) + "|", end='' )
        print('\n', ("----------|"), ("----------|"), ("----------"), sep='')
    print('\n')

    while True:
        play = input (f"{turn}'s Turn:")
        play = play.replace(' ', '')
        if len(play) == 2 and play.isnumeric():
            play = (int(play[0]), int(play[1]))
            
            if 0 < play[0] < 4 and 0 < play[1] < 4:
                if board[play[0] - 1][play[1] - 1] == None:
                    board[play[0] - 1][play[1] - 1] = turn
                    break 
        print(play, "Wrong input")
    
    if None not in board[0] and None not in board[1] and None not in board[2]:
        running = False
        print('tst')
    
    winner = check_winner(board)
    if winner:
        running = False

    if turn == 'X': turn = 'O'
    else: turn = 'X'

if winner:
    print(f"{winner} Won \n GAME OVER")
else: print("TIE")


for i, row in enumerate(board):
    for j, pos in  enumerate(row):
        print(f" [ {pos} ] ".center(10), end='|' )
    print('\n', ("----------|"), ("----------|"), ("----------"), sep='')
print('\n')

