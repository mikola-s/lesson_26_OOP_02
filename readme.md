##Дз к уроку 26. ООП 02. Дандер методы

####1) Написать класс, который будет работать с контекстным менеджером, чтобы можно профилировать участок кода.



```python


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


```

результат

```

start work on: Sun Nov 24 15:53:19 2019
 stop work on: Sun Nov 24 15:53:20 2019
   time spent: 1.0011 sec

start work on: Sun Nov 24 15:53:20 2019
 stop work on: Sun Nov 24 15:53:22 2019
   time spent: 2.0017 sec

Process finished with exit code 0


```


[ссылка на файл](/task_01/lsn_26_task_01.py)


-------


####2) Написать класс, который будет читать .csv любых размеров, и будет отдавать ответ построчно аля генератор🤔



```python

from os import path as check_path
from sys import exit


class CsvReader:
    red = '\033[91m'
    white = '\033[0m'

    def __init__(self, path=None):
        if path is not None:
            if check_path.exists(path) and check_path.isfile(path):
                self.path = path
                self.file = open(self.path, 'r')
                self.generator = (line for line in self.file)
            else:
                exit(f"\n{self.red}задайте правильный путь и имя файла{self.white}\n")
        else:
            exit(f"\n{self.red}задайте путь и имя файла{self.white}\n")

    def __del__(self):
        self.file.close()

    def __enter__(self):
        self.file = open(self.path, 'r')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def print_next(self, count: int = 1) -> None:
        """печатает count линий из файла если не достигнут конец файла"""

        for counter in range(count):
            try:
                print(next(self.generator), end="")
            except StopIteration:
                print(f"\n\n{self.red}достигнут конец файла!!!\n{self.white}")
                break

    def print_all(self) -> None:
        for line in self.generator:
            print(line, end="")


csv = CsvReader('convertcsv.csv')

with csv:
    print(next(csv.generator).split(","))

csv.print_next(5)


```

результат

```

['first', ' last', ' email', ' phone', ' age', ' gender', ' state', ' street', ' postal', ' sentence\n']
Bertha,Harvey,coh@atte.lt,(359) 463-1547,41,Female,ND,Fufa Key,G2A 2K0,Vuzanuege leurwek hec jonu viucfu rokrazak golu ureehook wat ihhakema liw ektub.
Gussie,Hernandez,buahaheh@ivji.at,(915) 866-2609,43,Female,DE,Zijbov Parkway,J7V 4T3,Kepred tohjizis iconum osi ute wal folle ze keg cazonci rulcoto dude he.
Etta,Martinez,dose@vurfi.dk,(677) 426-2539,50,Female,OR,Dozwi Loop,C6I 0W7,Usirov ojruzo bohle oli suwapwu lef ro lig giniz ofi aju ripeam.
Nathaniel,Goodman,ura@okuhi.it,(467) 383-9058,20,Male,MS,Pirnez Lane,A2R 1B0,Tikep bavere zefpak titlogteg osbewis livfa cu erahojji epe gefkel orujuwwek idiru balivo mafothid igi ta mote.
Luis,Barrett,tibow@zuek.kg,(532) 677-7965,30,Male,OR,Ehce Junction,G2H 7V0,Nohfoplim dazsijham kuzivu wojbah dawga foprun omubezwus temos ar lalow nudkec azu isno.

Process finished with exit code 0

```


[ссылка на файл](/task_02/lsn_26_task_02.py)


-------


