import ctypes
import time

__all__ = ['swapped', 'translate', 'click', 'down', 'up',
           'LEFT', 'MIDDLE', 'RIGHT', 'PRIMARY', 'SECONDARY']

LEFT = 0
MIDDLE = 1
RIGHT = 2
PRIMARY = 3
SECONDARY = 4

user32 = ctypes.windll.user32
GetSystemMetrics = user32.GetSystemMetrics
mouse_event = user32.mouse_event

_key_down = {
    LEFT: 0x2,
    MIDDLE: 0x20,
    RIGHT: 0x8,
}

SM_SWAPBUTTON = 23

def swapped():
    return bool(GetSystemMetrics(SM_SWAPBUTTON))

def translate(key, up):
    if key < 3:
        if up:
            return _key_down[key] << 1
        else:
            return _key_down[key]
    elif key == PRIMARY:
        return translate(RIGHT if swapped() else LEFT, up)
    elif key == SECONDARY:
        return translate(LEFT if swapped() else RIGHT, up)

def click(key, x=None, y=None, wait=None):
    if x is not None and y is not None:
        move(x, y)
    hit(key)
    if wait is not None:
        time.sleep(wait)

def hit(key):
    down(key)
    up(key)

def down(key):
    mouse_event(translate(key, 0), 0, 0, 0, 0)

def up(key):
    mouse_event(translate(key, 1), 0, 0, 0, 0)

def move(x, y, wait=None):
    SetCursorPos(x, y)
    if wait is not None:
        time.sleep(wait)
