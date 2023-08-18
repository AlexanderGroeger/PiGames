from lib.abstract import Instance
from lib.text import Text
from lib.input.snes import *
import lib.globals as G
from pygame.font import SysFont

class Controller(Instance):
    def __init__(self,controller,**kwargs):
        controller.init()
        self.controller = controller
        self.info = {}

        super().__init__(**kwargs)

    def draw_button(self,surf,id,pressed = False):
        dx, dy = G.SNES_GRAPHIC_POSITION[id]
        gfx = G.SNES_GRAPHICS[id].copy()
        sx, sy = gfx.get_size()
        if pressed:
            gfx.set_alpha(255)
        else:
            gfx.set_alpha(64)
        surf.blit(gfx,(self.x+dx-sx/2,self.y+dy-sy/2))

    def draw_controller_id(self,surf,id):
        dx, dy = G.SNES_GRAPHIC_POSITION[id]
        font = SysFont('Comic Sans MS', 16)
        text_surface = font.render(str(self.controller.get_instance_id()), True, (192,)*3)
        sx, sy = text_surface.get_size()
        surf.blit(text_surface,(self.x+dx-sx/2,self.y+dy-sy/2))

    def draw_joystick(self,surf,id,dir = (0,)*2):
        dx, dy = G.SNES_GRAPHIC_POSITION[id]

        h, v = dir
        if v < -0.25:
            id += "_up"
        elif v > 0.25:
            id += "_down"
        if h < -0.25:
            id += "_left"
        elif h > 0.25:
            id += "_right"


        gfx = G.SNES_GRAPHICS[id].copy()
        sx, sy = gfx.get_size()
        surf.blit(gfx,(self.x+dx-sx/2,self.y+dy-sy/2))

        if self.info.get(id+"_v"):
            self.info[id+"_v"].setText(f"{v:.2f}")
        else:
            self.info[id+"_v"] = Text("0",
                font = G.am.getFont("Arial",18),
                bold = True,
                color = (255,)*3,
                halign = "center",
                valign = "center",
                xy = (
                    self.x+dx,
                    self.y+dy-sy*9//16,
                )
            )
        if self.info.get(id+"_h"):
            self.info[id+"_h"].setText(f"{h:.2f}")
        else:
            self.info[id+"_h"] = Text("0",
                font = G.am.getFont("Arial",18),
                bold = True,
                color = (255,)*3,
                halign = "center",
                valign = "center",
                xy = (
                    self.x+dx-sx*9//16,
                    self.y+dy,
                )
            )
        self.info[id+"_h"].draw(surf)
        self.info[id+"_v"].draw(surf)

    def draw(self,surf):
        draw_button = lambda id, pressed = False: self.draw_button(surf,id,pressed)
        draw_joystick = lambda id, dir = (False,)*4: self.draw_joystick(surf,id,dir)

        draw_button('a',self.controller.get_button(A_BUTTON))
        draw_button('b',self.controller.get_button(B_BUTTON))
        draw_button('x',self.controller.get_button(X_BUTTON))
        draw_button('y',self.controller.get_button(Y_BUTTON))
        draw_button("start",self.controller.get_button(START_BUTTON))
        draw_button("select",self.controller.get_button(SELECT_BUTTON))
        draw_button("left_shoulder",self.controller.get_button(LEFT_SHOULDER_BUTTON))
        draw_button("right_shoulder",self.controller.get_button(RIGHT_SHOULDER_BUTTON))
        draw_button('dpad_right',self.controller.get_axis(HSTICK1)>0)
        draw_button('dpad_left',self.controller.get_axis(HSTICK1)<0)
        draw_button('dpad_up',self.controller.get_axis(VSTICK1)<0)
        draw_button('dpad_down',self.controller.get_axis(VSTICK1)>0)
        self.draw_controller_id(surf,'device_num')
        # draw_joystick("dpad",
        #     dir = (
        #         self.controller.get_button(RIGHT_DPAD)-self.controller.get_button(LEFT_DPAD),
        #         self.controller.get_button(DOWN_DPAD)-self.controller.get_button(UP_DPAD),
        #     )
        # )
