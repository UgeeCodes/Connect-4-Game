def make_board(rows, columns):
    board = []
    for i in range(rows):
      board.append([])
      for x in range(columns):
        board[i].append('.')
    return board

def print_board(board):
    z = ''
    for i in range(len(board)):
        new_board = ''
        for j in range(len(board[i])):
            new_board += board[i][j]
        print(new_board)
    print(z)
    pass
       

def make_move(token_color, column, board):
    # update 'board', by placing a token
    # of 'token_color' in 'column'.
    a = board
    print_board(a)
    if column < 0 or column > len(board) or board[0][column] != '.':
        raise Exception('illegal move')
    else:
      for i in range(len(board)):
        if board[len(board)-1-i][column] == '.':
          board[len(board)-1-i][column] = token_color
          return board
    pass

def evaluate_board(board):
    #   '.' - nobody has won yet
    #   'R' - there are 4 'R' tokens in a row: this 
    #         is a win for 'R'
    #   'Y' - there are 4 'Y' tokens in a row: this
    #         is a win for 'Y'
    #   'T' - the game is a tie: all cells full and no 
    #         lines of 4 tokens for either player
    for i in range(len(board)):
      for j in range(len(board[i])):
        # vertical
        if i + 3 < len(board) and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j] and board[i][j] == board[i + 3][j] and board[i][j] != '.':
          return board[i][j]
        # horizontal
        elif j + 3 < len(board[0]) and board[i][j] != '.' and board[i][j] == board[i][j + 1] and board[i][j] == board[i][j + 2] and board[i][j] == board[i][j + 3]:
          return board[i][j]
        # diagonal
        elif i + 3 < len(board) and j + 3 < len(board[i]) and board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i + 2][j + 2] and board[i][j] == board[i + 3][j + 3] and board[i][j] != '.':
          return board[i][j]
        elif i - 3 >= 0 and j + 3 < len(board[i]) and board[i][j] == board[i - 1][j + 1] and board[i][j] == board[i - 2][j + 2] and board[i][j] == board[i - 3][j + 3]:
          return board[i][j]
        # opposite diagonal
        elif i + 3 < len(board) and j - 3 >= 0 and board[i][j] != '.' and board[i][j] == board[i + 1][j - 1] and board[i][j] == board[i + 2][j - 2] and board[i][j] == board[i + 3][j - 3]:
          return board[i][j]
        # no winner
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == '.':
          return '.'
    return 'T'


if __name__ == '__main__':
  board = make_board(6, 7)

  score = '.'

  while score == '.':
    c = int(input('R move: which column? '))
    make_move('R', c, board)
    print_board(board)
    score = evaluate_board(board)
      
    if score == '.':
      c = int(input('Y move: which column? '))
      make_move('Y', c, board)
      print_board(board)
      score = evaluate_board(board)
    
  # if the game is over
  # either one of the players won, or it's a tie
  if score == 'R':
    print('R wins')
  elif score == 'Y':
    print('Y wins')
  elif score == 'T':
    print('tie game')


