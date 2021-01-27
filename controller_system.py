import pygame


class Controller:

    KEY_MAP = {'Down': pygame.K_DOWN,
               'Up': pygame.K_UP,
               'Left': pygame.K_LEFT,
               'Right': pygame.K_RIGHT}

    def __init__(self):
        self.direction = {'Left': False, 'Right': False, 'Up': False, 'Down': False}
        self.force_magnitude = {'X': 5, 'Y': 3}

    def update(self, event_list):
        direction_changed = False
        for event in event_list[::-1]:
            if event.type == pygame.KEYDOWN:
                if event.key == self.KEY_MAP['Up']:
                    self.direction['Up'] = True
                    self.direction['Down'] = False
                    direction_changed = True
                elif event.key == self.KEY_MAP['Down']:
                    self.direction['Down'] = True
                    self.direction['Up'] = False
                    direction_changed = True
                elif event.key == self.KEY_MAP['Left']:
                    self.direction['Left'] = True
                    self.direction['Right'] = False
                    direction_changed = True
                elif event.key == self.KEY_MAP['Right']:
                    self.direction['Right'] = True
                    self.direction['Left'] = False
                    direction_changed = True
                # Only take most recent direction command
                if direction_changed:
                    break

        for event in event_list[::-1]:
            if event.type == pygame.KEYUP:
                if event.key == self.KEY_MAP['Up']:
                    self.direction['Up'] = False
                elif event.key == self.KEY_MAP['Down']:
                    self.direction['Down'] = False
                elif event.key == self.KEY_MAP['Left']:
                    self.direction['Left'] = False
                elif event.key == self.KEY_MAP['Right']:
                    self.direction['Right'] = False

    @property
    def force(self):
        ret_val = [0, 0]
        if self.direction['Left']:
            ret_val[0] = -1 * self.force_magnitude['X']
        elif self.direction['Right']:
            ret_val[0] = self.force_magnitude['X']
        if self.direction['Up']:
            ret_val[1] = -1 * self.force_magnitude['Y']
        elif self.direction['Down']:
            ret_val[1] = self.force_magnitude['Y']
        return ret_val
