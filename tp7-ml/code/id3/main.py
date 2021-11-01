from decisiontree import decisionTree


# ### How to csv into python. Or I have to do it myself?
dataset = []

decisionTree = decisionTree(dataset, ['a', 'b', 'c'], 'played', 0)
print(decisionTree.root.value, decisionTree.root.children)
