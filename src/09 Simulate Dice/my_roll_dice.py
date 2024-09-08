import random

def  roll_dice(*args):
  nbTirage = 1000000
  resultDice = []
  sumResultDice = []


  for i in range(len(args)):
    a = []
    for l in range(nbTirage):
      a.append(random.randrange(1, args[i] + 1))
    resultDice.append(a)
  for i in range(nbTirage):
    sum = 0
    for r in range(len(args)):
      sum = sum + resultDice[r][i]
    sumResultDice.append(sum)
  sumNumberSide = 0
  for r in range(len(args)):
    sumNumberSide = sumNumberSide + args[r]
  dict ={}
  for outcome in range(len(args), sumNumberSide + 1):
    for i in sumResultDice:
      if (outcome is i):
        if (outcome not in dict.keys()):
          dict[outcome] = 1
        else:
          dict[outcome] = dict[outcome] + 1
  print(dict)
  for k,j in dict.items():
    print(k, "   ", round( (j/ nbTirage) * 10000) / 100)

roll_dice(4, 6, 6)
roll_dice(4, 6, 6, 20)