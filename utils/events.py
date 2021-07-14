from pynput import keyboard


class Events:
    """Events with according keyboard keys"""
    SWIPE_LEFT = keyboard.Key.left
    SWIPE_RIGHT = keyboard.Key.right
    

def on_event(event, callback):
    for e, f in callback.items():
        if e == event:
            f()