import numexpr, keyboard # pip install numexpr keyboard
import numpy as np  # pip install numpy
from fast_ctypes_screenshots import ScreenshotOfRegion # pip install fast-ctypes-screenshots
from mousekey import MouseKey  # pip install mousekey
from locate_pixelcolor_c import search_colors  # pip install locate-pixelcolor-c
ativo = False
mkey = MouseKey()
mkey.enable_failsafekill("ctrl+e")
distancediff0, distancediff1 = 30, 30
c = 660, 371, 1240, 790
colorndarray = np.ascontiguousarray(np.array([tuple(reversed((255, 219, 195)))], dtype=np.uint8))
def on_off():
    global ativo
    ativo = not ativo
def numexpr_diff(arra, dis):
    aa = np.insert(arra[:-1], 0, 0)
    return numexpr.evaluate(f"abs(aa-arra) > {dis}")
def click_mouse(colfound2, goodcords):
    _ = [None for y, x in colfound2[goodcords]
         if mkey.left_click_xy((x + c[0]),
                               (y + c[1]), 0.000001)]
def main(shot):
    if not ativo: return
    colfound2 = search_colors(shot, colorndarray)
    return click_mouse(colfound2,
        np.where((numexpr_diff(colfound2[..., 0],
                               distancediff0))
            | (numexpr_diff(colfound2[..., 1],
                            distancediff1)) )[0],)
if __name__ == "__main__":
    keyboard.add_hotkey("ctrl+alt+k", on_off)
    with ScreenshotOfRegion(*c, ascontiguousarray=False)\
            as screenshots_region:
        _ = list((None for shot in screenshots_region
                  if main(shot)))
