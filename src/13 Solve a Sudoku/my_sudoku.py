def valid_line(sudoku_arr, sudoku_rayure, line):
  for i, j in enumerate(sudoku_arr[line]):
    if (j > 0):
      for k in range(9):
        sudoku_rayure[i][k].difference(set([j]))
  return sudoku_rayure

def valid_colonne(sudoku_arr, sudoku_rayure, colonne):
  for line in sudoku_arr:
    if (line[colonne] > 0):
      for k in range(9):
        sudoku_rayure[k][colonne].difference(set([line[colonne]]))
  return sudoku_rayure

def valid_carre(sudoku_arr, sudoku_rayure,startLine ,startColonne):
  for ligne in range(startLine, startLine + 3):
    for colonne in range(startColonne, startColonne + 3):
      print(ligne, " " , colonne)
      if (sudoku_arr[ligne][colonne] > 0):
          for ligne in range(startLine, startLine + 3):
            for colonne in range(startColonne, startColonne + 3):
              sudoku_rayure[ligne][colonne].difference(set([sudoku_arr[ligne][colonne]]))
  return sudoku_rayure
  
def sudoku_rayure_has_change(sudoku_rayure_old, sudoku_rayure_new):
  for ligne in range(0,9):
    for colonne in range(0,9):
      if len(sudoku_rayure_old[ligne][colonne].symmetric_difference(sudoku_rayure_new[ligne][colonne]))!=0:
        return True
  return False
def solve_sudoku(sudoku_arr):
  sudoku_rayure_old = [[set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                      [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                      [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], 
                       [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])], ]
  a = [1,2,3,4,5,6,7,8,9]
  sudoku_rayure = [[set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                      [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                       [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                       [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                         [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                         [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                         [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                       [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],
                         [set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a),set(a)],]
  while(sudoku_rayure_has_change(sudoku_rayure_old, sudoku_rayure)):
    sudoku_rayure_old = sudoku_rayure
    for i in range(0,9):
      sudoku_rayure = valid_line(sudoku_arr, sudoku_rayure, i)
    for i in range(0,9):
      sudoku_rayure = valid_colonne(sudoku_arr, sudoku_rayure, i)
    for startLine in range(0, 9, 3):
      for startColonne in range(0, 9, 3):
        sudoku_rayure = valid_carre(sudoku_arr, sudoku_rayure,startLine ,startColonne)
    print(sudoku_rayure)
test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]



print(solve_sudoku(test_puzzle))