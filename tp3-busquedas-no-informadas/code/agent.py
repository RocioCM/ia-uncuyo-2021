from random import randrange


class Agent:
    statesCount = 1
    frontier = []
    path = []

    def __init__(self, environment, searchType):
        self.environment = environment
        environment.agent = self
        self.searchType = searchType
        self.initialNode = self.findAvailablePosition()
        self.targetNode = self.findAvailablePosition()
        self.state = self.initialNode
        self.think()

    def findAvailablePosition(self):
        availablePosition = False
        while (not(availablePosition)):
            positionX = randrange(self.environment.size)
            positionY = randrange(self.environment.size)
            if (not(self.environment.hasObstacle(positionY, positionX))):
                availablePosition = True
        return self.environment.getNodeAt((positionY, positionX))

    def isExplorablePosition(self, position):
        node = self.environment.getNodeAt(position)
        return not(node.isObstacle) and node.status == 0

    def up(self):
        position = self.state.position
        if (position[0] > 0):
            return self.isExplorablePosition((position[0]-1, position[1]))

    def down(self):
        position = self.state.position
        if (position[0] < self.environment.size - 1):
            return self.isExplorablePosition((position[0]+1, position[1]))

    def left(self):
        position = self.state.position
        if (position[1] > 0):
            return self.isExplorablePosition((position[0], position[1]-1))

    def right(self):
        position = self.state.position
        if (position[1] < self.environment.size - 1):
            return self.isExplorablePosition((position[0], position[1]+1))

    def getNextNode(self):
        searchType = self.searchType
        frontier = self.frontier
        try:
            if (searchType == 0):  # Queue
                return frontier.pop(0)
            elif (searchType == 1):  # Priority Queue
                # TODO: check this sorting works!
                def distanceSort(node):
                    return node.distance
                frontier.sort(key=distanceSort)
                return frontier.pop(0)
            elif (searchType == 2):  # Stack
                return frontier.pop()
            else:
                raise Exception(
                    "No se eligió un método de búsqueda válido. \nMétodos válidos: \n  0 = BFS \n  1 = Búsqueda Uniforme \n  2 = DFS")
        except (IndexError):
            return None

    def sucesor(self):
        position = self.state.position
        nodeFrontier = []
        if (self.searchType == 2 and self.state.distance >= self.environment.size*3):
            # Depth limit reached for DFS
            return nodeFrontier
        if (self.up()):
            nodeFrontier.append(self.environment.getNodeAt(
                (position[0]-1, position[1])))
        if (self.down()):
            nodeFrontier.append(self.environment.getNodeAt(
                (position[0]+1, position[1])))
        if (self.left()):
            nodeFrontier.append(self.environment.getNodeAt(
                (position[0], position[1]-1)))
        if (self.right()):
            nodeFrontier.append(self.environment.getNodeAt(
                (position[0], position[1]+1)))
        return nodeFrontier

    def think(self):
        # 1. Miro este nodo.
        currentNode = self.state
        currentNode.distance = 0
        currentNode.status = 2
        if (currentNode == self.targetNode):
            currentNode = None
        while (currentNode != None):
            self.state = currentNode
            self.state.status = 2

            # 2. Pongo todos en la frontera.
            nodeFrontier = self.sucesor()
            # 2.1 Reviso que cada uno no sea el target y lo actualizo como visitado.
            reachedTarget = False
            for node in nodeFrontier:
                node.status = 1
                node.prevNode = self.state
                node.distance = self.state.distance + 1
                if (node == self.targetNode):
                    reachedTarget = True
                    break
            if (reachedTarget):
                break
            self.frontier.extend(nodeFrontier)

            # 3. Elijo un nuevo nodo y reitero.
            currentNode = self.getNextNode()
            self.statesCount += 1

        # 4. Marcar el camino. Empezando desde el destino y yendo por los previousNode hasta el inicial.
        target = self.targetNode
        if (target.prevNode == None):
            self.path = None
            return
        node = target
        while (node != None):
            node.status = 3
            self.path.insert(0, node.position)
            node = node.prevNode

    def getPerformance(self):
        return (self.statesCount, self.path)
