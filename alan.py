import pyautogui as auto
import time

time.sleep(2)

auto.dragRel(50, 250, duration=.8)
auto.dragRel(50, -110, duration=.8)
auto.dragRel(50, 130, duration=.8)
auto.dragRel(50, -180, duration=.8)

auto.moveRel(-95, -70)

auto.dragRel(-90, 250, duration=.8)
auto.dragRel(90, -250, duration=.8)
auto.dragRel(90, 290, duration=.8)
