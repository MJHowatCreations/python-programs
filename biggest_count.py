name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fulltext = open(name)
counts = dict()

for lines in fulltext:
    lines = lines.rstrip().split()
    if "From" in lines:
        fromword = lines[1]
        counts[fromword] = counts.get(fromword,0) + 1

biggest_address = None
biggest_count = None

for word, values in counts.items():
    if biggest_count == None or values > biggest_count:
        biggest_count = values
        biggest_address = word

print biggest_address, biggest_count

#goes through a text file and finds the most commonly used word and how often it was used