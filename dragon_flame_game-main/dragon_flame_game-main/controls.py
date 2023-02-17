import dragon
import shield


class Controls(dragon.Dragon, shield.Shield):
    def __init__(self):
        super().__init__()

    def shield_control_keys(self, player_control, coor_axis, valoreve, axisnumy, joynum, speed):
        if player_control == joynum:
            if coor_axis == axisnumy:
                if abs(valoreve) > 0.4:
                    self.dir.y = valoreve * speed
                else:
                    self.dir.y = 0

    def dragons_control_keys(self, player_control, coor_axis, valoreve, axisnumx, axisnumy, joynum, speed):
        if player_control == joynum:
            if coor_axis == axisnumx:
                if abs(valoreve) > 0.4:
                    self.dir.x = valoreve * speed
                else:
                    self.dir.x = 0
        Controls.shield_control_keys(self, player_control, coor_axis, valoreve, axisnumy, joynum, speed)
