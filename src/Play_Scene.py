from Scene import Scene
import pygame



class Play_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')


    def start(self):
        print('Se inicia: ', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('intro')
            print('', pygame.key)

    def update(self):
        pass

    def draw(self):
        self.screen.fill((225, 225, 225))
        pygame.draw.circle(self.screen, (0, 0, 0), (self.app.width/2, self.app.height/2), 30)

    def exit(self):
        print('Termina: ', self.name)

