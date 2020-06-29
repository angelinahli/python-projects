# Filename:    i94_parser.py
# Author:      Angelina Li
# Date:        2020.06.29
# Version:     Python 3
# Description: Every now and again I need to re-parse my I-94 travel history
#              to get a list of when my arrivals and departures from the US have been,
#              usually requiring a csv where each row is for each visit.
#              Since the I-94 website hasn't changed in a while, it seems easier to
#              just save this script instead of rewriting it every time it is needed.
#              Outputs a i94_visits.csv file.

import csv
import datetime

## CHANGE INPUT HERE
# delete header row
# text should start with '1', as with the below example
raw_text = """1   
2020-05-02
Arrival
SFR"""

# remove empty lines
lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

entries = []
ordered_columns = ["i", "date", "type", "location"]
assert len(lines) % len(ordered_columns) == 0
for i in range(0, len(lines), len(ordered_columns)):
    entry_lines = lines[i:i + len(ordered_columns)]
    entry_data = dict(zip(ordered_columns, entry_lines))
    y, m, d = map(int, entry_data["date"].split("-"))
    entry_data["date"] = datetime.date(y, m, d)
    entries.append(entry_data)

# reverse entries for this next step
ordered_entries = entries[::-1]
ordered_visits = []

# round the max i to visit up 
for i in range(0, len(ordered_entries), 2):
    visit_data = dict()
    arrival = ordered_entries[i]
    assert arrival["type"] == "Arrival"
    visit_data["Arrival_Year"] = arrival["date"].year
    visit_data["Arrival_Date"] = arrival["date"].isoformat()
    visit_data["Arrival_Location"] = arrival["location"]
    # if yes, there is a departure associated with this visit
    if i < len(ordered_entries) - 1:
        departure = ordered_entries[i + 1]
        assert departure["type"] == "Departure"
        visit_data["Departure_Year"] = departure["date"].year
        visit_data["Departure_Date"] = departure["date"].isoformat()
        visit_data["Departure_Location"] = departure["location"]
        visit_data["Trip_Duration"] = (departure["date"] - arrival["date"]).days
    else:
        visit_data["Trip_Duration"] = (datetime.date.today() - arrival["date"]).days

    ordered_visits.append(visit_data)

with open("i94_visits.csv", "w", newline="") as fl:
    writer = csv.DictWriter(fl, fieldnames=ordered_visits[0].keys())
    writer.writeheader()
    writer.writerows(ordered_visits)
