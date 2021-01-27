import pygame


class RenderEngine:

    BACKGROUND = (40, 40, 40)

    def __init__(self, screen, params):
        self.screen = screen

        self.character = {'colour': params['CHARACTER_COLOUR'],
                          'size': params['CHARACTER_SIZE'],
                          'render_offset': [int(i/2) for i in params['CHARACTER_SIZE']]}

        self.obstacle = {'colour': (255, 255, 255),
                         'start_dist': 5000,
                         'size': params['OBSTACLE_SIZE']}

    def render(self, to_render):
        self.screen.fill(self.BACKGROUND)
        self._render_obstacle(to_render['obstacle_lst'])
        self._render_character(to_render['character_pos'])


    def _render_character(self, pos):
        rect = (pos[0] - self.character['render_offset'][0],
                pos[1] - self.character['render_offset'][1],
                self.character['size'][0], self.character['size'][1])
        self.screen.fill(self.character['colour'], rect)

    def _render_obstacle(self, obs_lst):
        for obs in obs_lst:
            self._render_single_obstacle(obs)

    def _render_single_obstacle(self, obs):
        dist_scaling = (self.obstacle['start_dist'] - obs[2]) / self.obstacle['start_dist']
        rect_size = [self.obstacle['size'][i] * dist_scaling for i in [0, 1]]
        rect = (int(obs[0] - rect_size[0]/2), int(obs[1] - rect_size[1]/2), int(rect_size[0]), int(rect_size[1]))

        colour_val = int(-255 / (self.obstacle['start_dist']**2) * obs[2]**2 + 255)
        colour = (colour_val, colour_val, colour_val)

        self.screen.fill(colour, rect)

