from random import randrange


class Agent:
    statesCount = 1
    frontier = []
    path = []

    def __init__(self, environment):
        self.environment = environment
        environment.agent = self
        self.initialNode = self.findAvailablePosition()
        self.targetNode = self.findAvailablePosition()
        self.state = self.initialNode
        self.think()

    def findAvailablePosition(self):
        # Returns a random node available to use as initial position or target position.
        availablePosition = False
        while (not(availablePosition)):
            positionX = randrange(self.environment.size)
            positionY = randrange(self.environment.size)
            if (not(self.environment.hasObstacle((positionY, positionX)))):
                availablePosition = True
        return self.environment.getNodeAt((positionY, positionX))

    def isExplorablePosition(self, position):
        # The position is explorable if it's not an obstacle and it's not already explored nor in the frontier.
        node = self.environment.getNodeAt(position)
        return not(node.isObstacle) and (node.status == 0)

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
        frontier = self.frontier
        try:
            # Priority Queue. Prioritize paths with shorter distances already to explore.
            frontier.sort(key=lambda node: (node.cost - node.distance**0.5))
            return frontier.pop(0)
        except (IndexError):
            return None

    def heuristic(self, position):
        targetPosition = self.targetNode.position
        return abs(position[0] - targetPosition[0]) + abs(position[1] - targetPosition[1])

    def sucesor(self):
        position = self.state.position
        nodeFrontier = []
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
        # 1. Check the initial state.
        currentNode = self.state
        currentNode.distance = 0
        currentNode.status = 2  # Visited
        if (currentNode == self.targetNode):
            currentNode = None
        while (currentNode != None):
            # 2. Update the current state.
            self.state = currentNode
            self.state.status = 2  # Visited

            # 3. Find the possible next states (add new nodes to the frontier).
            nodeFrontier = self.sucesor()
            # 3.1 Check if any of the new frontier nodes are the target node and update them, then add them to the frontier.
            reachedTarget = False
            for node in nodeFrontier:
                if (node.status == 0):  # In uniform search, node may already be on the frontier (status == 1)
                    self.frontier.append(node)
                node.status = 1  # Frontier
                node.prevNode = self.state
                node.distance = self.state.distance + 1
                node.cost = node.distance + self.heuristic(node.position)
                if (node == self.targetNode):
                    reachedTarget = True
                    break
            if (reachedTarget):
                break

            # 4. Choose the next state from the possible next states (depending on the selected search algorithm)
            currentNode = self.getNextNode()
            self.statesCount += 1

        # 5. Draw the path. Starting from the target up to the initial node.
        target = self.targetNode
        if (target.prevNode == None):
            self.path = None
            return
        node = target
        while (node != None):
            node.status = 3  # Path
            self.path.insert(0, node.position)
            node = node.prevNode

    def getPerformance(self):
        return (self.statesCount, self.path)
