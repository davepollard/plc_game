import pygame


class Controller:

    KEY_MAP = {'Down': pygame.K_DOWN,
               'Up': pygame.K_UP,
               'Left': pygame.K_LEFT,
               'Right': pygame.K_RIGHT,
               'Forward': pygame.K_a,
               'Backward': pygame.K_z}

    def __init__(self):
        self.direction = {'Left': False, 'Right': False, 'Up': False, 'Down': False, 'Forward': False, 'Backward': False}
        self.force_magnitude = {'X': 5, 'Y': 3, 'Z': 5}

    def update(self, event_list):
        direction_changed = [False, False, False]
        for event in event_list[::-1]:
            if event.type == pygame.KEYDOWN:
                if event.key == self.KEY_MAP['Up'] and not direction_changed[1]:
                    self.direction['Up'] = True
                    self.direction['Down'] = False
                    direction_changed[1] = True
                elif event.key == self.KEY_MAP['Down'] and not direction_changed[1]:
                    self.direction['Down'] = True
                    self.direction['Up'] = False
                    direction_changed[1] = True
                elif event.key == self.KEY_MAP['Left'] and not direction_changed[0]:
                    self.direction['Left'] = True
                    self.direction['Right'] = False
                    direction_changed[0] = True
                elif event.key == self.KEY_MAP['Right'] and not direction_changed[0]:
                    self.direction['Right'] = True
                    self.direction['Left'] = False
                    direction_changed[0] = True
                elif event.key == self.KEY_MAP['Forward'] and not direction_changed[2]:
                    self.direction['Forward'] = True
                    self.direction['Backward'] = False
                    direction_changed[2] = True
                elif event.key == self.KEY_MAP['Backward'] and not direction_changed[2]:
                    self.direction['Backward'] = True
                    self.direction['Forward'] = False
                    direction_changed[2] = True

                # Only take most recent direction command
                if all(direction_changed):
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
                elif event.key == self.KEY_MAP['Forward']:
                    self.direction['Forward'] = False
                elif event.key == self.KEY_MAP['Backward']:
                    self.direction['Backward'] = False

    @property
    def force(self):
        ret_val = [0, 0, 0]
        if self.direction['Left']:
            ret_val[0] = -1 * self.force_magnitude['X']
        elif self.direction['Right']:
            ret_val[0] = self.force_magnitude['X']
        if self.direction['Up']:
            ret_val[1] = -1 * self.force_magnitude['Y']
        elif self.direction['Down']:
            ret_val[1] = self.force_magnitude['Y']
        if self.direction['Forward']:
            ret_val[2] = self.force_magnitude['Z']
        elif self.direction['Backward']:
            ret_val[2] = -1 * self.force_magnitude['Z']
        return ret_val
