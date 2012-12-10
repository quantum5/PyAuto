import ctypes

from pyauto import error

user32 = ctypes.windll.user32
SWP_NOMOVE   = 0x0002
SWP_NOZORDER = 0x0004
SWP_NOSIZE   = 0x0001
HWND_BOTTOM  = 1
HWND_TOP     = 0

class Window(object):
    def __init__(self, name):
        self.handle = user32.FindWindow(None, name)
        if not self.handle:
            raise error.WindowNotFoundError
    
    @classmethod
    def from_class(cls, name):
        self = cls.__new__(cls)
        self.handle = user32.FindWindow(name, None)
        if not self.handle:
            raise error.WindowNotFoundError
        return self
    
    def setsize(self, x, y):
        self._SetWindowPos(0, 0, x, y, None, SWP_NOMOVE | SWP_NOZORDER)
        return self
    
    def setpos(self, x, y):
        self._SetWindowPos(x, y, 0, 0, None, SWP_NOSIZE | SWP_NOZORDER)
        return self
    
    def top(self):
        self._SetWindowPos(0, 0, 0, 0, HWND_TOP, SWP_NOSIZE | SWP_NOSIZE)
        return self
    
    def bottom(self):
        self._SetWindowPos(0, 0, 0, 0, HWND_BOTTOM, SWP_NOSIZE | SWP_NOSIZE)
        return self
    
    def _SetWindowPos(self, x, y, cx, cy, z, flags):
        user32.SetWindowPos(self.handle, z, x, y, cx, cy, flags)
