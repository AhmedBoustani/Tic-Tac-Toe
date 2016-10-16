def isEqual(query, p1, p2):
  if query == 1:
    p1 = p1 + 1
  elif query == 2:
    p2 = p2 + 1
  return (p1, p2)

def checker(p1, p2, score):
  if p1 == score:
    return (1, 0)
  elif p2 == score:
    return (0, 2)
  return (0, 0)

def If_won(game, row, column, score):
  p1 = 0
  p2 = 0
  # Horizontal Checking
  for i in range(0, row):
    for j in range(0, column):
      (p1, p2) = isEqual(game[i][j], p1, p2)
    (s1, s2) = checker(p1, p2, score)
    if (s1, s2) != (0, 0):
      return (s1, s2)
    (p1, p2) = (0, 0)
  # Vertical Checking
  for k in range(0, column):
      for l in range(0, row):
        (p1, p2) = isEqual(game[l][k], p1, p2)
      (s1, s2) = checker(p1, p2, score)
      if (s1, s2) != (0, 0):
          return (s1, s2)
      (p1, p2) = (0, 0)
  # Diagonal Checking
  for m in range(0, column):
    (p1, p2) = isEqual(game[m][m], p1, p2)
  return checker(p1, p2, score)

