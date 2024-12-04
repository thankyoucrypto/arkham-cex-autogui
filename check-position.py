import pyautogui
import time


while True:
    try:
        x, y = pyautogui.position()
        print(f"Координаты мыши: X={x}, Y={y}")  # Перезаписывает строку
        time.sleep(0.1)  # Уменьшает частоту обновления, чтобы не перегружать консоль

    except KeyboardInterrupt:
        print("\nВыход из программы.")
