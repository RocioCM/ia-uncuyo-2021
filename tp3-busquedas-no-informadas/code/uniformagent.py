from agent import Agent


class AgentUniform(Agent):
    def getNextNode(self):
        frontier = self.frontier
        try:
            frontier.sort(key=(lambda node: node.distance))  # Priority Queue
            return frontier.pop(0)
        except (IndexError):
            return None

    def isExplorablePosition(self, position):
        node = self.environment.getNodeAt(position)
        currentDistance = self.state.distance + 1
        # The position is explorable if it's not an obstacle and it's not explored nor in the frontier.
        # But in uniform search, the position is ALSO explorable if it's on the frontier and its previous distance is greater that the distance on the current path.
        return not(node.isObstacle) and (node.status == 0 or (node.distance > currentDistance))
