from decisiontree import decisionTree, Object
import csv

file = open('tennis.csv')
csvReader = csv.reader(file)
dataset = []
attributes = next(csvReader)
for rowValues in csvReader:
    element = Object(attributes, rowValues)
    dataset.append(element)
file.close()

formulaAttributes = attributes.copy()
formulaAttributes.remove('play')

decisionTree = decisionTree(dataset, formulaAttributes, 'play', 'yes')
