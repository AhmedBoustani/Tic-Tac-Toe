import sys # To use sys.stdout to print without endline

# Draw the game board
def Draw (game):
  ceil = " ---"
  side = "|"
  for i in range(0, 4):
    print 3 * ceil
    if i < 3:
      for j in range(0, 3):
        sys.stdout.write(side + " " + game[i][j] + " ")
        sys.stdout.flush()
      print side


# Check if the query is X or O
def isEqual(query, p1, p2):
  if query == 'X':
    p1 = p1 + 1
  elif query == 'O':
    p2 = p2 + 1
  return (p1, p2)


# Check if a player reached 3
def checker(p1, p2):
  if p1 == 3:
    return (1, 0)
  elif p2 == 3:
    return (0, 2)
  return (0, 0)

# Check if a player won
def If_won(game):
  p1 = 0
  p2 = 0
  # Horizontal Checking
  for i in range(0, 3):
    for j in range(0, 3):
      (p1, p2) = isEqual(game[i][j], p1, p2)
    (s1, s2) = checker(p1, p2)
    if (s1, s2) != (0, 0):
      return (s1, s2)
    (p1, p2) = (0, 0)
  # Vertical Checking
  for k in range(0, 3):
      for l in range(0, 3):
        (p1, p2) = isEqual(game[l][k], p1, p2)
      (s1, s2) = checker(p1, p2)
      if (s1, s2) != (0, 0):
          return (s1, s2)
      (p1, p2) = (0, 0)
  # Diagonal Checking
  for m in range(0, 3):
    (p1, p2) = isEqual(game[m][m], p1, p2)
  return checker(p1, p2)

# Count the number of empty fields in the board
def Count(lst):
  c = 0
  for i in range(0, 3):
    for j in range(0, 3):
        if lst[i][j] == ' ':
          c = c + 1
  return c

# Declare the winner
def finish(game):
  (p1, p2) = If_won(game)
  if (p1 == 1):
      print "Player 1 won!"
      return True
  if (p2 == 2):
      print "Player 2 won!"
      return True
  return False

# Play the game
def handle_input():
  game = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

  print "Player1 is X, Player2 is O"
  
  Draw(game)
  
  while Count(game) != 0:
    flag = False
    (p1, p2) = If_won(game);
  
    while flag == False and (p1, p2) == (0, 0):
      row, column = raw_input("Player1--> Enter coordinates for X: ").split(", ")
      row, column = int(row), int(column)

      if game[row - 1][column - 1] == ' ':
        game[row - 1][column - 1] = 'X'
        flag = True
      else:
        print ("Position already in use, try again!")

    Draw(game)

    if finish(game):
      break
    if Count(game) == 0:
      break
    
    flag = False

    while flag == False:
      row, column = raw_input("Player2--> Enter coordinates for O: ").split(", ")
      row, column = int(row), int(column)
      if game[row - 1][column - 1] == ' ':
        game[row - 1][column - 1] = 'O'
        flag = True
      else:
        print ("Position already in use, try again!")

      Draw(game)

    if finish(game):
        break

handle_input()


