import pygame
import random
from render_engine import RenderEngine
from character_object import CharacterObject


class GameEngine:

    def __init__(self, params):

        self.fps = params['GAME_FPS']
        self.fps_clock = pygame.time.Clock()

        self.character_size = params['CHARACTER_SIZE']
        self.obstacle_size = params['OBSTACLE_SIZE']

        # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode(params['SCREEN_SIZE'])
        pygame.display.set_caption('plc rockets')
        self.render_engine = RenderEngine(screen, params)

        # Initialise game components
        self.character = CharacterObject(params)
        self._init_obstacle()

        self.render_list = {'character_pos': self.character.current_position,
                            'obstacle_lst': self.obstacle_list}

        self.points = 0

        self.running = True
        self.main_loop()

    def main_loop(self):
        while self.running:
            event_list = pygame.event.get()

            # Check for quit command
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.running = False

            # Update position
            self.character.update(event_list)
            self._update_obstacle()

            # Update render engine
            self.render_list['character_pos'] = self.character.current_position
            self.render_list['obstacle_lst'] = self.obstacle_list
            self.render_engine.render(self.render_list)

            pygame.display.update()
            self.fps_clock.tick(self.fps)

    def _init_obstacle(self):
        self.obstacle_list = [[random.randint(200, 600), random.randint(200, 600), i] for i in range(100, 5000, 1000)]

    def _update_obstacle(self):
        speed = self.character.speed
        for i in range(0, len(self.obstacle_list)):
            self.obstacle_list[i][2] -= speed
            if self.obstacle_list[i][2] <= 0:
                if self.is_inside(self.obstacle_list[i]):
                    self.points += 1

                self.obstacle_list[i] = [random.randint(200, 600), random.randint(200, 600), 5000]

    def is_inside(self, obs):
        p = self.character.current_position
        x_lims = [p[0] - self.character_size[0]/2 > obs[0] - self.obstacle_size[0]/2,
                  p[0] + self.character_size[0]/2 < obs[0] + self.obstacle_size[0]/2]

        y_lims = [p[1] - self.character_size[1] / 2 > obs[1] - self.obstacle_size[1] / 2,
                  p[1] + self.character_size[1] / 2 < obs[1] + self.obstacle_size[1] / 2]

        if all(x_lims) and all(y_lims):
            return True
        return False

