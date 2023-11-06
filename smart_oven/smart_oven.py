from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time


board = CustomTelemetrix(arduino_instance_id=1)


LED_GREEN = 5
LED_RED = 4
BUZZER = 3


def set_cooking_time(count_time_minutes):
    global timer
    timer = count_time_minutes * 60
    board.analog_write(BUZZER, 1)
    time.sleep(1.5)
    board.analog_write(BUZZER, 0)
    board.digital_write(LED_RED, 1)
    board.digital_write(LED_GREEN, 0)


def countdown_timer():
    global timer
    while timer > 0:
        timer -= 1
        time.sleep(1)
        board.displayShow(timer)
        print(timer)
        


def cooking_done():
    board.digital_write(LED_RED, 0)
    board.digital_write(LED_GREEN, 1)


def loop():
    timer_set = float(input('How long does the pizza need to be in the oven (minutes): '))
    set_cooking_time(timer_set)
    countdown_timer()
    cooking_done()
    time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            print('Shutdown')
            board.shutdown()
            break