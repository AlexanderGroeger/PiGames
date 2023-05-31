import lib.input.gamecube as gc
import lib.input.snes as snes

class Controller:
    def __init__(self,joystick):
        self.joystick = joystick
        self.framesButtonHeld = {}

    def input(self):
        for button, framesHeld in self.framesButtonHeld.items():
            if self.joystick.get_button(button):
                self.framesButtonHeld[button] += 1
            else:
                if framesHeld > 0:
                    self.framesButtonHeld[button] *= -1
                else:
                    self.framesButtonHeld[button] = 0

class GameCubeController(Controller):
    def __init__(self,joystick):
        super(GameCubeController,self).__init__(joystick)
        self.framesButtonHeld = {
            gc.A_BUTTON: 0,
            gc.B_BUTTON: 0,
            gc.X_BUTTON: 0,
            gc.Y_BUTTON: 0,
            gc.Z_BUTTON: 0,
            gc.START_BUTTON: 0,
            gc.LEFT_SHOULDER_BUTTON: 0,
            gc.RIGHT_SHOULDER_BUTTON: 0,
        }


class SNESController(Controller):
    def __init__(self,joystick):
        super(SNESController,self).__init__(joystick)
        self.framesButtonHeld = {
            snes.A_BUTTON: 0,
            snes.B_BUTTON: 0,
            snes.X_BUTTON: 0,
            snes.Y_BUTTON: 0,
            snes.START_BUTTON: 0,
            snes.SELECT_BUTTON: 0,
            snes.LEFT_SHOULDER_BUTTON: 0,
            snes.RIGHT_SHOULDER_BUTTON: 0,
        }
        self.PRIMARY_BUTTON = snes.A_BUTTON
        self.SECONDARY_BUTTON = snes.B_BUTTON
        self.SPECIAL_1_BUTTON = snes.X_BUTTON
        self.SPECIAL_2_BUTTON = snes.Y_BUTTON
        self.LEFT_BUTTON = snes.LEFT_SHOULDER_BUTTON
        self.RIGHT_BUTTON = snes.RIGHT_SHOULDER_BUTTON
        self.PRIMARY_H_AXIS = snes.HSTICK1
        self.PRIMARY_V_AXIS = snes.VSTICK1


controller_guids = {
    "03000069790000002601000000000000": SNESController
}
