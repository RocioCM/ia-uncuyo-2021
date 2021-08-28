from agent import Agent


class AgentDFS(Agent):
    def getNextNode(self):
        frontier = self.frontier
        try:
            return frontier.pop()  # Stack
        except (IndexError):
            return None

    def sucesor(self):
        depthLimit = self.environment.size*3
        if (self.state.distance >= depthLimit):
            return []
        return super().sucesor()
