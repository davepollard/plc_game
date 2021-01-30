import pygame
import random
from render_engine import RenderEngine
from character_object import CharacterObject


class GameEngine:

    def __init__(self, params, use_graphics=True):

        self.fps = params['GAME_FPS']
        self.fps_clock = pygame.time.Clock()

        self.use_graphics = use_graphics

        self.character_size = params['CHARACTER_SIZE']
        self.obstacle_size = params['OBSTACLE_SIZE']

        if self.use_graphics:
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
        self.missed = 0
        self.frames_remaining = params['GAME_LENGTH'] * params['GAME_FPS']

        self.running = True
        self.main_loop()

    def main_loop(self):
        while self.running:
            if self.use_graphics:
                event_list = pygame.event.get()

                # Check for quit command
                for event in event_list:
                    if event.type == pygame.QUIT:
                        self.running = False
            else:
                event_list = []

            # Update position
            self.character.update(event_list)
            self._update_obstacle()

            if self.use_graphics:
                # Update render engine
                self.render_list['character_pos'] = self.character.current_position
                self.render_list['obstacle_lst'] = self.obstacle_list
                self.render_engine.render(self.render_list)
                self.render_engine.render_score(self.points, self.missed, self.frames_remaining)

                pygame.display.update()
                self.fps_clock.tick(self.fps)

            self.frames_remaining -= 1
            if self.frames_remaining <= 0:
                self.running = False

        self._display_score()

    def _init_obstacle(self):
        self.obstacle_list = [[random.randint(200, 600), random.randint(200, 600), i] for i in range(100, 5000, 1000)]

    def _update_obstacle(self):
        speed = self.character.speed
        for i in range(0, len(self.obstacle_list)):
            self.obstacle_list[i][2] -= speed

        if self.obstacle_list[0][2] <= 0:
            if self.is_inside(self.obstacle_list[i]):
                self.points += 1
            else:
                self.missed += 1

            # Rotate list and add a new obstacle
            self.obstacle_list = self.obstacle_list[1:] + self.obstacle_list[:1]
            self.obstacle_list[-1] = [random.randint(200, 600), random.randint(200, 600), 5000]

    def _display_score(self):
        print('Game Over')
        print('Passed: %i' % self.points)
        print('Missed: %i' % self.missed)
        print('Score: %i' % self.score)

    def is_inside(self, obs):
        p = self.character.current_position
        x_lims = [p[0] - self.character_size[0]/2 > obs[0] - self.obstacle_size[0]/2,
                  p[0] + self.character_size[0]/2 < obs[0] + self.obstacle_size[0]/2]

        y_lims = [p[1] - self.character_size[1] / 2 > obs[1] - self.obstacle_size[1] / 2,
                  p[1] + self.character_size[1] / 2 < obs[1] + self.obstacle_size[1] / 2]

        if all(x_lims) and all(y_lims):
            return True
        return False

    @property
    def score(self):
        return self.points - self.missed**2

