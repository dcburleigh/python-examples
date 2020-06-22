
import sys

na = len(sys.argv)
print(f"{na} args given")

n = 0
for a in sys.argv:
    print(f"{n}) arg={a} ")
    n += 1
