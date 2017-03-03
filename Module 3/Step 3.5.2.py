import csv

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    crimes = [row['Primary Type'] for row in reader if '2015' in row['Date']]
    counts = {e: crimes.count(e) for e in set(crimes)}
    print(sorted(counts.items(), key=lambda x: x[1]))
