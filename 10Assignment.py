name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for lines in handle: 
    lines = lines.rstrip().split() #Splits text into lines 
    if "From" in lines: #Finds "From in text file
        for words in lines[5:6]: #figures out the hour it was sent
            counts[words[0:2]] = counts.get(words[0:2],0) + 1 #adds time and frequency to dictionary


for key, value in sorted(counts.items()): #prints sorted(by hour) list of time and frequency
    print key, value 
