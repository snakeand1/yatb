from pathlib import Path
from time import time
from typing import Any, Container, Dict, Optional

from pyautogui import screenshot
from PIL.Image import Image

from .settings import Settings


class Screenshot:

    def __init__(self, image: Optional[Image] = None):
        self.image = image

    @classmethod
    def from_screen(cls, bbox: Optional[Container[int]] = None):

        if not bbox:
            return cls(image=screenshot())

        return cls(image=screenshot(region=bbox))


class LabeledScreenshot(Screenshot):

    def __init__(self, image: Optional[Image] = None, label: Optional[int] = None, filename: Optional[str] = None, path: Optional[str] = None):
        super().__init__(image)
        self.label = label
        self.filename = filename
        self.path = path

    def set_label(self, label: Optional[int] = None):
        self.label = label
        return self

    def set_filename(self, filename: Optional[str] = None):
        if not filename:
            self.filename = f'{int(time())}.png'
            self.path = Path(f'data/{self.label}')

        if not self.path.exists():
            self.path.mkdir(parents=True, exist_ok=True)

        return self

    def save(self):
        self.image.save(self.path / self.filename)


class Labeler:

    def __init__(self):
        pass

    def __call__(self):
        pass


class Like(Labeler):

    def __init__(self, bbox=Settings.BOUNDING_BOX):
        self.bbox = bbox

    def __call__(self):
        LabeledScreenshot.from_screen(self.bbox).set_label(1).set_filename().save()


class Dislike(Labeler):

    def __init__(self, bbox=Settings.BOUNDING_BOX):
        self.bbox = bbox

    def __call__(self):
        LabeledScreenshot.from_screen(self.bbox).set_label(0).set_filename().save()


class Labelers:
    LIKE = Like
    DISLIKE = Dislike
