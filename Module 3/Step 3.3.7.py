import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    f = re.findall(r"cat", line)
    if len(f) >= 2:
        print(line)
