# 高速クリック
import pyautogui
import time
import keyboard

x, y = 0, 0


def main():
    while True:
        pyautogui.click(x, y)
        # クリック間隔を短くして高速化
        if keyboard.is_pressed('q'):
            break
        # time.sleep(0.001)  # 1ms待機でCPU負荷を抑えつつ高速化
if __name__ == "__main__":
    while True:
        while True:
            if keyboard.is_pressed('s'):
                break
        x, y = pyautogui.position()
        main()