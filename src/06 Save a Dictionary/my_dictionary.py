import json 
def save_dict( dict,filePath):
  with open(filePath, "w") as outfile: 
    json.dump(dict, outfile)
    outfile.close()
def load_dict(filePath):
  with open(filePath, "r") as outfile:
    jsonString = outfile.read() 
    return json.loads(jsonString)
test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.pickle')
recovered = load_dict('test_dict.pickle')
print(recovered)