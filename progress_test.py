from time import sleep
from progress.bar import Bar
import random


while True:

    random_number = random.randint(100, 500)

    with Bar("Hold on a sec...", fill="#", max=random_number) as bar:
        for i in range(random_number):
            sleep(0.05)
            bar.next()
