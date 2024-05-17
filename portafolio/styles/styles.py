import reflex as rx
from .fonts import Font
from .colors import Color, TextColor
from enum import Enum


MAX_WIDTH = "1500px"
WIDTH_IMAGE = "25em"
HEIGHT_IMAGE = "45em"
HEIGHT_IMAGE2 = "17em"

BORDER_RADIUS = "15em"

WIDTH_CARD = "12em"

class Size(Enum):
    ZERO = "0"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    NOTSOBIG = "3.5em"
    VERYBIG = "5em"
    VERYVERYBIG = "7em"


STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Roboto"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.DARK.value,
    "backgroung" : Color.WHITE.value,
}
