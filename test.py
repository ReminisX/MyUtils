import time

from progress.bar import ShadyBar

bar = ShadyBar()
for i in bar(range(10)):
    time.sleep(0.1)
