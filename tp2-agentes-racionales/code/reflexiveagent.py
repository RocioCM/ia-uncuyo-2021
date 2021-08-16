from agent import Agent


class ReflexiveAgent(Agent):
    def think(self):
        if (self.percept == True):
            self.suck()
        else:
            print("Hola")
            # Insert as many if then as you want here.
            # Maybe, elegir entre alguna de las cuatro direcciones (nunca elegir idle) de forma aleatoria. Podria comprobar que si estoy al borde, no moverme para ese lado.
