import dragon
import shield


class Controlers(dragon.Dragon, shield.Shield):
    def __init__(self):
        super().__init__()

    def control_keys(self, player_control, coor_axis, valoreve, axisnumx, axisnumy, joynum):
        if player_control == joynum:  #
            if coor_axis == axisnumx:
                if abs(valoreve) > 0.4:
                    self.dir.x = valoreve
                else:
                    self.dir.x = 0
            if coor_axis == axisnumy:
                if abs(valoreve) > 0.4:
                    self.dir.y = valoreve
                else:
                    self.dir.y = 0
