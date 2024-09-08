import secrets


def splitLines(line):
  lineSplited = line.split()
  if len(lineSplited) > 1:
      return (lineSplited[0], lineSplited[1])
  else: 
    return ("line","")


def generate_passphrase(num_words, wordlist_path='diceware.wordlist.asc'):
  with open(wordlist_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    dict = {splitLines(line)[0]: splitLines(line)[1]  for line in lines[2:]} 
    resultArray = []
    for i in range(0, num_words):
      resultArrayOfALine = []
      for j in range(0, 5):
         resultArrayOfALine.append(str(secrets.choice(range(1, 7))))
      resultArray.append(resultArrayOfALine)
    wordList = [dict["".join(tutu)] for tutu in resultArray]
    return " ".join(wordList)
 



print(generate_passphrase(7))
print(generate_passphrase(7))