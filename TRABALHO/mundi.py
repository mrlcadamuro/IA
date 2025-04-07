# Objeto Mapa
# - pais
# - estados
"""
Revisão de 00, relembrando injeçção de dependecias e estrutuea de dados ' Grafo '
"""


class State:
    """
    Classe que define estados de uma nação 
    """
    def __init__(self, state_name, size):
        self.state_name = state_name
        self.size = size


class Country:
    """
    Classe que define uma nação     
    """
    def __init__(self, country_name, flag):
        self.coutry_name = country_name
        self.flag = flag
        self.states = []
       
    def add_state(self, state: State):
        self.states.append(state)


    def list_states(self):
        for state in self.states:
            print(state)


class World_Map:
    """
    Classe que cria o mapa mundi.
    """
    brazil = Country("Brazil", "🇧🇷")
    argentina = Country("Argentina", "AR")

brazil.add_state(State("São Paulo", 10))
brazil.add_state(State("Rio e Janeiro", 8))
brazil.add_state(State("Minas Gerais", 5))