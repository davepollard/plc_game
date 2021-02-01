import time
import snap7


class PlcInterface:
    """
    Interface with PLC
    Each joystick interface returns range -1 -> 1
    """

    def __init__(self):
        pass

    @property
    def js1_x(self):
        return 0

    @property
    def js1_y(self):
        return 0

    @property
    def js2_x(self):
        return 0

    @property
    def js2_y(self):
        return 0


if __name__ == '__main__':
    plc_test = PlcInterface()
    while(True):
        xy_1 = [plc_test.js1_x, plc_test.js1_y]
        xy_2 = [plc_test.js2_x, plc_test.js2_y]

        print([1, xy_1])
        print([2, xy_2])
        print('---------')
        time.sleep(1)
