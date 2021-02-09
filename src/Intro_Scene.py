from Scene import Scene
import pygame



class Intro_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('IntroScene')


    def start(self):
        print('Se inicia: ', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (225, 225, 225), (self.app.width/2, self.app.height/2), 30)

    def exit(self):
        print('Termina: ', self.name)

