# Bill Nicholson
# nicholdw@ucmail.uc.edu
import csv

with open('StatesAndCapitals.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) # skip the header row.
    for row in csvreader:
        state = row[0]
        capital = row[1]
        print(f"State: {state}, Capital: {capital}")