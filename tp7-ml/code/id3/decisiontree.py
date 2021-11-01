class Tree():
    root = None

    def __init__(self, root):
        self.root = root


class Node:
    value = None
    classify = None
    children = []


class Object(object):  # Dynamic object, like javascript objects.
    def __init__(self, mapping=[]):
        for pair in mapping:
            [key, value] = pair
            setattr(self, key, value)


def classifyByKey(dataset, attribute):
    # Return an array containing the elements in the dataset filtered by the value of the given attribute.

    classification = [(1, dataset)]
    classification = []
    for element in dataset:
        value = element[attribute]
        classIndex = None
        for i in range(len(classification)):
            classValue = classification[i][0]
            if (classValue == value):
                classIndex = i
                break
        if (classIndex != None):
            # Adds the element to the array of its class.
            classification[i][1].append(element)
        else:
            # Creates a new class including just this element.
            classification.append((value, [element]))
    return classification


def orderByBestClassifier(classificationsByKey):
    # ### Code this function.
    # Make a sort of that array based on how good is the classification with that attribute.
    # Podría ser contando la cantidad de clases que no son completamente determinantes y ordenar inversamente a eso. Yyyy, algun otro modificador basado en la distribución de los elementos en esas clases no determinantes.
    return classificationsByKey


def classifierFunction(classification, attribute):
    def classify(element):
        # Given a new element to classify in an internal node of the decision tree,
        # this function decides to which of the children nodes this new element belongs.
        elementValue = element[attribute]
        for i in range(len(classification)):
            childValue = classification[i][0]
            if (elementValue == childValue):
                return i
        raise Exception("Factor " + attribute +
                        " has new levels " + elementValue)

    # This callback is assigned once to each internal node in the decision tree.
    return classify


def areAllFromTheSameClass(dataset, attribute):
    value = dataset[0][attribute]
    for element in dataset:
        if (element[attribute] != value):
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

    # 2. Elegir la propiedad más ponderante.
    classificationsByEachKey = orderByBestClassifier(classificationsByEachKey)
    [key, classification] = classificationsByEachKey.pop()

    # 3.1. Computes the classifier function for this node (given a new element, this function will decide in which of the children it should be classified).
    root.classify = classifierFunction(classification)
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
    keysToEvalLeft = keysToEval.copy().remove(key)

    # 5. Recursive call for the children that need further classification.
    for node in root.children:
        if (type(node.value) == list):
            subtreeDataset = node.value
            node.value = None
            subTree = findTreeRecursive(subtreeDataset, keysToEvalLeft,
                                        keyToPredict, default)
            node.children = subTree
            # ### or alternatively, if necessary, do:
            # node.classify = subTree.classify
            # node.children = subTree.children
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
