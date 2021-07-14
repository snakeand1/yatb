from pynput import keyboard

from utils.events import Events, on_event
from utils.labelers import Labelers
from utils.settings import Settings


callbacks = {
    Events.SWIPE_LEFT: Labelers.DISLIKE(),
    Events.SWIPE_RIGHT: Labelers.LIKE(),
}


def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press=lambda _: on_event(_, callbacks),
    on_release=on_release
    ) as listener:
    listener.join()
