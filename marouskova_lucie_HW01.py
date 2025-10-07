import json

with open("data/alice.txt", mode="r", encoding="utf-8") as file:
    text = file.read()
    text = text.lower()

counts = {}

for znak in text:
    if znak != " " and znak != "\n":
        if znak in counts:
            counts[znak] += 1
        else:
            counts[znak] = 1


counts = dict(sorted(counts.items()))


with open("hw01_output.json", "w", encoding="utf-8") as vystup:
    json.dump(counts, vystup, indent=4, ensure_ascii=False)