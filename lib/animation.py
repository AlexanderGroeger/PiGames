ANIM_INFINITY = 0
import lib.globals as G
import numpy as np

def Infinity(width=24,height=14,seconds_per_cycle=3):
    def internal(start_tick):
        t = ((G.t - start_tick) % (seconds_per_cycle*G.fps)) / (seconds_per_cycle*G.fps)
        dx, dy = width//2*np.cos(2*np.pi*(t-.25)), -height//2*np.sin(4*np.pi*t)
        return dx, dy
    return internal
