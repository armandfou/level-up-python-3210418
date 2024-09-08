import csv


def merge_csv(arrayOfCsvFileNameInput, csvFileNameOutput):
  inputEntries = {}
  for fileName in arrayOfCsvFileNameInput:
    with open(fileName, "r") as f:
      inputEntries[fileName] = list(csv.DictReader(f))
  fieldNameSet = set({})
  for j in inputEntries.values():
    fieldNameSet = fieldNameSet.union(set(j[1].keys()))

  resLine = {}
  resultsOutput = []
  for inputFileValue in inputEntries.values():
    for lineOfResults in inputFileValue:
      for fieldOfTheSet in  fieldNameSet:
        if fieldOfTheSet in inputFileValue[1].keys():
            resLine[fieldOfTheSet] = lineOfResults[fieldOfTheSet]
        else:
          resLine[fieldOfTheSet] = None
      resultsOutput.append(resLine)  
      resLine = {}
  with open(csvFileNameOutput, "w") as f:
    writer   = csv.writer(f)
    writer.writerow(list(fieldNameSet))
    for row in resultsOutput:
      writer.writerow(row.values())

merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')