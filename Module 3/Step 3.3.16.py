import sys

for number in sys.stdin:
    number = number.strip()
    try:
        a = sum(int(i) for i in number[0::2])
        b = sum(int(i) for i in number[1::2])
        if (a - b) % 3 == 0:
            print(number)
    except Exception:
        pass
