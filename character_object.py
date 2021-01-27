from controller_system import Controller


class CharacterObject:

    def __init__(self, params):
        self.screen_size = params['SCREEN_SIZE']
        self.size = params['CHARACTER_SIZE']
        self.bounce_coefficient = 0.9

        self.init_position = [i/2 for i in self.screen_size]
        self.position = self.init_position.copy()
        self.velocity = [0, 0]

        self.controller = Controller()

        self.mass = 20

    def update(self, event_list):
        self.controller.update(event_list)
        applied_force = self.controller.force
        acceleration = [f/self.mass for f in applied_force]
        self.velocity = [v+a for (v, a) in zip(self.velocity, acceleration)]
        self.position = [p+v for (p, v) in zip(self.position, self.velocity)]

        self._check_impact()

    def _check_impact(self):
        if self.position[0] < self.size[0]/2 or self.position[0] > self.screen_size[0]-self.size[0]/2:
            self.velocity[0] *= -1 * self.bounce_coefficient
        if self.position[1] < self.size[1]/2 or self.position[1] > self.screen_size[1]-self.size[1]/2:
            self.velocity[1] *= -1 * self.bounce_coefficient

    @property
    def current_position(self):
        return self.position
