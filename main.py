from game_engine import GameEngine

GAME_FPS = 20
GAME_LENGTH = 10  # s
SCREEN_SIZE = [800, 800]
CHARACTER_SIZE = [50, 20]
CHARACTER_COLOUR = (200, 50, 0)
OBSTACLE_SIZE = [100, 100]
CONTROLLER_SELECTION = 0


def main(params):
    game_engine = GameEngine(params, use_graphics=False)


if __name__ == '__main__':
    game_parameters = {'GAME_FPS': GAME_FPS,
                       'GAME_LENGTH': GAME_LENGTH,
                       'SCREEN_SIZE': SCREEN_SIZE,
                       'CHARACTER_SIZE': CHARACTER_SIZE,
                       'CHARACTER_COLOUR': CHARACTER_COLOUR,
                       'OBSTACLE_SIZE': OBSTACLE_SIZE,
                       'CONTROLLER_SELECTION': CONTROLLER_SELECTION}
    main(game_parameters)

