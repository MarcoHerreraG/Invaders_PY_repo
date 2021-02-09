
class Scene():
    '''Clase abstracta scene para crear escenas en pygame   '''
    def __init__(self, name):
        self.name = name
        print('Escena creada: ', self.name)

    def start(self):
        raise NotImplementedError

    def process_events(self, events):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError
