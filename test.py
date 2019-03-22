from random import randint
import pyautogui


def rand_coord(x_low, y_low, x_range, y_range):
    """Simple random coordinate generator with bounds"""
    x = randint(x_low, x_low + x_range)
    y = randint(y_low, y_low + y_range)

    return pyautogui.moveTo(x, y, 0)

