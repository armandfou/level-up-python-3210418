def valid_line(sudoku_arr, line):
  cpt = 0
  b = set()
  for a in sudoku_arr[line]:
    if (a > 0):
      cpt = cpt + 1
      b.add(a)
  if (len(b) < cpt):
    return False
  else:
    return True

def valid_colonne(sudoku_arr, colonne):
  b =set()
  cpt = 0
  for line in sudoku_arr:
    if (line[colonne] > 0):
      cpt = cpt + 1
      b.add(line[colonne])
  if (len(b) < cpt):
    return False
  else:
    return True

def valid_carre(sudoku_arr,startLine ,startColonne):
  b =set()
  cpt = 0
  for ligne in range(startLine, startLine + 3):
    for colonne in range(startColonne, startColonne + 3):
      if (sudoku_arr[ligne][colonne] > 0):
        cpt = cpt + 1
        b.add(sudoku_arr[ligne][colonne])
  if (len(b) < cpt):
    return False
  else:
    return True

def makesudoku_data_struct(sudoku_arr):
  sudo = []
  for i in range(0, 9):
    a = []
    for j in range(0, 9):
      if (sudoku_arr[i][j] > 0):
        a.append((sudoku_arr[i][j], True))
      else:
        a.append((sudoku_arr[i][j], False))
    sudo.append(a)
  return sudo


def incremente(sudoku_arr):
  sudo = []
  incNext = True
  for i in range(8, -1, -1):
    a = []
    for j in range(8, -1, -1):
      if (sudoku_arr[i][j][1] == False and sudoku_arr[i][j][0] < 9  and incNext):
        a.append((sudoku_arr[i][j][0] + 1, False))
        incNext = False
      elif(sudoku_arr[i][j][1] == False and sudoku_arr[i][j][0] == 9 and incNext):
        a.append((0, False))
      else:
        a.append(sudoku_arr[i][j])
    sudo.append(a)
  return sudo

def extend(sudoku_arr):
  extendNext = True
  sudo = []
  for i in range(0, 9):
    a =[]
    for j in range(0, 9):
      if (sudoku_arr[i][j][0] == 0 and extendNext == True):
        extendNext = False
        a.append((1, False))
      else:
        a.append(sudoku_arr[i][j])
    sudo.append(a)
  return sudo


def valid_sudok(sudoku_arr):
  for i in range(0,9):
      bool = valid_line(sudoku_arr, i)
      if (bool is False):
        return False
  for i in range(0,9):
    bool =  valid_colonne(sudoku_arr,  i)
    if (bool is False):
        return False
  for startLine in range(0, 9, 3):
    for startColonne in range(0, 9, 3):
      bool = valid_carre(sudoku_arr, startLine ,startColonne)
      if (bool is False):
        return False
  return True

def winner(sudoku_arr):
  for i in sudoku_arr:
    for j in i:
      a = j[0]
      if (a == 0):
        return False
  return valid_sudok(sudoku_arr)

def solve_sudok(sudoku_arr):
  sudok = sudoku_arr
  for startLine in range(0, 9):
    for startColonne in range(0, 9):
      if sudok[startLine][startColonne] == 0:
        for no in range(1, 10):
          if valid_sudok(sudoku_arr):
            sudok[startLine][startColonne] = no
            if trial := solve_sudok(sudok):
              return trial
            sudok[startLine][startColonne] = 0
        return False
  return sudok

tutu =  [[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]
    
test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]
test_puzzle1 =[[(5, True), (5, True), (0, False), (0, False), (7, True), (0, False), (0, False), (0, False), (0, False)], [(6, True), (0, False), (0, False), (1, True), (9, True), (5, True), (0, False), (0, False), (0, False)], [(0, False), (9, True), (8, True), (0, False), (0, False), (0, False), (0, False), (6, True), (0, False)], [(8, True), (0, False), (0, False), (0, False), (6, True), (0, False), (0, False), (0, False), (3, True)], [(4, True), (0, False), (0, False), (8, True), (0, False), (3, True), (0, False), (0, False), (1, True)], [(7, True), (0, False), (0, False), (0, False), (2, True), (0, False), (0, False), (0, False), (6, True)], [(0, False), (6, True), (0, False), (0, False), (0, False), (0, False), (2, True), (8, True), (0, False)], [(0, False), (0, False), (0, False), (4, True), (1, True), (9, True), (0, False), (0, False), (5, True)], [(0, False), (0, False), (0, False), (0, False), (8, True), (0, False), (0, False), (7, True), (9, True)]]

tutu = solve_sudok(test_puzzle)
print(tutu)
