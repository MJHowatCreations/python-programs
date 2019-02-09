import re
fulltext = open('regex_sum_250508.txt')
#total = 0

#for lines in fulltext:
 #   total = total + sum( [ int(r) for r in re.findall('[0-9]+', lines) ] )
 
#print total
print sum( [ int(r) for r in re.findall('[0-9]+', fulltext.read() ) ] )
#Opens a file and finds all the numbers in it and adds them up
#two different ways to do it with the used one being the most compact