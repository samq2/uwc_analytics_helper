from pathlib import Path
import csv
import re


#path = str(Path.home()) + r"\documents\code\uwc_analytics\description_data.csv"
path = str(Path.home()) + r"\documents\code\uwc_analytics\u_simple_requests.csv"

def word_count_description(csvPath):
  requestDictionary = {} 
  maxCharacterDictionary = {}
  overMaxCounter = 0
  maxCharacter = 0
  requestNumberMaxCharacter = ''

  with open (csvPath, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

    row_count = len(data)
    for rows in range(row_count):
      if (re.search("Submitted by:", data[rows][1])) != None:
        if (len(data[rows][1])) >= 4000:
          overMaxCounter+=1
          requestDictionary.update({overMaxCounter:data[rows][0]})
        if (len(data[rows][1]) > maxCharacter):
          maxCharacter = len(data[rows][1])
          requestNumberMaxCharacter = data[rows][0]

  #print(requestNumberMaxCharacter + " is the one with the highest character with a count of " + str(maxCharacter))
        
  return requestDictionary
    # for rows in data[1:]:

overFourThousandCharacters  = word_count_description(path)

print(overFourThousandCharacters)

