import pyautogui
import time
import random


# --------------- INFORMATION ---------------
#
# Укажите координаты куда кликать под ваш экран
# Софт будет кликать бесконечно открывая - закрывая позиции
# по максимальному объему на споте
#
# --------------- CONFIG ---------------

boy_b = (2910, 285)         # Кнопка BUY (раздел BUY/SELL)

sell_b = (2970, 284)        # Кнопка SELL (раздел BUY/SELL)

max_b = (3214, 448)         # Координаты ползунка в режим максимум

main_button = (3055, 591)   # Основная кнопка открытия позиции

SLEEP_MIN = 0.5             # Мин. задержка между действиями
SLEEP_MAX = 3.5             # Макс. задержка между действиями

# --------------- END CONFIG ---------------

coordinates = [boy_b, max_b, main_button, sell_b, max_b, main_button]  # Порядок клика


time.sleep(3)

try:
    # В бесконечном цикле открываем - закрываем позиции
    while True:

        # Поочереди для всех координат
        for x, y in coordinates:

            # Клик по указанным координатам
            pyautogui.click(x, y)

            # Случайная задержка между кликами
            sleep_delay = random.uniform(SLEEP_MIN, SLEEP_MAX)
            time.sleep(sleep_delay)

except KeyboardInterrupt:
    print("\nОстановлено пользователем.")
