class Instance:

    def __init__(self, xy = (0,0), depth = 0, **kwargs):
        self.x, self.y = xy
        self.depth = 0
        # if kwargs:
        #     print(kwargs)

    def step(self):
        pass

    def draw(self):
        pass

class Object(Instance):

    def __init__(self, hspeed = 0, vspeed = 0, **kwargs):
        self.hspeed = hspeed
        self.vspeed = vspeed
        Instance.__init__(self, **kwargs)

    def step(self):
        self.x += self.hspeed
        self.y += self.vspeed
