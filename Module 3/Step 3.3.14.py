import re, sys
for line in sys.stdin:
    line = re.sub(r'\b(\w)(\w)', r'\2\1', line.strip())
    print(line)
