import json

with open("data/alice.txt", mode="r", encoding="utf-8") as file:
    text = file.read()
    text = text.lower()

counts = {}

for character in text:
    if character != " " and character != "\n":
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1


counts = dict(sorted(counts.items()))


with open("hw01_output.json", "w", encoding="utf-8") as vystup:
    json.dump(counts, vystup, indent=4, ensure_ascii=False)