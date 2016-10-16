def Board (v, h):
  ceil = " ---"
  side = "|   "
  for i in range(0, h + 1):
    print v * ceil
    if i < h:
      print (h + 1) * side

v, h = raw_input().split("x")

Board (int(v), int(h))


