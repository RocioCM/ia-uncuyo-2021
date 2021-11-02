from math import log2


class Tree():
    root = None

    def __init__(self, root):
        self.root = root


class Node:
    value = None
    classify = None
    children = []


class Object(object):  # Dynamic object, like javascript objects.
    def __init__(self, attributes=[], values=[]):
        for i in range(len(attributes)):
            setattr(self, attributes[i], values[i])


def classifyByKey(dataset, attribute):
    # Return an array containing the elements in the dataset filtered by the value of the given attribute.

    classification = [(1, dataset)]
    classification = []
    for element in dataset:
        value = getattr(element, attribute)
        classIndex = None
        for i in range(len(classification)):
            classValue = classification[i][0]
            if (classValue == value):
                classIndex = i
                break
        if (classIndex != None):
            # Adds the element to the array of its class.
            classification[classIndex][1].append(element)
        else:
            # Creates a new class including just this element.
            classification.append((value, [element]))
    return classification


def entropyForAttribute(classification, attribute):
    def I(p1, p2):
        if (p1 == 0 or p2 == 0):
            return 0
        return -p1 * log2(p1) - p2 * log2(p2)

    entropy = 0
    total = 0
    for subClass in classification:
        elements = subClass[1]
        played = 0
        for element in elements:
            if (getattr(element, attribute) == 'yes'):
                played += 1
            total += 1
        entropy += len(elements) * I(played/len(elements),
                                     (len(elements) - played)/len(elements))
    entropy /= total
    return entropy


def findBestClassifier(classificationsByKey, attribute):
    # Returns the classification by the attribute with less entropy.

    bestEntropy = 1
    bestClassification = None
    for classification in classificationsByKey:
        entropy = entropyForAttribute(classification[1], attribute)
        print("ENTROPY FOR", classification[0], ":", entropy)
        if (entropy <= bestEntropy):
            bestClassification = classification
            bestEntropy = entropy
    return bestClassification


def classifierFunction(classification, attribute):
    def classify(element):
        # Given a new element to classify in an internal node of the decision tree,
        # this function decides to which of the children nodes this new element belongs.
        elementValue = getattr(element, attribute)
        for i in range(len(classification)):
            childValue = classification[i][0]
            if (elementValue == childValue):
                return i
        raise Exception("Factor " + attribute +
                        " has new levels " + elementValue)

    # This callback is assigned once to each internal node in the decision tree.
    return classify


def areAllFromTheSameClass(dataset, attribute):
    value = getattr(dataset[0], attribute)
    for element in dataset:
        if (getattr(element, attribute) != value):
            return (False, None)
    return (True, value)


def decisionTree(data, keysToEval, keyToPredict, default):
    treeRootNode = findTreeRecursive(data, keysToEval, keyToPredict, default)
    return Tree(treeRootNode)


def findTreeRecursive(data, keysToEval, keyToPredict, default):
    root = Node()

    # 0. Return default value if there's no data to analyze.
    if (len(data) == 0 or len(keysToEval) == 0):
        root.value = default
        return root

    # 1. Classify the dataset according to each of the keysToEval attributes.
    classificationsByEachKey = []
    for key in keysToEval:
        classification = classifyByKey(data, key)
        classificationsByEachKey.append((key, classification))

    # 2. Find the best classifier attribute-
    [key, classification] = findBestClassifier(
        classificationsByEachKey, keyToPredict)
    print("Selected attribute:", key)

    # 3.1. Computes the classifier function for this node (given a new element, this function will decide in which of the children it should be classified).
    root.classify = classifierFunction(classification, key)
    # 3.2 Fill the children array and determine if each child of this tree has a class or should have a subtree for further classification.
    for childData in classification:
        elements = childData[1]
        [isSingleClass, classValue] = areAllFromTheSameClass(
            elements, keyToPredict)
        child = Node()
        if (isSingleClass):
            child.value = classValue
        else:
            child.value = elements
        root.children.append(child)

    # 4. Filter the keys that are left to classify in the subtrees.
    keysToEvalLeft = keysToEval.copy()
    keysToEvalLeft.remove(key)

    # 5. Recursive call for the children that need further classification.
    for node in root.children:
        if (type(node.value) == list):
            subtreeDataset = node.value
            node.value = None
            subTree = findTreeRecursive(subtreeDataset, keysToEvalLeft,
                                        keyToPredict, default)
            node.classify = subTree.classify
            node.children = subTree.children
    return root


def predict(tree, element):
    prediction = None
    node = tree.root
    while (prediction == None):
        if (node.value != None):
            prediction = node.value
            break
        nextNodeIndex = node.classify(element)
        node = node.children[nextNodeIndex]
    return prediction
