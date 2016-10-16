def Count(lst):
  c = 0
  for i in range(0, 3):
    for j in range(0, 3):
      if lst[i][j] == 0:
          c = c + 1
  return c

def handle_input():
  game = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
  print "Player1 is X, Player2 is O"
  for i in range(0, 3):
    print ", ".join(map(str, game[i]))

  while Count(game) != 0:
    flag = False
    while flag == False:
      row, column = raw_input("Player1--> Enter coordinates for X: ").split(", ")
      row, column = int(row), int(column)
      if game[row - 1][column - 1] == 0:
        game[row - 1][column - 1] = 'X'
        flag = True
      else:
        print ("Position already in use, try again!")
    for i in range(0, 3):
      print ", ".join(map(str, game[i]))
    if Count(game) == 0:
      break
    flag = False
    while flag == False:
      row, column = raw_input("Player2--> Enter coordinates for O: ").split(", ")
      row, column = int(row), int(column)
      if game[row - 1][column - 1] == 0:
        game[row - 1][column - 1] = 'O'
        flag = True
      else:
        print ("Position already in use, try again!")
    for i in range(0, 3):
      print ", ".join(map(str, game[i]))

handle_input()

