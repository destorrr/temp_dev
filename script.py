import math
import sys
from os import rename

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeting = f"hello {who_to_greet}"
    return greeting


r = requests.get("http://ya.ru")
print(r.status_code)
