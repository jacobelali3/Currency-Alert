import jsonlines
import pandas as pd
import json
from collections import defaultdict

class currencyAlert():

  def __init__(self, entryIndex = 0, averageTime = 0, item = {}):

      self.entryIndex = entryIndex
      self.averageTime = averageTime
      self.item = item

   #Calculates a rolling average based on currencyPair based on 5 min average
  def averageRate(self, entryCounter, currencyDivider):
     counter = entryCounter
     windowSize = 300  #5 minutes at 1 second per entry = 300 entries. So we measure the window as 300

     df = pd.DataFrame.from_dict(currencyDivider, orient='index').rolling(windowSize, min_periods=0, axis='columns').mean()
     df = df.loc[:, counter]
     averageValues = df.to_dict()
     return averageValues

   #this function will read, manipulate data and print alerts
  def Main(self, fileName):

      currencyDivider = defaultdict(list)
      currencyData= {}
      averageRates = {}

       #Reading currency entries from file
      with open(fileName, "r+", encoding="utf8") as f:
        self.item = jsonlines.Reader(f)

        for entries in self.item:



            currencyData[entries['currencyPair']] = entries['rate']

            for key, value in currencyData.items():
                currencyDivider[key].append(value)


            averageRates = currencyAlert().averageRate(self.entryIndex, currencyDivider)

            #compare rate to 10% range of average
            if entries['rate'] >= (1.1* averageRates[entries['currencyPair']]) or entries['rate'] <= (0.9* averageRates[entries['currencyPair']]):
                 entries.pop('rate')
                 entries['alert'] = 'spotChange'
                 print(json.dumps(entries))

            else:
                 continue

            self.entryIndex = self.entryIndex + 1


if __name__ == "__main__":
     fileName = input("Please enter the JSON file name including the file extension (eg: input1.jsonl)\n")
     currencyAlert().Main(fileName)



























