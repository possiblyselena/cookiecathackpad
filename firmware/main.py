import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.ENTER, KC.LFCTRL, KC.AT, KC.Y, KC.C, KC.V,]
]

if __name__ == '__main__':
    keyboard.go()
