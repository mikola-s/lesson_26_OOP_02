# Написать класс, который будет работать
# с контекстным менеджером, чтобы можно профилировать участок кода.

from time import time, sleep, ctime


class OverWatch:

    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def __enter__(self):
        self.start_time = time()
        print(f"\nstart work on: {ctime(self.start_time)}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time()
        print(f" stop work on: {ctime(self.stop_time)}\n"
              f"   time spent: {round(self.stop_time - self.start_time, 4)} sec")

    def start(self):
        self.start_time = time()
        print(f"\nstart work on: {ctime(self.start_time)}")

    def stop(self):
        if self.start_time is not None:
            self.stop_time = time()
            print(f' stop work on: {ctime(self.stop_time)}\n'
                  f'   time spent: {round(self.stop_time - self.start_time, 4)} sec')
        else:
            print("\n\033[91mOverWatch.start() не определен\033[0m")


over_watch = OverWatch()

with over_watch:
    sleep(1)  # участок кода

over_watch.start()
sleep(2)  # участок кода
over_watch.stop()

