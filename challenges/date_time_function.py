# Zadanie - śledzenie czasu pracy nad projektem
# W tym zadaniu użyjesz modułu time i datetime do symulacji prostego
# systemu śledzenia czasu pracy nad projektem. Nauczysz się używać
# różnych funkcji związanych z czasem i datą.
#
# 1) Użyj modułu datetime, aby zapisać czas rozpoczęcia pracy nad projektem
# jako zmienną 'start_time'.
# 2) Symuluj prac.e nad projektem przez wywołanie time.sleep() z losowo
# wybranym krótkim czasem (np. od 1 do 5 sekund)
# 3) Użyj modułu datetime ponownie, aby zapisać czas zakończenia pracy
# nad projektem jako zmienną 'end_time'.
# 4) Oblicz łączny czas pracy nad projektem przez odjęcie 'start_time'
# od 'end_time' i wyświetl wynik
# 5) Jeśli łączny czas pracy przekracza 3 sekundy, wyświetl komunikat
# o dużej ilości włożonego czasu, w przeciwnym razie poinformuj o krótkim czasie pracy
#
# Rozwiązanie:

import datetime
import time
import random

start_time = datetime.datetime.now()
time.sleep(random.randint(1, 5))
end_time = datetime.datetime.now()

working_time = end_time - start_time
print(f"Time of work on project: {working_time}")

if working_time > datetime.timedelta(seconds=3):
    print("You spend much work on this project.")
else:
    print("You spend less work on this project.")


