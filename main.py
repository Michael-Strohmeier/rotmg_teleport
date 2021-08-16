import time
import cv2
import pyautogui
import win32gui
import numpy as np


def capture(hwnd, menu_bar_offset=0):
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))

    return pyautogui.screenshot(region=(x, y + menu_bar_offset, x1, y1 - menu_bar_offset))


def check_health(img):
    num_red = 0

    img_arr = np.array(img)
    for pixel_row in img_arr:
        for pixel in pixel_row:
            if pixel[0] >= 190:
                num_red += 1

    percentage_red = num_red / (img_arr.size / 3)
    return percentage_red


def teleport_nexus(health_percent: float, nexus_key_bind: str, threshold=0.25):
    if health_percent <= threshold:
        pyautogui.keyDown(nexus_key_bind)
        time.sleep(0.025)
        pyautogui.keyUp(nexus_key_bind)


if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, r"RotMGExalt")
    win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)
    # win32gui.MoveWindow(hwnd, 0, 0, 380, 380, True)

    nexus_key_bind = "p"
    left, top, right, bottom = 620, 260, 790, 270

    while True:
        screen = capture(hwnd, menu_bar_offset=16)
        # image = image.convert("L")

        img_cropped = screen.crop((left, top, right, bottom))
        img_cropped = np.array(img_cropped)

        health_percent = check_health(img_cropped)
        print(health_percent)

        # converting only for the display
        img_cropped = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2RGB)

        teleport_nexus(health_percent=health_percent, nexus_key_bind=nexus_key_bind)

        cv2.imshow("screen", img_cropped)
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break

    print("DONE")
