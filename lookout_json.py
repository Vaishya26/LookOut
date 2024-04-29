import csv
import json

keys = ["roll_deg", "pitch_deg", "heading_deg", "latitude", "longitude", "cog", "spd", "acc_a", "acc_b", "acc_c"]

with open("furuno_15.txt", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = [dict(zip(keys, row)) for row in csvreader]

with open("furuno_15.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=2)