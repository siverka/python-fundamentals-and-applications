import re, sys

for line in sys.stdin:
    line = re.sub(r'(\w)\1+', r'\1', line.strip())
    print(line)
# line = 'attractionnnn'
# line = 'attraction'
# line = 'buzzzz'
