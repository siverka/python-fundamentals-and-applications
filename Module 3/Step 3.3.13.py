import re, sys

for line in sys.stdin:
    print(re.sub(r'\ba+\b', 'argh', line.strip(), 1, re.IGNORECASE))
