from controller_system import Controller
from plc_interface import PlcInterface


class PlcController(Controller):
    def __init__(self):
        # Initialise PLC interface
        self.force_max_magnitude = {'X': 10, 'Y': 10, 'Z': 10}
        self.plc_interface = PlcInterface()
        self.force_vectors = {'X': 0, 'Y': 0, 'Z': 0}

    def update(self, _):
        self.force_vectors['X'] = self.plc_interface.js1_x * self.force_max_magnitude['X']
        self.force_vectors['Y'] = self.plc_interface.js1_y * self.force_max_magnitude['Y']
        self.force_vectors['Z'] = self.plc_interface.js2_x * self.force_max_magnitude['Z']

    @property
    def force(self):
        return [f for f in self.force_vectors.values()]
