from lib.abstract import Instance
import lib.globals as G

class Text(Instance):

    def __init__(self, text, font = G.am.getFont("Arial",24),
                antialias = False, color = (0,0,0), alpha = 255,
                halign = 'left', valign = 'top',
                **kwargs):

        self.text = text
        self.font = font
        self.x_alignment, self.y_alignment = 0, 0
        self.antialias = antialias
        self.color = color
        self.alpha = alpha
        self.halign = halign
        self.valign = valign
        self.__alignment()
        self.render()
        
        super().__init__(**kwargs)


    def draw(self,surf):
        surf.blit(self.surf,(self.x+self.x_alignment,self.y+self.y_alignment))

    def render(self):
        self.surf = self.font.render(self.text, self.antialias, self.color)
        self.surf.set_alpha(self.alpha)

    def setText(self, text):
        self.text = text
        self.__alignment()
        self.render()

    def setColor(self,color):
        self.color = color
        self.render()

    def setAlpha(self,alpha):
        self.alpha = alpha
        self.render()

    def __alignment(self):
        tw, th = self.font.size(self.text)

        if self.halign == 'left':
            self.x_alignment = 0
        elif self.halign == 'center':
            self.x_alignment = -tw//2
        elif self.halign == 'right':
            self.x_alignment = -tw

        if self.valign == 'top':
            self.y_alignment = 0
        elif self.valign == 'center':
            self.y_alignment = -th//2
        elif self.valign == 'bottom':
            self.y_alignment = -th
