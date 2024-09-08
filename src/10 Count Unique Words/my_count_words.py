import re
def count_words(filePath):
  with open(filePath, "r") as infile:
    s = infile.read()
    tokens =[token.upper() for token in re.findall(r'[0-9a-zA-Z-]+', s)]
    setWord = list(set(tokens))
    dict = {}
    
    for i in tokens:
      if i in dict.keys():
        dict[i] = dict[i] + 1
      else:
        dict[i] = 1
    def myFunc(e):
      if e in dict.keys():
        return dict[e]
      else:
        return 0
    
    print("Total words: ", len(tokens))
    print("Top 20 words:")
  #  print(setWord.sort(reverse=True, key=myFunc))
   
  #
    setWord.sort(reverse=True, key=myFunc)
    print(setWord[0:20])
    for i in setWord[0:20]:
      print(i, " ", dict[i])
count_words('shakespeare.txt')