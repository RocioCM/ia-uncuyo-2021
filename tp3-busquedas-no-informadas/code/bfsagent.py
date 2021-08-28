from agent import Agent


class AgentBFS(Agent):
    def getNextNode(self):
        frontier = self.frontier
        try:
            return frontier.pop(0)  # Queue
        except (IndexError):
            return None
